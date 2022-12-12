<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/jurassicparklogo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
      <nav>
    <router-link to="/dinomenu">DINO</router-link> |
    <router-link to="/jeepmenu">JEEP</router-link> |
    <router-link to="/recintomenu">RECINTO</router-link> |
    </nav>

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
