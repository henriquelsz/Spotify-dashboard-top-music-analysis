from fastapi import APIRouter, HTTPException
from spotify_client import SpotifyClient

router = APIRouter()

@router.get("/track-insights/{track_id}")
def get_track_insights(track_id : str):
    spotify = SpotifyClient()
    try:
        track_details = spotify.get_track_details(track_id)
        audio_features = spotify.get_audio_features(track_id)

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
    sportify = SpotifyClient()
    try:
        artist = spotify.get_artist_details(artist_id)

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