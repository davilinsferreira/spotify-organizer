
# 1. Cria o arquivo README.md com todo o texto (Inglês e Português)
cat <<EOF > README.md
# 🎵 Spotify Genre Organizer

**[English]**
A Python script that automatically organizes your "Liked Songs" into genre-specific playlists.
Developed as a study project on API integration, algorithms, and data manipulation.

**[Português]**
Um script em Python que organiza automaticamente suas "Músicas Curtidas" em playlists específicas por gênero.
Desenvolvido como projeto de estudo sobre integração de APIs, algoritmos e manipulação de dados.

---

## 🚀 Features / Funcionalidades

- **Authentication:** Connects securely to Spotify via OAuth/Token.
- **Smart Sorting:** Analyzes the artist of each track to determine its genre.
- **Optimization:** Uses **Batch Processing** to fetch metadata for 50 artists at once, reducing API calls by ~98% and avoiding Rate Limits.
- **Playlist Creation:** Automatically creates playlists like "Genre: Rock", "Genre: Pop", etc.

- **Autenticação:** Conecta de forma segura ao Spotify via OAuth/Token.
- **Classificação Inteligente:** Analisa o artista de cada faixa para determinar o gênero.
- **Otimização:** Utiliza **Processamento em Lote** (Batch) para buscar metadados de 50 artistas por vez, reduzindo chamadas de API em ~98% e evitando bloqueios (Rate Limits).
- **Criação de Playlists:** Cria automaticamente playlists como "Gênero: Rock", "Gênero: Pop", etc.

## 🛠️ Technologies / Tecnologias

- **Language:** Python 3
- **Library:** Spotipy (Spotify Web API wrapper)
- **OS:** Linux (Pop!_OS)

## 📦 How to Run / Como Rodar

1. **Clone the repository / Clone o repositório:**
   \`\`\`bash
   git clone https://github.com/davilinsferreira/spotify-organizer.git
   cd spotify-organizer
   \`\`\`

2. **Set up the environment / Configure o ambiente:**
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   pip install spotipy
   \`\`\`

3. **Get your Access Token / Pegue seu Token de Acesso:**
   Go to [Spotify Developer Console](https://developer.spotify.com/console/get-current-user-saved-tracks/) and generate a token with \`playlist-modify-public\` scope.
   
   Acesse o [Spotify Developer Console](https://developer.spotify.com/console/get-current-user-saved-tracks/) e gere um token com permissão \`playlist-modify-public\`.

4. **Run / Execute:**
   \`\`\`bash
   python3 organizar.py
   \`\`\`

---
*Developed by / Desenvolvido por: Davi Lins Ferreira*
