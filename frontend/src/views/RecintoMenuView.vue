<template>
  <div class="recintomenu">
    <h1>RECINTO MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
  <div>
    <h2>A continuacion se muestran los recintos del parque:</h2>
    <div v-for="recinto in recintos" :key="recinto.id">
        <h2>TodoTerreno con id: {{ recinto.id }}</h2>
        <p>id: {{ recinto.id }}</p>
        <p>status: {{ recinto.status }}</p>
    </div>
  </div>
  <div>
    <button onclick="window.location.href='/recintoup'" style="float: center;width: 150px; height: 70px;" >Encender sistema eléctrico</button>
    <button onclick="window.location.href='/recintodown'" style="float: center;width: 150px; height: 70px;" >Apagar sistema eléctrico</button>
  </div>
  
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      recintos: [],
    };
  },
  methods: {
    getRecintos() {
          axios.get('/recintos').then((res) => {
            this.recintos = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    }
  },
  created() {
    this.getRecintos();
  }
};
</script>