function test() {
    var map = L.map('map').setView([39.46975, -0.37739], 13);
    mapLink =
        '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; ' + mapLink + ' Contributors',
        maxZoom: 18,
    }).addTo(map);
    let planes = [["name", 39.46975, -0.37739], ["name", 39.56974, -0.37739]]
    for (var i = 0; i < planes.length; i++) {
        marker = new L.marker([planes[i][1], planes[i][2]])
            .bindPopup(planes[i][0])
            .addTo(map);
    }
    var source = new EventSource('/topic/generator');
    source.addEventListener('message', function (e) {
        console.log('LLEGA EVENTO:')
        obj = JSON.parse(e.data);
        for (var key in obj) {
            aux = obj[key]
            console.log(aux);
        }
    }, false);
}