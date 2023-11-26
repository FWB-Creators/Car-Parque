<script>
  import Navbar from '../../component/Navbar.svelte'
  import { localStorageStore } from '../../localStorageStore.js'

  const name = localStorageStore.getItem('name')
  const floor = localStorageStore.getItem('floor')
  const start_time = localStorageStore.getItem('start_time')
  const end_time = localStorageStore.getItem('end_time')
  const date = localStorageStore.getItem('date')
</script>

<Navbar />
<div class="font-bold text-[30px] text-center mt-3">Review Summary</div>
<div class="flex flex-col rounded-lg border border-gray-300 mt-3 p-3 m-2 m">
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class=" text-lg text-left font-medium text-black text-opacity-60">
      Parking Area :
    </div>
    <div class=" text-lg font-medium text-right right-2">{name}</div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class="text-lg text-left font-medium text-black text-opacity-60">
      Vehicle :
    </div>
    <div class=" text-lg font-medium text-right right-2">
      Toyota Altis (อน 3324)
    </div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class="text-lg text-left font-medium text-black text-opacity-60">
      Parking Spot :
    </div>
    <div class=" text-lg font-medium text-right right-2">A05</div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class="text-lg text-left font-medium text-black text-opacity-60">
      Date :
    </div>
    <div class=" text-lg font-medium text-right right-2">{date}</div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class="text-lg text-left font-medium text-black text-opacity-60">
      Duration :
    </div>
    <div class=" text-lg font-medium text-right right-2">2 Hours</div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class="text-lg text-left font-medium text-black text-opacity-60">
      Hours :
    </div>
    <div class=" text-lg font-medium text-right right-2">
      {start_time} - {end_time} Hours
    </div>
  </div>
</div>

<div class="flex flex-col rounded-lg border border-gray-300 mt-6 p-3 m-2 m">
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class=" text-lg text-left font-medium text-black text-opacity-60">
      Amount :
    </div>
    <div class=" text-lg font-medium text-right right-2">฿ 60.00</div>
  </div>
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class=" text-lg text-left font-medium text-black text-opacity-60">
      Discount :
    </div>
    <div class=" text-lg font-medium text-right right-2">฿ 0.00</div>
  </div>
  <hr class="h-px bg-gray-300 border-0" />
  <div class="grid grid-cols-2 py-3 p-1 w-[100%]">
    <div class=" text-lg text-left font-medium text-black text-opacity-60">
      Total :
    </div>
    <div class=" text-lg font-medium text-right right-2">฿ 60.00</div>
  </div>
</div>
<div class="relative">
  <div class="m-3 flex flex-v">
    <input
      class="px-2 shadow appearance-none border rounded w-[24.5rem] placeholder:pl-3 py-2 h-[40px] text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      placeholder="Enter Coupon Code"
    />
  </div>
  <div class="absolute top-0 right-0 mr-3 grid justify-items-end h-[40px]">
    <button
      class=" bg-gray-700 text-white px-3 py-1 rounded hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-500"
      >Enter</button
    >
  </div>
</div>

<div class="flex flex-col rounded-lg border border-gray-300 p-3 m-2 mt-6">
  <div class="flex w-full">
    <div class="flex">
      <img class="h-12 w-12 ml-2" src="visa.png" alt="" />
      <div
        class="ml-5 mt-3 text-lg font-medium text-black flex- text-opacity-60"
      >
        **** **** **** 4679
      </div>
    </div>
    <div class="flex-1 flex items-center justify-end">
      <a href="/payment">
        <button
          class="mr-4 font-semibold text-gray-800 underline focus:outline-none focus:text-gray-500"
        >
          Change
        </button>
      </a>
    </div>
  </div>
</div>
<div class="relative mt-3 w-full">
  <input
    id="link-checkbox"
    type="checkbox"
    class=" absolute top-0 left-7 w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-2"
  />
  <label
    for="link-checkbox"
    class="absolute left-14 top-2 transform -translate-y-1/2"
    >I'm aware of Terms and Conditions</label
  >
</div>
<div class="flex flex-col rounded-lg border bg-gray-800 p-3 m-2 mt-16">
  <button
    disabled={true}
    class={`font-bold ${true && 'active'} bg-white-100 text-white`}
    >Confrim</button
  >
  <!-- <button disabled={true} class="font-bold text-white">Confrim</button> -->
</div>
