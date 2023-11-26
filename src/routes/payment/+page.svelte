<script>
  import Navbar from '../../component/Navbar.svelte'
</script>

<Navbar />
<div class="font-bold text-[40px] text-center mt-3">Payment</div>
<div class=" font-thin text-2xl text-left mt-8 ml-8">
  Choose Payment Methods
</div>
<div>
  <button
    class="flex flex-row rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="h-[100%] ml-5 flex justify-center items-center">
      <img class=" w-12" src="credit-card.png" alt="" />
    </div>
    <div class="h-[100%] flex text-xl ml-5 justify-center items-center">
      Credit / Debit Card
    </div>
  </button>
  <button
    class="flex flex-row rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="h-[100%] ml-5 flex justify-center items-center">
      <img class=" w-12" src="promptpay.png" alt="" />
    </div>
    <div class="h-[100%] flex text-xl ml-5 justify-center items-center">
      Prompt Pay
    </div>
  </button>
  <button
    class="flex flex-row rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="h-[100%] ml-5 flex justify-center items-center">
      <img class=" w-12" src="new-k-plus.png" alt="" />
    </div>
    <div class="h-[100%] flex text-xl ml-5 justify-center items-center">
      K Plus +
    </div>
  </button><button
    class="flex flex-row rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5 focus:shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
  >
    <div class="h-[100%] ml-5 flex justify-center items-center">
      <img class=" w-12" src="truewallet.png" alt="" />
    </div>
    <div class="h-[100%] flex text-xl ml-5 justify-center items-center">
      True Wallet
    </div>
  </button>

  <div
    class="flex flex-row rounded-lg text-center bg-black h-14 bg-opacity-25 mt-5 ml-5 mr-5"
  >
    <div class="flex flex-col text-xl mt-3 mb-3 ml-5 justify-center text-white">
      + &nbsp;&nbsp; Add New Payment
    </div>
  </div>

  <button
    class="flex flex-row rounded-lg border absolute bottom-[15px] bg-black h-14 w-[23.5rem] mt-5 ml-5 mr-5 focus:outline-none focus:ring focus:bg-opacity-80"
  >
    <div
      class="h-[100%] w-[100%] font-bold text-white flex items-center justify-center text-xl"
    >
      Continue
    </div>
  </button>
</div>

<!-- <div>
    <div class="font-bold text-2xl text-left mt-8 ml-8">
        Payment History
    </div>
    <div class="flex flex-row justify-center">
        <div class="flex flex-col rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5">
            <div class="flex flex-row justify-between">
                <div class="flex flex-row ml-5 mt-3">
                    <div class="flex flex-col">
                        <div class="text-xl font-bold">Credit / Debit Card</div>
                        <div class="text-xl font-bold">**** **** **** 1234</div>
                    </div>
                </div>
                <div class="flex flex-row mr-5 mt-3">
                    <div class="flex flex-col">
                        <div class="text-xl font-bold">฿ 100</div>
                        <div class="text-xl font-bold">12/12/2021</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="flex flex-row justify-center">
        <div class="flex flex-col rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5">
            <div class="flex flex-row justify-between">
                <div class="flex flex-row ml-5 mt-3">
                    <div class="flex flex-col">
                        <div class="text-xl font-bold">Credit / Debit Card</div>
                        <div class="text-xl font-bold">**** **** **** 1234</div>
                    </div>
                </div>
                <div class="flex flex-row mr-5 mt-3">
                    <div class="flex flex-col">
                        <div class="text-xl font-bold">฿ 100</div>
                        <div class="text-xl font-bold">12/12/2021</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="flex flex-row justify-center">
        <div class="flex flex-col rounded-lg border border-gray-700 h-20 w-[23.5rem] mt-5 ml-5 mr-5">
            <div class="flex flex-row justify-between">
            </div>
        </div>
    </div>
</div> -->
