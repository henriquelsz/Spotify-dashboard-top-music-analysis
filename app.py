import argparse
from spotify_client import get_spotify_client
from data_processing import parse_top_tracks
from visualizer import plot_top_tracks, print_table, save_to_csv, generate_pdf_report

def main():
    parser = argparse.ArgumentParser(description="Gera relatório das músicas mais ouvidas no Spotify")
    parser.add_argument('--time_range', choices=['short_term', 'medium_term', 'long_term'], default='medium_term',
                        help="Período de análise (short_term = 4 semanas, medium_term = 6 meses, long_term = histórico completo)")

    args = parser.parse_args()

    sp = get_spotify_client()

    top_tracks = sp.current_user_top_tracks(limit=20, time_range=args.time_range)
    tracks_data = parse_top_tracks(top_tracks)

    print(f"\n🎶 Analisando seu histórico do Spotify ({args.time_range})...\n")

    print_table(tracks_data)
    save_to_csv(tracks_data, f'top_tracks_{args.time_range}.csv')
    plot_top_tracks(tracks_data)
    generate_pdf_report(tracks_data, f'top_tracks_report_{args.time_range}.pdf')

if __name__ == "__main__":
    main()
