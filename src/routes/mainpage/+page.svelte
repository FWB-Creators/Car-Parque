<script>
  import Navbar from '../../component/Navbar.svelte'
  import Map from '../../component/Mainpage/Map.svelte'
  import { onMount, createEventDispatcher } from 'svelte'
  import { browser } from '$app/environment'
  let loading = true
  let passingDataLoading = true
  let newData = []
  let mockStore = [
    { name: 'Central', status: '' },
    { name: 'Big C', status: '' },
    { name: 'Tesco Lotus', status: '' },
    { name: 'Makro', status: '' },
    { name: 'HomePro', status: '' },
    { name: 'Robinson', status: '' },
    { name: 'Mega Bangna', status: '' },
    { name: 'Mega Bangyai', status: '' },
  ]

  const mockStatus = ['Moderate', 'High', 'Low']

  const randomStatus = () => {
    return mockStatus[Math.floor(Math.random() * mockStatus.length)]
  }

  let tempData
  const handlePassingData = (event) => {
    tempData = event.detail.newData
    tempData = tempData.sort((a, b) => a.distanceInKm - b.distanceInKm)
    console.log(tempData)
    passingDataLoading = false
  }

  let isReady = false

  onMount(async () => {
    mockStore.forEach((store) => {
      store.status = randomStatus()
    })
    // const dataMall = await fetch('Mall.json')
    // const data = await dataMall.json()
    // data.forEach((mall) => {
    //   const distance = Math.sqrt(
    //     Math.pow(mall.Latitude, 2) + Math.pow(mall.Longitude, 2)
    //   )
    //   console.log('root', distance)
    // })
    loading = false // Set isReady to true after generating random statuses
  })

  // Use reactive statement to trigger rendering after statuses are ready
</script>

<Navbar />
<div class="relative h-[calc(screen-4rem)] overflow-hidden">
  <div class="relative z-0">
    <Map bind:newData on:sendData={handlePassingData} />
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
  {#if loading == false}
    <div class="mt-6 mb-2 text-center font-bold text-lg">
      Nearby Department Store
    </div>

    <div class="h-64 overflow-scroll">
      {#if passingDataLoading == false}
        {#each tempData as { name, distanceInKm }}
          <div class="relative flex flex-row border-b-2 mx-4 py-3">
            <img src="location_icon.png" width="20" />
            <div class="ml-2 font-medium">{name}</div>
            <div class="absolute right-2">
              {distanceInKm.toFixed(2)} km
            </div>
            <!-- {#if distance === 'Moderate'}
              <div class="absolute right-2 text-yellow-500">{distance}</div>
            {:else if distance === 'High'}
              <div class="absolute right-2 text-red-500">{distance}</div>
            {:else if distance === 'Low'}
              <div class="absolute right-2 text-green-500">{distance}</div>
            {/if} -->
          </div>
        {/each}
      {/if}
    </div>
  {:else}
    <div class="flex justify-center items-center h-fit">
      <div
        class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-gray-900"
      ></div>
    </div>
  {/if}
</div>
