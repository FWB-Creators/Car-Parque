<script>
  import Navbar from '../../../component/Navbar.svelte'
  import { onMount } from 'svelte'
  import { localStorageStore } from '../../../localStorageStore.js'

  let imgUrl = localStorageStore.getItem('name')
  imgUrl = '../' + imgUrl + '.png'
  console.log('img ', imgUrl)
  let isDataLoaded = false
  let show = false
  let avaliable = 0
  let parkSlot = []
  let results = []
  const value = localStorageStore.getItem('name')
  console.log(value)

  onMount(async () => {
    const fetchData = async () => {
      const response = await fetch('../mockData.json')
      const data = await response.json()
      //filter with object
      const newdata = data[value][1]
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

    const promises = []
    for (let i = 1; i <= 3; i++) {
      promises.push(eachFloor(i))
    }

    results = await Promise.all(promises)
    console.log(results)
  })

  const toggle = () => {
    show = !show
    console.log(show)
  }

  const eachFloor = async (floor) => {
    let freeSlot = 0
    const response = await fetch('../mockData.json')
    const data = await response.json()
    const newdata = data[value][floor]
    console.log(newdata)
    for (let i = 1; i <= Object.values(newdata).length; i++) {
      if (newdata[i] == true) {
        freeSlot++
      }
    }
    return freeSlot
  }

  const sendDataToPage = (floor) => {
    localStorageStore.setItem('floor', floor)
  }
</script>

<Navbar />
<div class="flex flex-row justify-center overflow-hidden">
  <div class="max-h-60">
    <img class="rounded-b-lg" src={imgUrl} alt="" />
  </div>
</div>
<div class="mt-6 font-bold text-[36px] text-center">{value}</div>

<!-- <div class="bg-gray-400 p-2 grid grid-cols-2">
    <div class="inline-block ">One</div>
    <div class="inline-block ">Two</div>
  </div> -->
<div class="overflow-scroll">
  <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
    <div class="ml-2 text-lg font-bold">Floor</div>
    <div class=" text-lg font-bold right-2">Avaliable Slots</div>
  </div>
  <a
    class="grid grid-cols-2 text-center border-b-2 mx-4 py-3"
    href="/parkingpage/{value}"
    on:click={() => sendDataToPage(1)}
  >
    <div class="ml-2 font-bold">1st</div>
    <div class=" font-bold right-2">{results[0]}</div>
  </a>
  <a
    class="grid grid-cols-2 bg-gray-100 text-center border-b-2 mx-4 py-3"
    href="/parkingpage/{value}"
    on:click={() => sendDataToPage(2)}
  >
    <div class="ml-2 font-bold">2nd</div>
    <div class=" font-bold right-2">{results[1]}</div>
  </a>
  <a
    class="grid grid-cols-2 text-center border-b-2 mx-4 py-3"
    href="/parkingpage/{value}"
    on:click={() => sendDataToPage(3)}
  >
    <div class="ml-2 font-bold">3rd</div>
    <div class=" font-bold right-2">{results[2]}</div>
  </a>
  <!-- <div class="grid grid-cols-2 bg-gray-100 text-center border-b-2 mx-4 py-3">
    <div class="ml-2 font-bold">4th</div>
    <div class=" font-bold right-2">7</div>
  </div>
  <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
    <div class="ml-2 font-bold">5th</div>
    <div class=" font-bold right-2">32</div>
  </div>
  <div class="grid grid-cols-2 bg-gray-100 text-center border-b-2 mx-4 py-3">
    <div class="ml-2 font-bold">6th</div>
    <div class=" text-red-700 font-bold right-2">Full</div>
  </div> -->
</div>

<div class="max-w-screen mt-3">
  <div class="">
    <!-- Accordion Header -->
    <div
      on:click={toggle}
      class="p-2 border-2 rounded text-black flex flex-row flow-root cursor-pointer mr-3 ml-3"
    >
      <h2 class="text-lg font-semibold overflow-auto float-left mr-3 ml-3">
        Description
      </h2>
      <svg
        data-accordion-icon
        class="w-3 h-3 rotate-180 mt-2 float-right mr-3"
        aria-hidden="true"
        fill="none"
        viewBox="0 0 10 6"
      >
        <path
          class="float-right right-7"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M9 5 5 1 1 5"
        />
      </svg>
    </div>
    <div
      class="{show == true
        ? ''
        : 'hidden'} p-4 bg-white mr-3 ml-3 border-l-2 border-r-2 border-b-2 overflow-y-scroll scroll-smooth"
    >
      <div class="grid grid-cols-2 gap-4 overflow-auto">
        <div>
          <p class="font-bold">Open:</p>
          <p>10:00 - 22:00</p>
        </div>
        <div>
          <p class="font-bold">Tel:</p>
          <p>+66 2 610 8000</p>
        </div>
      </div>
      <div>
        <p class="font-bold mt-3">Contact & Social Media:</p>
        <div class="flex flex-row mt-2">
          <div class="flex flex-row mr-3">
            <img class="h-6 w-6" src="../facebook.png" alt="" />
          </div>
          <div class="flex flex-row mr-3">
            <img class="h-6 w-6" src="../instagram.png" alt="" />
          </div>
          <div class="flex flex-row mr-3">
            <img class="h-6 w-6" src="../twitter.png" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
