---
title: Contact / Visit
nav_order: 1
description: "How to find, visit, and contact the NC State Software Engineering group."
parent: Home
---

{% include badges.html %}

# <i class="fa-solid fa-location-dot" aria-hidden="true"></i> Contact / Visit

## Find us

CS dept. WiSER Lab. Room 3228, Koch Hall, NC State.

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
  // 4.1.2: Leaflet gives every marker role=button, so the name rides inside the
  // icon's own html (Leaflet rebuilds the outer element, and it does not exist
  // at all until the map has a view)
  var pin = function (color, name) {
    return L.divIcon({ className: '', iconSize: [22, 22], iconAnchor: [11, 11],
      html: '<div style="width:22px;height:22px;border-radius:50%;background:' + color +
            ';border:3px solid #fff;box-shadow:0 0 4px rgba(0,0,0,.5)"></div>' +
            '<span class="sr-only">' + name + '</span>' });
  };
  L.marker(lab, { icon: pin('#CC0000', 'WiSER Lab, 3228 Koch Hall') }).addTo(map)
    .bindTooltip('<b>We are here.</b><br>CS dept. WiSER Lab.<br>3228 Koch Hall', { permanent: true, direction: 'right', offset: [12, 0] });
  L.marker(park, { icon: pin('#4156A1', 'Visitor parking, Partners Way Deck') }).addTo(map)
    .bindTooltip('<b>Visitor parking</b><br>Partners Way Deck', { permanent: true, direction: 'left', offset: [-12, 0] });
  // walking route: west of Golden LEAF, round the Oval Dr circle, in the entrance
  // by the Engineering II bus stop, then inside to the lab
  var door = [35.77206, -78.67363];
  var walk = [park, [35.77263, -78.67455], [35.77241, -78.67380], [35.77226, -78.67380],
              door, lab];
  L.polyline(walk, { color: '#000', weight: 3, dashArray: '6 6' }).addTo(map);
  map.fitBounds([lab, park], { padding: [80, 80] });
})();
</script>

## <i class="fa-solid fa-envelope" aria-hidden="true"></i> Contact us

Email [timm@ieee.org](mailto:timm@ieee.org).
