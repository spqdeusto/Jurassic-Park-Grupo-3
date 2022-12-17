<template>
  <div class="recintomenu">
    <h1>RECINTO MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
  <button onclick="window.location.href='/recintoup'" style="float: center;width: 100px; height: 50px;" >Encender sistema eléctrico</button>
  <button onclick="window.location.href='/recintoup'" style="float: center;width: 100px; height: 50px;" >Encender sistema eléctrico</button>
    <div>
      <h1>A continuacion se muestran los jeeps en ruta:</h1>
      <div v-for="recinto in recintos" :key="recinto.id">
          <h2>TodoTerreno con id: {{ recinto.id }}</h2>
          <p>id: {{ recinto.id }}</p>
          <p>status: {{ recinto.status }}</p>
      </div>
    </div>
    <div>
      <select v-model="selected">
          <option v-for="recinto in recintos" :key="recinto.id">{{ recinto.id }}</option>
      </select>
      <button v-on:click="upRecinto">Encender</button>
      <button v-on:click="quitRecinto">Apagar</button>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        recintos: [],
        selected: null
      };
    },
    methods: {
      quitRecinto() {
  
        if(this.selected) {
            const body = { id: this.selected};
            axios.post("/recinto/down", body)
                .then(function (response) {
                    console.log(response)
                })
                .catch(function (error) {
                    console.log(error)
                });
            this.getRecintos();
        }
      },
      upRecinto() {
  
        if(this.selected) {
            const body = { id: this.selected};
            axios.post("/recinto/up", body)
                .then(function (response) {
                    console.log(response)
                })
                .catch(function (error) {
                    console.log(error)
                });
            this.getRecintos();
        }
      },
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