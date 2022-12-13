<template>
  <div class="jeepmenu">
    <h1>JEEP MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

  <button onclick="window.location.href='/newjeep'" style="float: center;width: 100px; height: 50px;" >Nuevo Jeep</button>

  
<!-- Este es el formulario donde se mostrará el input de opciones -->
<form>
  <label for="options">Seleccione el jeep que desea quitar de la ruta:</label>
  <select id="options">
    <option v-for="option in options" :key="option.id" :value="option.value">{{ option.id }}</option>
  </select>
  <button v-on:click="submitForm">Quitar</button>
</form>

</template>
<script>
import axios from 'axios';

export default {
  name: 'ItemList',
  data() {
    return {
      options: []
    }
  },
  methods:{
    mounted() {
      axios
        .get('/jeepsRuta')
        .then(response => (this.options = response.data))
    },
    submitForm() {
      
      axios.post('/jeep/ruta/down', {
        //no sabia donde poner el id que le pasa al metodo de quitRuta       
        id: this.option.id
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
button {
  color: rgb(0, 21, 139)
}

</style>
