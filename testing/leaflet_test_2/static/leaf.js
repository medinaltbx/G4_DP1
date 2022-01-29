var map = L.map('map').setView([41.66, -4.72],
    14);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);

L.control.scale().addTo(map);
// L.marker([41.66, -4.71], {draggable: true}).addTo(map);
var source = new EventSource('/topic/generator');
source.addEventListener('message', function (e) {
    console.log('LLEGA EVENTO:')
    // marker = L.marker([39.46975, -0.37739]).addTo(mymap)
    obj = JSON.parse(e.data);
    let markers = [];
    for (var key in obj) {
        aux = obj[key]
        console.log(aux);
    }
    // lat = aux["position"]["lat"];
    // long = aux["position"]["lon"];
    // // username = obj["name"];
    // // marker = L.marker([lat,long],).addTo(mymap).bindPopup('Username: <strong>' + username + '</strong>');
    // marker = L.marker([lat,long],).addTo(mymap)


}, false);

// var source = new EventSource('/topic/generator');
// source.addEventListener('message', function (e) {
//     console.log('LLEGA EVENTO:')
//     obj = JSON.parse(e.data);
//     for (var key in obj) {
//         aux = obj[key]
//         console.log(aux);
//     }
// }, false);