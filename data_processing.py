def parse_top_tracks(top_tracks):
    data = []
    for track in top_tracks['items']:
        data.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'duration_min': round(track['duration_ms'] / 60000, 2)
        })
    return data
