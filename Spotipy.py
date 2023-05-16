####################################
# Automatisation de Spotify
# Auteur: VIDON
# Cadre: Projet Personnel
####################################

## les modules
import spotipy
from spotipy.oauth2 import SpotifyOAuth

## Variables du Programme

# Informations
                ## cf le read-me
client_id = None # Identifiant du client
client_secret = None # Mot de Passe du client
redirect_uri = None # La même URL que celle rentrée dans L'API de Spotify
username= None # Nom d'utilisateur Spotify

# Verification Parameters
scope = 'playlist-modify-private user-modify-private user-read-private playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri=redirect_uri,
                                                    scope=scope))                
class Playlist():
    """Accès aux playlistes du compte Spotify de l'utilisateur"""

    def __init__(self):
        # Variables du programme
        pass

    def listerPlaylistCompte(self):
        """afficher les playlists du compte"""
        Liste=[]
        results=sp.current_user_playlists()
        while results:
            for playlist in results['items']:
                Liste.append([playlist['id'],playlist['name'],playlist['owner']['id'],playlist['public'],playlist['collaborative']])
            if results['next']:
                results=sp.next(results)
            else:
                results=None

        return Liste
class Musique():
    """Accès à la musique contenue dans une playlist"""
    def __init__(self):
        pass

    def Lire(self,playlist_id):
        """ Lecture du contenu d'une playlist """
        L=[]
        results = sp.playlist_items(playlist_id=playlist_id)
        while results:
            for track in results['items']:
                if 'track' in track and 'artists' in track['track']:
                    artists = [artist['name'] for artist in track['track']['artists']]
                    L.append([track['track']['name'], ', '.join(artists), track['track']['id'],track['track']['uri']])    
            if results['next']:
                results=sp.next(results)
            else:
                results=None
        return L
    
    def Supprimer(self,playlist_id,uri,position):
        """Fonction permettant de supprimer les chansons en doublons des playlists"""
        sp.user_playlist_remove_specific_occurrences_of_tracks(user='me', playlist_id=playlist_id,tracks=[{"uri":uri,"positions":[position]}])

    def Simplifier(self,playlist_id):
        """Fonction permettant de voir les doublons au sein des playlists"""
        doublons = []
        similaire = []
        
        playlist=Musique()
        Musiques=playlist.Lire(playlist_id)
    
        for i in range(len(Musiques)):
            for j in range(i+1,len(Musiques)):
                if (Musiques[i][0]==Musiques[j][0] and Musiques[i][1]==Musiques[j][1]) and i<j : # ici on fait le tri pour ne pas avoir 2 scans en doubles (on ressort un résultat unique)
                    if Musiques[i][3]==Musiques[j][3]:
                        Ens=[Musiques[j],(j)]
                        doublons.append(Ens)
                    else:
                        similaire.append([Musiques[i],Musiques[j]])
        return [doublons,similaire]
    
#################################
####        Programme        ####
#################################

## Variables initialisation
TotalMusique=[]
ListeDesPlaylists=[]
Comparaison=[]
Doublons=[]

## utilisation des classes

# Impression de toutes les playlistes du compte et stockage dans une liste
a=Playlist()
ListeDesPlaylists=a.listerPlaylistCompte()
# print(ListeDesPlaylists)

# Impressions de toutes les musiques du compte et stockage dans une liste
Musiques=Musique()

## Fonctions du Programme
def Deduplification_Playlists(ListeDesPlaylists:classmethod,Musiques:classmethod):
    """Fonction permettant de supprimer les doublons et retourner les musiques similaires dans une série de Playlistes données"""
    doublon=[]
    Doublons=[]
    
    for i in range(len(ListeDesPlaylists)):
        if ListeDesPlaylists[i][2]==username and (ListeDesPlaylists[i][3] and ListeDesPlaylists[i][4]) is False  :
            
            doublon=Musiques.Simplifier(ListeDesPlaylists[i][0])[0]
            for x in range(len(doublon)) :
                Musiques.Supprimer(ListeDesPlaylists[i][0],doublon[x][0][2],(doublon[x][1]-x))
            if doublon !=[]:
                Doublons.append([ListeDesPlaylists[i][1],"-",doublon])

    print ("Doublons déjà supprimés")
    print(Doublons)

    return Doublons

## Programme Brut

Musiques=Musique()
Deduplification_Playlists(ListeDesPlaylists,Musiques)
