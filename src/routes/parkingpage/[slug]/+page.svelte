<script>
  import Navbar from '../../../component/Navbar.svelte'
  import ParkSlot from '../../../component/Parkingpage/ParkSlot.svelte'
  import ParkSlotMiddle from '../../../component/Parkingpage/ParkSlotMiddle.svelte'
  import { localStorageStore } from '../../../localStorageStore.js'
  // import { sharedData } from '../../store.js'
  // sharedData.subscribe((value) => {
  //   console.log(value)
  // })
  const value = localStorageStore.getItem('name')
  console.log('test', value)
  const fetchData = async () => {
    const response = await fetch('mockData.json')
    const data = await response.json()
    // const data = data.filter((item) => item.name === value)
    return data
  }
</script>

<Navbar />
<div class="relative">
  <div class="absolute left-4">
    <ParkSlot />
  </div>
  <div class="absolute left-36">
    <ParkSlotMiddle />
  </div>
  <div class="absolute right-36">
    <ParkSlotMiddle />
  </div>
  <div class="absolute right-4">
    <ParkSlot />
  </div>
</div>
