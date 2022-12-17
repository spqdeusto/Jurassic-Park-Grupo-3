<template>
    <div class="newjeep">
      <h1>JEEP</h1>
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: left;width: 100px; height: 50px;" >Menu Jeep</button>

 
    <label for="ruta">Ruta:</label>
    <input type="checkbox"  id="ruta" v-model="ruta"><br>
    <label for="numvisitantes">Numero de visitantes:</label>
    <input type="number" id="numvisitantes" v-model="numvisitantes" min="1" max="5"><br>
    <button v-on:click="submit">Submit</button>

  </template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      ruta: false,
      numvisitantes: 1,
    }
  },
  methods: {
    submit() {
      const body = { id: '-1', ruta: this.ruta, numvisitantes: this.numvisitantes, sistemaseguridad: false};
      axios.post("/todoterreno/create", body)
      .then(function (response) {
          console.log(response)
      })
      .catch(function (error) {
          console.log(error)
      });
      alert("Jeep creado correctamente!")
      this.ruta="";
      this.numvisitantes="";
      this
    }
  }
}
</script>
  
<style>
  #myForm {
    margin: auto;
    width: 50%;
  }
  button {
  color: rgb(5, 5, 5)
}
</style>