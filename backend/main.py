from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from src.dashboard import gerar_dashboard

app = FastAPI()

# Configura CORS para aceitar requisições do front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-top-read"
)

session_cache = {}

@app.get("/login")
def login():
    return RedirectResponse(sp_oauth.get_authorize_url())

@app.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    token_info = sp_oauth.get_access_token(code)
    session_cache["token_info"] = token_info
    return RedirectResponse("http://localhost:3000/dashboard.html")

@app.get("/top-tracks")
def top_tracks():
    token_info = session_cache.get("token_info")
    if not token_info:
        return JSONResponse({"error": "Usuário não autenticado"}, status_code=401)

    sp = spotipy.Spotify(auth=token_info['access_token'])
    df, graph = gerar_dashboard(sp)

    return JSONResponse({
        "tracks": df.to_dict(orient="records"),
        "graph": graph
    })
