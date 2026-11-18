---
title: Contact / Visit
nav_order: 7
description: "How to find, visit, and contact the NC State Software Engineering group."
---

{% include badges.html %}

# <i class="fa-solid fa-location-dot"></i> Contact / Visit

## Find us

Lab 3228, Koch Hall, NC State
([map](https://www.google.com/maps/search/?api=1&query=Engineering+Building+II%2C+890+Oval+Dr%2C+Raleigh%2C+NC+27606)).

**Parking:** use the Partners Way deck, lower levels
([visitor rates](https://transportation.ncsu.edu/visitor-parking/)).
Then it is a short walk south to Koch Hall.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<div id="campus-map" style="height:420px; max-width:720px; border-radius:6px; margin:1rem 0;"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  var lab  = [35.77161, -78.67321];   // Koch Hall CS wing (was Engineering Building II), 890 Oval Dr
  var park = [35.77336, -78.67435];   // Partners Way Parking Deck entrance, on Partners Way
  var map = L.map('campus-map', { scrollWheelZoom: false });
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  var pin = function (color) {
    return L.divIcon({ className: '', iconSize: [22, 22], iconAnchor: [11, 11],
      html: '<div style="width:22px;height:22px;border-radius:50%;background:' + color +
            ';border:3px solid #fff;box-shadow:0 0 4px rgba(0,0,0,.5)"></div>' });
  };
  L.marker(lab, { icon: pin('#CC0000') }).addTo(map)
    .bindTooltip('<b>We are here.</b><br>CS dept. WiSER Lab.<br>3228 Koch Hall', { permanent: true, direction: 'right', offset: [12, 0] });
  L.marker(park, { icon: pin('#1a5fb4') }).addTo(map)
    .bindTooltip('<b>Visitor parking</b><br>Partners Way Deck', { permanent: true, direction: 'left', offset: [-12, 0] });
  L.polyline([park, lab], { color: '#555', weight: 3, dashArray: '6 6' }).addTo(map);
  map.fitBounds([lab, park], { padding: [80, 80] });
})();
</script>

## <i class="fa-solid fa-envelope"></i> Contact us

Email [timm@ieee.org](mailto:timm@ieee.org).

## <i class="fa-brands fa-github"></i> Typo? Idea?

[Report an issue](https://github.com/ncsu-software/ncsu-software.github.io/issues)
on GitHub.
