<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/jurassicparklogo.png">
    <HelloWorld msg="Welcome to DINO"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
