<script>
    import Navbar from '../../component/Navbar.svelte'
</script>

<div class="flex flex-row justify-center"> 
    <img class=" h-20 w-20 rounded-lg  mt-11" src="image 6.svg" alt="">
</div>
<div class="font-bold text-[40px] text-center ">Login</div>
<div class="font-bold ml-7 mt-11">Email</div>
<input class="shadow appearance-none ml-7 mt-2 border rounded w-[22rem] py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="example@gmail.com">
<div class="font-bold ml-7 mt-7">Password</div>
<input type="password" class="shadow appearance-none ml-7 mt-2 border rounded w-[22rem] py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="****************">
<div class="text-black text-opacity-40 text-right mr-8 underline mt-1 hover:opacity-50 ">Forget Password?</div>
<div class="relative w-full">
    <input id="link-checkbox" type="checkbox" class=" absolute top-0 left-7 w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
    <label for="link-checkbox" class="absolute left-14 top-2 transform -translate-y-1/2">Remember me</label>
</div>
<div class="mt-16 flex justify-center">
    <button class=" bg-[#FF6F6F] hover:bg-opacity-50 text-white font-bold py-2 px-16 rounded ">
        LOGIN
      </button>
</div>
<div class="inline-flex items-center justify-center w-full">
    <hr class="w-64 h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
    <span class="absolute px-3  text-gray-900 -translate-x-1/2 bg-white left-1/2 dark:text-black font-bold">or</span>
</div>
<div class="font-bold text-center">Sign with</div>
<div class="mt-9 flex justify-center space-x-14">
    <div>
        <img class="object-scale-down  h-16 w-16 rounded-lg" src="\apple.png" alt="" height={200}>
    </div>
    <div>
        <img class="object-scale-down h-16 w-16 rounded-lg" src="\facebook.png" alt="">
    </div>
    <div>
        <img class="object-scale-down h-16 w-16 rounded-lg" src="\google.png" alt="">
    </div>
</div>
<div>
    <div class="text-black text-opacity-40 text-center mt-16">Need an account?</div>
    <div class="text-black text-opacity-40 text-center mt-1 underline hover:opacity-50 ">Register</div>
</div>