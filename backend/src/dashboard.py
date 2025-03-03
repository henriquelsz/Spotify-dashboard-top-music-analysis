import matplotlib
matplotlib.use('Agg')  # Força modo "sem tela", apenas salvando imagem

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def gerar_dashboard(sp):
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
