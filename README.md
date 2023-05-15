# Spotipy
Répertoire pour un projet privé de dépôt et gestion de playlists sur Spotify

## Initialisation
installation du module de **Spotipy** via Pip

	pip install spotipy
## API Spotify

### Création

Rendez vous à cette addresse : https://developer.spotify.com/dashboard

Elle permet de se creer un accès automate afin de pouvoir se connecter à ses playlists

**Cliquez sur le bouton "Create an App"**

On obtient l'image suivante:

![image](https://github.com/Patheux/Spotipy/assets/70717709/3f2e7f6a-5132-427b-8852-aca856ef0db9)

il suffit de remplir les valeurs:
- App name: comme vous voulez
- App description: idem
- Website: idem
- Redirect URI: une URL auquelle vous pouvez vous connecter comme une page facebook, un site web,...
- cochez la case des Term's Services

### Récupération des Clés
Dans **Settings** récupérez le **Client ID** et le **Client Secret** ainsi que l'**URI** (le même que vous avez rentré


## Connexion
Entrez dans le fichier *spotipy.py* au niveau des Variables Globales:
- Le numéro utilisateur: Client ID
- Le numéro secret : Client Secret
- Une adresse url que vous avez choisi dans l'API Spotify: URI
- Le nom de l'utilisateur: par exemple JohnSmith

Exemple

```python
# Informations
client_id = 'ghjkl'                   					# Identifiant du client
client_secret = '1234'                					# Mot de Passe du client
redirect_uri = 'https://www.printables.com/'    # La même URL que celle rentrée dans L'API de Spotify
username = 'JohnSmith'                   			  # Nom d'utilisateur Spotify
```
