<script>
  import Navbar from '../../component/Navbar.svelte'
  import Map from '../../component/Mainpage/Map.svelte'
  import { onMount } from 'svelte'
  import { browser } from '$app/environment'

  const mockStore = ['Central', 'Big C', 'Tesco Lotus', 'Makro', 'HomePro']
</script>

<Navbar />
<div class="relative">
  <div class="relative z-0">
    <Map />
  </div>
  <!-- search -->
  <div class="absolute top-0 left-1/2 right-1/2 z-10">
    <div class="flex flex-row justify-center my-6">
      <div>
        <input
          type="text"
          placeholder="Search Department"
          class="border border-gray-700 rounded-2xl px-4 py-1"
        />
      </div>
    </div>
  </div>
  <div class="mt-4 text-center font-bold">Nearby Department Store</div>
  {#each mockStore as store}
    <div>{store}</div>
  {/each}
</div>
