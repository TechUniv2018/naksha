function onSubmit(points, lat, lng) {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: {
      lat: lat,
      lng: lng,
    },
  });
  console.log(map);
  const heatMapZoomFactor = 2.5;
  // console.log(points)
  const maxHeat = points.reduce((acc, p) => {
    return Math.max(acc, p.heat);
  }, 0)
  points.map(point => {
    const lat = parseFloat(point.lat);
    const lng = parseFloat(point.lng);
    const circle = new google.maps.Circle({
      strokeColor: '#000000',
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: '#ff0000',
      fillOpacity: 0.1,
      map: map,
      center: {
        lat,
        lng
      },
      radius: 1000,
    });
    circle.addListener('click', function () {
      // console.log(point.details.length)
      if (!point.markers) {
        point.markers = [];
        point.details.map(establishment => {
          // console.log(establishment.name,
          //   establishment.types);
          const marker = new google.maps.Marker({
            position: {
              lat: parseFloat(establishment.geometry.location.lat),
              lng: parseFloat(establishment.geometry.location.lng)
            },
            map: map,
            title: establishment.name,
          });
          marker.addListener('click', function () {
            marker.infoWindow = new google.maps.InfoWindow({
              content: establishment.name,
            });
            marker.infoWindow.open(map, marker);
          });
          point.markers.push(marker);
        });
        // console.log(point.advertisements)
        if (point.advertisements === undefined) {
          point.advertisements = [];
        }
        point.advertisements.map(advertisement => {
          // console.log(advertisement.lat, advertisement.lng)
          const marker = new google.maps.Marker({
            position: {
              lat: parseFloat(advertisement.lat),
              lng: parseFloat(advertisement.lng)
            },
            map: map,
            title: advertisement.name,
            icon: './img/beachflag.png'
          });
          marker.addListener('click', function () {
            marker.infoWindow = new google.maps.InfoWindow({
              content: `<h1>${advertisement.name}</h1>
                          <img width=300 src="${advertisement.img}" alt="house" />
                          <p>Price: ${advertisement.price} lakhs</p>
                          <p>${advertisement.bhk} BHK</p>`,
            });
            marker.infoWindow.open(map, marker);
          });
          point.markers.push(marker);
        });
      } else {
        point.markers.map(marker => {
          marker.setMap(null);
        })
        delete point.markers;
      }
    });
  });
  const allData = points.map(point => {
    return point.details.map(establishment => {
      return {
        location: new google.maps.LatLng(
          parseFloat(establishment.geometry.location.lat),
          parseFloat(establishment.geometry.location.lng)
        ),
        weight: point.heat / maxHeat,
        radius: map.getZoom() * heatMapZoomFactor,
      };
    });
  });
  const data = [].concat.apply([], allData)
  heatmap = new google.maps.visualization.HeatmapLayer({
    data,
    map,
  });
  // setTimeout(() => {
  //  heatmap = new google.maps.visualization.HeatmapLayer({
  //         data,
  //         map,
  //     });
  // }, 1000);

  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
  google.maps.event.addListener(map, 'zoom_changed', () => {
    const radius = map.getZoom() * heatMapZoomFactor;
    // console.log(radius)
    heatmap.setOptions({
      radius
    })
  })

}
