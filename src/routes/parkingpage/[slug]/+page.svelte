<script>
  import { onMount } from 'svelte'
  import Navbar from '../../../component/Navbar.svelte'
  import ParkSlot from '../../../component/Parkingpage/ParkSlot.svelte'
  import ParkSlotMiddle from '../../../component/Parkingpage/ParkSlotMiddle.svelte'
  import { localStorageStore } from '../../../localStorageStore.js'

  const parkSlot = []
  const value = localStorageStore.getItem('name')
  const floor = localStorageStore.getItem('floor')
  console.log('test', value)
  let avaliable = 0
  let isDataLoaded = false

  onMount(() => {
    const fetchData = async () => {
      const response = await fetch('../mockData.json')
      const data = await response.json()
      //filter with object
      const newdata = data[value][floor]
      console.log(newdata)
      for (let i = 1; i <= Object.values(newdata).length; i++) {
        if (newdata[i] == true) {
          avaliable++
        }
        parkSlot.push(newdata[i])
      }
      console.log(parkSlot)
      isDataLoaded = true
    }

    fetchData()
  })
</script>

<Navbar />
{#if isDataLoaded}
  <div class="block">
    <div>
      <div class="font-bold text-xl text-center mb-6">{value}</div>
      <div class="relative h-[26rem]">
        <div class="absolute left-4">
          <ParkSlot data={parkSlot.slice(0, 11)} />
        </div>

        <div class="absolute left-32">
          <ParkSlotMiddle data={parkSlot.slice(12, 23)} />
        </div>
        <div class="absolute right-32">
          <ParkSlotMiddle data={parkSlot.slice(24, 35)} />
        </div>
        <div class="absolute right-4">
          <ParkSlot data={parkSlot.slice(36, 47)} />
        </div>
      </div>
    </div>
  </div>
{/if}
<div class="relative mx-4 h-24 rounded bg-black text-white">
  <div class="absolute left-4 top-4 text-xl font-bold">Floor</div>
  <div class="absolute left-4 top-12 text-xl font-bold">{floor}</div>
  <div class="absolute right-4 top-4 text-xl font-bold">Avaliable Slot</div>
  <div class="absolute right-4 top-12 text-xl font-bold">{avaliable}</div>
</div>
<div class="mt-8 text-center">Last Updated: 10 mins ago.</div>
