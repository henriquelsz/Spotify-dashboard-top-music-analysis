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
            scope="user-read-private user-top-read user-library-read" #permissao para retornar 20 musicas, artistas e generos mais escutados 
        )

    @property
    def sp_oauth(self):
        #Fornece acesso controlado ao atributo privado __sp_oauth
        return self.__sp_oauth
    
    #metodos publicos
    def get_authorize_url(self):
        return self.__sp_oauth.get_authorize_url()
    def get_access_token(self, code):
        return self.__sp_oauth.get_access_token(code)