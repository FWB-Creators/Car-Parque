<script>
  import Navbar from '../../component/Navbar.svelte'
  import { localStorageStore } from '../../localStorageStore.js'
  const selectValue1 = (e) => {
    localStorageStore.setItem('date', e.target.value)

    console.log('select')
  }

  const selectValue2 = (e) => {
    localStorageStore.setItem('start_time', e.target.value)

    console.log('select')
  }
  const selectValue3 = (e) => {
    localStorageStore.setItem('end_time', e.target.value)

    console.log('select')
  }
</script>

<Navbar />
<div class="font-bold text-[36px] text-center mt-3">Reservation</div>
<div class=" flex flex-col justify-center items-center">
  <button
    class="  border-2 rounded mt-2 w-[50%] h-20 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="flex items-center justify-center h-[100%] text-xl font-bold">
      A01
    </div>
  </button>
  <button
    class="  border-2 rounded mt-2 w-[50%] h-20 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="flex items-center justify-center h-[100%] text-xl font-bold">
      A02
    </div>
  </button>
  <button
    class="  border-2 rounded mt-2 w-[50%] h-20 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="flex items-center justify-center h-[100%] text-xl font-bold">
      A03
    </div>
  </button>
  <button
    class="  border-2 rounded mt-2 w-[50%] h-20 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="flex items-center justify-center h-[100%] text-xl font-bold">
      A04
    </div>
  </button>
  <button
    class="  border-2 rounded mt-2 w-[50%] h-20 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="flex items-center justify-center h-[100%] text-xl font-bold">
      A05
    </div>
  </button>
</div>

<div class="mt-10 text-[20px] font-bold ml-6 mb-3">Date & Time Selection</div>
<div class="flex flex-row justify-center">
  <div
    class="grid grid-cols-3 divide-x border-2 rounded border-gray-400 w-full mx-6 mb-10 py-3"
  >
    <div class="text-center">
      <select on:change={selectValue1}>
        <option value="26 Nov 2023">26 Nov 2023</option>
        <option value="27 Nov 2023">27 Nov 2023</option>
        <option value="28 Nov 2023">28 Nov 2023</option>
        <option value="29 Nov 2023">29 Nov 2023</option>
        <option value="30 Nov 2023">30 Nov 2023</option>
      </select>
    </div>
    <div class="text-center">
      <select on:change={selectValue2}>
        <option value="00:00">00:00 AM</option>
        <option value="00:30">00:30 AM</option>
        <option value="01:00">01:00 AM</option>
        <option value="01:30">01:30 AM</option>
        <option value="02:00">02:00 AM</option>

        <option value="02:30">02:30 AM</option>
        <option value="03:00">03:00 AM</option>
        <option value="03:30">03:30 AM</option>
        <option value="04:00">04:00 AM</option>
        <option value="04:30">04:30 AM</option>

        <option value="05:00">05:00 AM</option>

        <option value="05:30">05:30 AM</option>
        <option value="06:00">06:00 AM</option>
        <option value="06:30">06:30 AM</option>
        <option value="07:00">07:00 AM</option>
        <option value="07:30">07:30 AM</option>

        <option value="08:00">08:00 AM</option>
        <option value="08:30">08:30 AM</option>
        <option value="09:00">09:00 AM</option>
        <option value="09:30">09:30 AM</option>
        <option value="10:00">10:00 AM</option>

        <option value="10:30">10:30 AM</option>
        <option value="11:00">11:00 AM</option>
        <option value="11:30">11:30 AM</option>

        <option value="12:00">12:00 PM</option>
        <option value="12:30">12:30 PM</option>
        <option value="13:00">13:00 PM</option>
        <option value="13:30">13:30 PM</option>
        <option value="14:00">14:00 PM</option>

        <option value="14:30">14:30 PM</option>
        <option value="15:00">15:00 PM</option>
        <option value="15:30">15:30 PM</option>
        <option value="16:00">16:00 PM</option>
        <option value="16:30">16:30 PM</option>

        <option value="17:00">17:00 PM</option>
        <option value="17:30">17:30 PM</option>

        <option value="18:00">18:00 PM</option>
        <option value="18:30">18:30 PM</option>
        <option value="19:00">19:00 PM</option>
        <option value="19:30">19:30 PM</option>

        <option value="20:00">20:00 PM</option>
        <option value="20:30">20:30 PM</option>
        <option value="21:00">21:00 PM</option>
        <option value="21:30">21:30 PM</option>

        <option value="22:00">22:00 PM</option>
      </select>
    </div>
    <div class="text-center">
      <select on:change={selectValue3}>
        <option value="00:00">00:00 AM</option>
        <option value="00:30">00:30 AM</option>
        <option value="01:00">01:00 AM</option>
        <option value="01:30">01:30 AM</option>
        <option value="02:00">02:00 AM</option>

        <option value="02:30">02:30 AM</option>
        <option value="03:00">03:00 AM</option>
        <option value="03:30">03:30 AM</option>
        <option value="04:00">04:00 AM</option>
        <option value="04:30">04:30 AM</option>

        <option value="05:00">05:00 AM</option>

        <option value="05:30">05:30 AM</option>
        <option value="06:00">06:00 AM</option>
        <option value="06:30">06:30 AM</option>
        <option value="07:00">07:00 AM</option>
        <option value="07:30">07:30 AM</option>

        <option value="08:00">08:00 AM</option>
        <option value="08:30">08:30 AM</option>
        <option value="09:00">09:00 AM</option>
        <option value="09:30">09:30 AM</option>
        <option value="10:00">10:00 AM</option>

        <option value="10:30">10:30 AM</option>
        <option value="11:00">11:00 AM</option>
        <option value="11:30">11:30 AM</option>

        <option value="12:00">12:00 PM</option>
        <option value="12:30">12:30 PM</option>
        <option value="13:00">13:00 PM</option>
        <option value="13:30">13:30 PM</option>
        <option value="14:00">14:00 PM</option>

        <option value="14:30">14:30 PM</option>
        <option value="15:00">15:00 PM</option>
        <option value="15:30">15:30 PM</option>
        <option value="16:00">16:00 PM</option>
        <option value="16:30">16:30 PM</option>

        <option value="17:00">17:00 PM</option>
        <option value="17:30">17:30 PM</option>

        <option value="18:00">18:00 PM</option>
        <option value="18:30">18:30 PM</option>
        <option value="19:00">19:00 PM</option>
        <option value="19:30">19:30 PM</option>

        <option value="20:00">20:00 PM</option>
        <option value="20:30">20:30 PM</option>
        <option value="21:00">21:00 PM</option>
        <option value="21:30">21:30 PM</option>

        <option value="22:00">22:00 PM</option>
      </select>
    </div>
  </div>
</div>
<div class="flex justify-center items-center">
  <a href="/payment">
    <button
      class=" bg-black hover:bg-opacity-50 text-white font-bold py-2 px-16 rounded focus:outline-none focus:ring focus:bg-opacity-80"
    >
      Continue
    </button>
  </a>
</div>
