<script>
  import { createEventDispatcher } from 'svelte'
  export let data = []
  const dispatch = createEventDispatcher()
  console.log(data.length)
</script>

{#if data.length != 0}
  {#each data as item}
    {#if item == 1}
      <!-- <div class="rounded px-2 py-4 border border-black w-12 bg-red-200"></div> -->
      <img src="../car.png" alt="" width="55" class="mb-2" />
    {:else}
      <div
        class="rounded px-2 py-4 border border-black w-12 bg-green-200"
      ></div>
    {/if}
  {/each}
{/if}
