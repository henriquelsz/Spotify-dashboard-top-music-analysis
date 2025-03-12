from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from .spotify_client import SpotifyClient
from spotipy.client import Spotify
from config.redis_client import get_token_from_redis

router = APIRouter()

@router.get("/track-insights/{track_id}")
def get_track_insights(track_id : str):
    token = get_token_from_redis()
    if not token:
        return JSONResponse({"error ": "User not authenticated"}, status_code=401)
    
    spotify = Spotify(auth=token)
    try:
        track_details = spotify.track(track_id)
        audio_features = spotify.audio_features(track_id)

        insights = {
            "name": track_details['name'],
            "artists": [artist['name'] for artist in track_details['artists']],
            "popularity": track_details['popularity'],
            "features": {
                "danceability": audio_features['danceability'],
                "energy": audio_features['energy'],
                "valence": audio_features['valence'],
                "loundness": audio_features['loundness'],
                "tempo": audio_features['tempo']
            },
            "spotify_url": track_details['external_urls']['spotify']
        }

        return insights

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/artist-insights/{artist_id}")
def get_artist_insights(artist_id : str):
    sportify = Spotify(token)
    try:
        artist = spotify.artist(artist_id)

        insights = {
            "name": artist['name'],
            "genres": artist['genres'],
            "popularity": artist['popularity'],
            "followers": artist['followers']['total'],
            "spotify_url": artist['external_urls']['spotify']
        }

        return insights
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))