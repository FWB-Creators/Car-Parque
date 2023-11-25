<script>
  import { onMount, createEventDispatcher } from 'svelte'
  import { browser } from '$app/environment'

  export let newData = []
  const dispatch = createEventDispatcher()

  function haversineDistance(lat1, lon1, lat2, lon2) {
    // Radius of the Earth in kilometers
    const R = 6371

    // Convert latitude and longitude from degrees to radians
    const dLat = (lat2 - lat1) * (Math.PI / 180)
    const dLon = (lon2 - lon1) * (Math.PI / 180)

    // Calculate the Haversine distance
    const a =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(lat1 * (Math.PI / 180)) *
        Math.cos(lat2 * (Math.PI / 180)) *
        Math.sin(dLon / 2) *
        Math.sin(dLon / 2)

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

    const distance = R * c // Distance in kilometers

    return distance
  }

  onMount(async () => {
    try {
      const L = await import('leaflet')
      await import('leaflet/dist/leaflet.css')
      if (browser && L) {
        console.log('Leaflet library loaded successfully')

        const map = L.map('map').setView([0, 0], 13)
        console.log('Map initialized:', map)

        const dataMall = await fetch('Mall.json')
        const data = await dataMall.json()

        // Check if Geolocation is supported by the browser
        if ('geolocation' in navigator) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const { latitude, longitude } = position.coords
              console.log('Geolocation success:', latitude, longitude)

              map.setView([latitude, longitude], 13)

              // Add the tile layer outside the loop
              L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map)

              data.forEach((mall) => {
                const distance = Math.sqrt(
                  Math.pow(mall.Latitude - latitude, 2) +
                    Math.pow(mall.Longitude - longitude, 2)
                )
                const distanceInKm = haversineDistance(
                  mall.Latitude,
                  mall.Longitude,
                  latitude,
                  longitude
                )
                console.log(
                  'Adding marker for',
                  mall['Mall Location'],
                  'at',
                  mall.Latitude,
                  mall.Longitude
                )

                L.marker([mall.Latitude, mall.Longitude])
                  .addTo(map)
                  .bindPopup(mall['Mall Location'])
                  .openPopup()

                newData.push({
                  name: mall['Mall Location'],
                  distance: distance,
                  distanceInKm: distanceInKm,
                })
              })

              console.log('Markers added to the map:', newData)
              dispatch('sendData', { newData })
            },
            (error) => {
              console.error('Unable to retrieve your location', error)
            }
          )
        } else {
          console.error('Geolocation is not supported by your browser')
        }
      }
    } catch (err) {
      console.error('Error:', err)
    }
  })
</script>

<div id="map"></div>

<style>
  #map {
    height: 450px;
  }
</style>
