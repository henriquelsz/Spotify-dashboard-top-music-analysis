from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

class SpotifyClient:
    def __init__(self):
        #inicializando o client Spotify e mantendo atributo privado para encapsulamento
        self.__sp_oauth = SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="user-top-read" #permissao para retornar 20 musicas, artistas e generos mais escutados 
        )

    @property
    def sp_oauth(self):
        #Fornece acesso controlado ao atributo privado __sp_oauth
        return self.__sp_oauth
    
    #metodos publicos
    def get_top_tracks(self, time_range="medium_term"):
        results = self.__sp_oauth.current_user_top_tracks(limit=20, time_range=time_range)
        return results['items']
    def get_track_details(self, track_id):
        return self.__sp_oauth.track(track_id)
    def get_audio_features(self, track_id):
        return self.__sp_oauth.audio_features([track_id])[0]
    def get_artist_details(self, artist_id):
        return self.__sp_oauth.artist[artist_id]