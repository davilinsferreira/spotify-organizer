import spotipy
import time

# --- SUA CONFIGURAÇÃO ---
# Token atualizado em 02/01/2026:
# Pede o token ao usuário quando o programa roda
ACCESS_TOKEN = input("Cole seu Token do Spotify aqui: ")

# Autenticação
try:
    print("Tentando conectar com o Token Novo...")
    sp = spotipy.Spotify(auth=ACCESS_TOKEN)
    user = sp.me()
    user_id = user['id']
    print(f"✅ Conectado como: {user['display_name']}")
except Exception as e:
    print(f"❌ Erro no token: {e}")
    exit()

# 1. Coletar Músicas (Paginação)
print("\n--- 1. Baixando sua biblioteca (Isso é rápido) ---")
results = sp.current_user_saved_tracks(limit=50)
tracks = results['items']

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

print(f"📦 Total de músicas carregadas: {len(tracks)}")

# 2. OTIMIZAÇÃO: Extrair IDs únicos e buscar em lotes (Batch)
print("\n--- 2. Buscando Gêneros (Modo Batch - 50 por vez) ---")

# Mapeia música -> ID do artista
track_artist_map = {} 
artist_ids = set()

for item in tracks:
    if item['track'] and item['track']['artists']:
        art_id = item['track']['artists'][0]['id']
        artist_ids.add(art_id)
        track_artist_map[item['track']['id']] = art_id

unique_artists = list(artist_ids)
print(f"🔍 Analisando {len(unique_artists)} artistas únicos...")

# Cache de gêneros
artist_genre_cache = {}
batch_size = 50

# Loop em blocos de 50 (Reduz chamadas drasticamente)
for i in range(0, len(unique_artists), batch_size):
    batch = unique_artists[i:i + batch_size]
    
    try:
        response = sp.artists(batch)
        for artist in response['artists']:
            if artist['genres']:
                # Pega o primeiro gênero e deixa bonitinho (Title Case)
                artist_genre_cache[artist['id']] = artist['genres'][0].title()
            else:
                artist_genre_cache[artist['id']] = "Outros"
        
        # Feedback visual simples
        print(f"Processando lote {i//batch_size + 1} de {len(unique_artists)//batch_size + 1}...")
        time.sleep(0.5) # Pequena pausa para ser gentil com a API
        
    except Exception as e:
        print(f"⚠️ Erro no lote {i}: {e}")
        time.sleep(2)

# 3. Agrupar
print("\n--- 3. Organizando dados ---")
genero_tracks = {}

for track_id, artist_id in track_artist_map.items():
    if artist_id in artist_genre_cache:
        genre = artist_genre_cache[artist_id]
        if genre == "Outros": continue
        
        if genre not in genero_tracks:
            genero_tracks[genre] = []
        genero_tracks[genre].append(track_id)

# 4. Criar Playlists
print("\n--- 4. Criando Playlists no Spotify ---")
criadas = 0

for genero, t_ids in genero_tracks.items():
    # FILTRO: Só cria playlist se tiver pelo menos 15 músicas desse gênero
    if len(t_ids) >= 15:
        playlist_name = f"Gênero: {genero}"
        print(f"📂 Criando: '{playlist_name}' ({len(t_ids)} músicas)...")
        
        try:
            pl = sp.user_playlist_create(user_id, playlist_name, public=True)
            
            # Adiciona em blocos de 100 (limite do Spotify)
            for i in range(0, len(t_ids), 100):
                sp.playlist_add_items(pl['id'], t_ids[i:i+100])
            
            criadas += 1
            time.sleep(2) # Pausa educada entre criações
            
        except Exception as e:
            print(f"Erro ao criar {playlist_name}: {e}")

print(f"\n🎉 SUCESSO! {criadas} playlists foram criadas.")
