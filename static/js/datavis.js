var dataMap;

function getUserLocation() {
  if (navigator.geolocation) {
    return navigator.geolocation.getCurrentPosition(function(a) {
      dataMap.panTo(new L.LatLng(a.coords.latitude, a.coords.longitude));
    });
  } else {
    return null;
  }
}

function mapInit() {

  var userLoc = getUserLocation();
  var mapCoords = [64.810, -18.245];

  if (userLoc) {
    mapCoords = [userLoc.latitude, userLoc.longitude];
  }

  dataMap = L.map('map-viewport').setView(mapCoords, 13);

  var baseLayer = new L.TileLayer(mapURL, {
    attribution: mapAttribution,
    maxZoom: 18,
  })

  dataMap.invalidateSize(false);
  dataMap.addLayer(baseLayer);
}


$(window).load(function() {
  mapInit();
  $('#loading-overlay').delay(1000).fadeOut(500);
});
