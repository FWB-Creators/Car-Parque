<script>
import Navbar from '../../component/Navbar.svelte'
let show =false
const toggle = () => {
show = !show
console.log(show)
}
</script>
<Navbar />
<div class="flex flex-row justify-center overflow-hidden"> 
    <img class="rounded-b-lg" src="Paragon.jpg" alt="">
</div>
<div class="font-bold text-[40px] text-center ">Paragon</div>   

<!-- <div class="bg-gray-400 p-2 grid grid-cols-2">
    <div class="inline-block ">One</div>
    <div class="inline-block ">Two</div>
  </div> -->
  <div class="overflow-scroll">
    <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
        <div class="ml-2 text-lg font-bold">Floor</div>
        <div class=" text-lg font-bold right-2">Slots</div>
    </div>
    <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">1st</div>
        <div class=" font-bold right-2">23</div>
    </div>
    <div class="grid grid-cols-2 bg-gray-100 text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">2nd</div>
        <div class=" font-bold right-2">5</div>
    </div>
    <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">3rd</div>
        <div class=" font-bold right-2">12</div>
    </div>
    <div class="grid grid-cols-2 bg-gray-100  text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">4th</div>
        <div class=" font-bold right-2">7</div>
    </div>
    <div class="grid grid-cols-2 text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">5th</div>
        <div class=" font-bold right-2">32</div>
    </div>
    <div class="grid grid-cols-2 bg-gray-100  text-center border-b-2 mx-4 py-3">
        <div class="ml-2 font-bold">6th</div>
        <div class=" text-red-700 font-bold right-2">Full</div>
    </div>
  </div>
  


  <div class="max-w-screen mt-3">
    <div class="">
        <!-- Accordion Header -->
        <div on:click = {toggle} class="p-2 border-2 rounded text-black flex flex-row flow-root cursor-pointer mr-3 ml-3">
            <h2 class="text-lg font-semibold overflow-auto float-left mr-3 ml-3 ">Description</h2>
            <svg data-accordion-icon class="w-3 h-3 rotate-180 mt-2 float-right mr-3" aria-hidden="true"  fill="none" viewBox="0 0 10 6">
                <path class= "float-right right-7" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
              </svg>
        </div>
        <div class="{show == true ? '' : 'hidden'} p-4 bg-white mr-3 ml-3 border-l-2 border-r-2 border-b-2 overflow-y-scroll scroll-smooth">
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
                <p class="font-bold mt-3">Social Media:</p>
                <div class="flex flex-row ">
                    <div class="flex flex-row mr-3">
                        <img class="h-6 w-6" src="facebook.png" alt="">
                    </div>
                    <div class="flex flex-row mr-3">
                        <img class="h-6 w-6" src="instagram.png" alt="">
                    </div>
                    <div class="flex flex-row mr-3">
                        <img class="h-6 w-6" src="twitter.png" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>