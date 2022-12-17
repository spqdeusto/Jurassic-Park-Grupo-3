<template>
  <div class="recintomenu">
    <h1>RECINTO MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
  
    <div>
      <h3>A continuacion se muestran los recintos apagados:</h3>
      <div v-for="recinto in recintos" :key="recinto.id">
          <h4>TodoTerreno con id: {{ recinto.id }}</h4>
          <p>id: {{ recinto.id }}</p>
          <p>status: {{ recinto.status }}</p>
      </div>
    </div>
    <div>
      <select v-model="selected">
          <option v-for="recinto in recintos" :key="recinto.id">{{ recinto.id }}</option>
      </select>
      <button v-on:click="upRecinto">Encender</button>
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
      upRecinto() {
  
        if(this.selected) {
            const body = { id: this.selected};
            axios.post("/recintosApagados", body)
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