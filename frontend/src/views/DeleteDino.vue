<template>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
  <button onclick="window.location.href='/dinomenu'" style="float: left;width: 100px; height: 50px;" >Menu Dino</button>
  <div>
      <h3>DINOSAURIOS:</h3>
      <div v-for="dino in dinos" :key="dino.id">
          <h4>Dinosaurio con id: {{ dino.id }}</h4>
          <p>name: {{ dino.name }}</p>
      </div>
    </div>
    <div>
      <select v-model="selected">
          <option v-for="dino in dinos" :key="dino.id">{{ dino.id }}</option>
      </select>
      <button v-on:click="quitDino">Quitar</button>
    </div>

</template>

<script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dinos: [],
        selected: null
      };
    },
    methods: {
      quitDino() {
  
        if(this.selected) {
            const body = { id: this.selected};
            axios.post("/dinosaur/delete", body)
                .then(function (response) {
                    console.log(response)
                })
                .catch(function (error) {
                    console.log(error)
                });
            this.getDinos();
        }
      },
      getDinos() {
            axios.get('/dinos').then((res) => {
              this.dinos = res.data;
            })
            .catch((error) => {
              console.error(error);
            });
      }
    },
    created() {
      this.getDinos();
    }
  };
  </script>