import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from matplotlib.backends.backend_pdf import PdfPages

def plot_top_tracks(tracks_data):
    df = pd.DataFrame(tracks_data)

    plt.figure(figsize=(12, 6))
    plt.barh(df['name'], df['popularity'], color='skyblue')
    plt.xlabel('Popularidade')
    plt.title('Top 20 Músicas - Popularidade')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def print_table(tracks_data):
    df = pd.DataFrame(tracks_data)
    print("\n📋 Tabela - Top 20 Músicas:\n")
    print(tabulate(df, headers='keys', tablefmt='grid'))

def save_to_csv(tracks_data, filename):
    df = pd.DataFrame(tracks_data)
    df.to_csv(filename, index=False)
    print(f"\n✅ Dados salvos em: {filename}")

def generate_pdf_report(tracks_data, filename):
    df = pd.DataFrame(tracks_data)

    with PdfPages(filename) as pdf:
        plt.figure(figsize=(12, 6))
        plt.barh(df['name'], df['popularity'], color='skyblue')
        plt.xlabel('Popularidade')
        plt.title('Top 20 Músicas - Popularidade')
        plt.gca().invert_yaxis()
        plt.tight_layout()

        pdf.savefig()
        plt.close()

        # Página 2: Tabela
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('tight')
        ax.axis('off')
        table_data = [["Música", "Artista", "Popularidade", "Duração (min)"]]
        for track in tracks_data:
            table_data.append([track['name'], track['artist'], track['popularity'], track['duration_min']])

        ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center', colWidths=[0.3, 0.3, 0.2, 0.2])
        ax.set_title('Top 20 Músicas - Detalhes')
        pdf.savefig()
        plt.close()

    print(f"\n✅ Relatório PDF salvo em: {filename}")
