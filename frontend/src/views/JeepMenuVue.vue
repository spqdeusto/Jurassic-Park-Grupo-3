<template>
  <div class="jeepmenu">
    <h1>JEEP MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

  <button onclick="window.location.href='/newjeep'" style="float: center;width: 100px; height: 50px;" >Nuevo Jeep</button>
  <h4>JEEPS disponibles en el parque:</h4>
  <ul>
    <li v-for="item in items" v-bind:key="item.id">
      
      <p>Ruta: {{ item.ruta }}</p>
      <p>Numvisitantes: {{ item.numvisitantes }}</p>
      <p>SistemaSeguridad: {{ item.sistemaseguridad }}</p>
    </li>
  </ul>
</template>
<script>
import axios from 'axios';

export default {
  name: 'ItemList',
  data() {
    return {
      items: []
    }
  },
  created() {
    axios.get('/jeeps')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  }
}
</script>

<style>
button {
  color: rgb(0, 21, 139)
}

</style>
