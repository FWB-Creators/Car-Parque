<script>
  import Navbar from '../../component/Navbar.svelte'
  import Loading from '../../component/Loading.svelte'
  import { sharedData } from '../store.js'

  let dataToSend = 'Hello from homepage'

  function sendData() {
    sharedData.set(dataToSend)
    // console.log(sharedData)
  }
</script>

<button on:click={sendData}>Send Data</button>
<Navbar />
<Loading />
