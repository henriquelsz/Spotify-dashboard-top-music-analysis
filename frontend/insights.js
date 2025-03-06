document.addEventListener("DOMContentLoaded", function() {
    const params = new URLSearchParams(window.location.search);
    const trackId = params.get("track_id");
    const artistId = params.get("artist_id");
    const contentDiv = document.getElementById("content");

    if (trackId) {
        fetch(`/insights/track-insights/${trackId}`)
            .then(response => response.json())
            .then(data => renderTrackInsights(data))
            .catch(err => contentDiv.innerText = `Erro ao buscar insights da música: ${err}`);
    } else if (artistId) {
        fetch(`/insights/artist-insights/${artistId}`)
            .then(response => response.json())
            .then(data => renderArtistInsights(data))
            .catch(err => contentDiv.innerText = `Erro ao buscar insights do artista: ${err}`);
    } else {
        contentDiv.innerText = "Nenhum ID informado.";
    }
});

function renderTrackInsights(data) {
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = `
        <h2>${data.name}</h2>
        <p><strong>Artistas:</strong> ${data.artists.join(", ")}</p>
        <p><strong>Popularidade:</strong> ${data.popularity}</p>
        <p><a href="${data.spotify_url}" target="_blank">Ouvir no Spotify</a></p>

        <h3>Características Sonoras</h3>
        <ul>
            <li><strong>Dançabilidade:</strong> ${data.features.danceability}</li>
            <li><strong>Energia:</strong> ${data.features.energy}</li>
            <li><strong>Valência:</strong> ${data.features.valence}</li>
            <li><strong>Loudness:</strong> ${data.features.loudness}</li>
            <li><strong>Tempo:</strong> ${data.features.tempo} BPM</li>
        </ul>
    `;
}

function renderArtistInsights(data) {
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = `
        <h2>${data.name}</h2>
        <p><strong>Gêneros:</strong> ${data.genres.join(", ")}</p>
        <p><strong>Popularidade:</strong> ${data.popularity}</p>
        <p><strong>Seguidores:</strong> ${data.followers}</p>
        <p><a href="${data.spotify_url}" target="_blank">Ver no Spotify</a></p>
    `;
}
