from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import spotipy
from src.spotify_client import SpotifyClient
from src.insights import router as insights_router
from src.dashboard import router as dashboard_router
from config.redis_client import store_token_to_redis

app = FastAPI()

app.include_router(dashboard_router, prefix="/dashboards")
app.include_router(insights_router, prefix="/insights")

# Configura CORS para aceitar requisições do front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sp_oauth = SpotifyClient()

session_cache = {}

@app.get("/login")
async def login():
    return RedirectResponse(sp_oauth.get_authorize_url())

@app.get("/callback")
def callback(request: Request, code: str):
    code = request.query_params.get("code")
    token_info = sp_oauth.get_access_token(code)

    #Collect the token information
    access_token = token_info['access_token']
    expires_in = token_info['expires_in'] #information in seconds

    store_token_to_redis(access_token=access_token, expires_in=expires_in) 

    return RedirectResponse("http://localhost:3000/dashboard.html")


