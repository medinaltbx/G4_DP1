var mymap = L.map('mapid').setView([39.46975, -0.37739], 12);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoibWVkaW5hem9yaW4iLCJhIjoiY2t5enBybWZjMTRubjJvbXhqcWtsNm1oYSJ9.48K1ovzCYJzrDxPkHzZicQ'
}).addTo(mymap);

var source = new EventSource('/topic/raw_data');

source.addEventListener('message', function(e){
    obj = JSON.parse(e.data);
    console.log(obj);
    lat = obj.place.bounding_box.coordinates[0][0][1];
    long = obj.place.bounding_box.coordinates[0][0][0];
    username = obj.name;
    tweet = obj.text;

    marker = L.marker([lat,long],).addTo(mymap).bindPopup('Username: <strong>' + username + '</strong><br>Tweet: <strong>' + tweet + '</strong>');

}, false);