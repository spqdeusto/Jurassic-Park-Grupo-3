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
      axios.post('/todoterreno/create', {
        ruta: this.ruta,
        numvisitantes: this.numvisitantes,
        sistemaseguridad: this.sistemaseguridad
      })
      .then(response => {
        console.log(response);
        this.success = "Data saved successfully";
      })
      .catch(error => {
        console.log(error);
        this.response = "Error: " + error.response.status
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
  color: darkred
}
</style>