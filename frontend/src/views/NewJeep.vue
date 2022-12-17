<template>
    <div class="newjeep">
      <h1>JEEP</h1>
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: left;width: 100px; height: 50px;" >Menu Jeep</button>

    <form id="myForm">
        <label for="ruta">Ruta:</label>
        <input type="checkbox"  id="ruta" name="ruta"><br>
        <label for="numvisitantes">Numero de visitantes:</label>
        <input type="number" id="numvisitantes" name="numvisitantes" min="1" max="5"><br>
        <label for="sistemaseguridad">Sistema de seguridad:</label>
        <input type="checkbox" id="sistemaseguridad" name="sistemaseguridad"><br><br>
        <button v-on:click="submitForm">Submit</button>
    </form>

  </template>

<script>
import axios from 'axios';

export default {
  name: 'NewJeepForm',
  data() {
    return {
      ruta: false,
      numvisitantes: 0,
      sistemaseguridad: false
    }
  },
  methods: {
    submitForm() {
      const body = { ruta: this.ruta, numvisitantes: this.numvisitantes, sistemaseguridad: this.sistemaseguridad};
      axios.post("/todoterreno/create", body)
      .then(function (response) {
                    console.log(response)
                })
                .catch(function (error) {
                    console.log(error)
                });
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