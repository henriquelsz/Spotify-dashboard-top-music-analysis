async function fetchTopTracks() {
    const response = await fetch("http://localhost:8000/top-tracks");
    const data = await response.json();

    if (data.error) {
        alert("Erro: " + data.error);
        window.location.href = "index.html";
        return;
    }

    const tableBody = document.querySelector("#top-tracks-table tbody");
    data.tracks.forEach(track => {
        const row = tableBody.insertRow();
        row.insertCell().innerText = track.name;
        row.insertCell().innerText = track.artists;
    });

    document.getElementById("top-tracks-graph").src = data.graph;
}

window.onload = fetchTopTracks;
