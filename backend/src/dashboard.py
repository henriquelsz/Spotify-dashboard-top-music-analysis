import matplotlib
matplotlib.use('Agg')  # Força modo "sem tela", apenas salvando imagem

import spotipy
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
from config.redis_client import get_token_from_redis
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

router = APIRouter()

@router.get("/top-tracks")
async def top_tracks(request: Request):
    token_info = get_token_from_redis()
    if not token_info:
        return JSONResponse({"error ": "User not authenticated"}, status_code=401)

    sp = spotipy.Spotify(auth=token_info)
    df, graph = await gen_dashboard(sp)

    return JSONResponse({
        "tracks": df.to_dict(orient="records"),
        "graph": graph
    })

async def gen_dashboard(sp):
    top_tracks = sp.current_user_top_tracks(limit=20)

    tracks = []
    for item in top_tracks['items']:
        tracks.append({
            "name": item['name'],
            "artists": ', '.join(artist['name'] for artist in item['artists']),
            "popularity": item['popularity']
        })

    df = pd.DataFrame(tracks)

    plt.figure(figsize=(10, 5))
    plt.barh(df['name'], df['popularity'], color='skyblue')
    plt.xlabel("Popularidade")
    plt.ylabel("Música")
    plt.gca().invert_yaxis()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    graph_base64 = "data:image/png;base64," + base64.b64encode(buf.read()).decode("utf-8")

    return df, graph_base64
