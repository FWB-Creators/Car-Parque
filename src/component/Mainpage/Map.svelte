<script>
  import 'leaflet/dist/leaflet.css'
  //   import L from 'leaflet'
  import { onMount } from 'svelte'
  import { browser } from '$app/environment'

  onMount(async () => {
    try {
      const L = await import('leaflet')
      if (browser && L) {
        console.log('browser')
        const map = L.map('map').setView([51.505, -0.09], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(
          map
        )
      }
    } catch (err) {
      console.log('error' + err)
    }
  })
</script>

<div id="map"></div>

<style>
  #map {
    height: 450px;
  }
</style>
