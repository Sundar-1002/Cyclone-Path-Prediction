// Define the map object
var map = L.map('map').setView([0, 0], 2);

// Add the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
  maxZoom: 18
}).addTo(map);

// Define the coordinates array
var coordinates = [  [51.505, -0.09],
  [40.7128, -74.0060],
  [35.6895, 139.6917],
  [-33.859972, 151.211111]
];

// Add the markers to the map
coordinates.forEach(function(coord) {
  L.marker(coord).addTo(map);
});
