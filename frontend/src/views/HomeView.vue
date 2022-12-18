<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/jurassicparklogo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  <div>
    <button onclick="window.location.href='/dinomenu'" style="float: center;width: 100px; height: 50px;" >Menu Dino</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: center;width: 100px; height: 50px;" >Menu Jeep</button>
    <button onclick="window.location.href='/recintomenu'" style="float: center;width: 100px; height: 50px;" >Menu Recinto</button>
  </div>
  <div>
    <h1 id="alerta">Nivel de Alerta: {{ status.alerta }}</h1>
  </div>
  <div>
    <h1>Recintos:</h1>
    <div id="table" v-for="recinto in status.recintos" :key="recinto.id">
      <table>
      <caption><h2>{{ recinto.name }}</h2></caption>
      <tr>
        <th>id</th>
        <th>name</th>
        <th>species</th>
        <th>age</th>
        <th>weigh</th>
        <th>gender</th>
        <th>dangerousness</th>
      </tr>
      <tr v-for="dinosaur in recinto.dinosaurs" :key="dinosaur.id">
        <td>{{ dinosaur.id }}</td>
        <td>{{ dinosaur.name }}</td>
        <td>{{ dinosaur.species }}</td>
        <td>{{ dinosaur.age }}</td>
        <td>{{ dinosaur.weigh }}</td>
        <td v-if="dinosaur.gender == true">male</td>
        <td v-else>female</td>
        <td>{{ dinosaur.dangerousness }}</td>
      </tr>
      </table>
      <div>
        <p v-if="recinto.state == true">Valla electrica: Activada</p>
        <p v-else>Valla electrica: Desactivada</p>
        <button v-if="recinto.state == true" v-on:click="desactivarElectricidad(recinto.id)">Desactivar</button>
        <button v-else v-on:click="activarElectricidad(recinto.id)">Activar</button>
      </div>
    </div>
  </div>
  <div>
    <h1>Jeeps:</h1>
    <div id="table">
      <table>
      <tr>
        <th>id</th>
        <th>ruta</th>
        <th>numvisitantes</th>
        <th>sistemaseguridad</th>
        <th>Estado</th>
      </tr>
      <tr v-for="jeep in status.jeeps" :key="jeep.id">
        <td>{{ jeep.id }}</td>
        <td>{{ jeep.ruta }}</td>
        <td>{{ jeep.numvisitantes }}</td>
        <td>{{ jeep.sistemaseguridad }}</td>
        <td>
          <button v-if="jeep.ruta == true" v-on:click="desactivarRuta(jeep.id)">Quitar de Ruta</button>
          <button v-else v-on:click="activarRuta(jeep.id)">Poner en Ruta</button>
        </td>
      </tr>
      </table>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      id: null,
      status: null
    }
  },
  methods: {

    desactivarRuta(id) {
      const body = {id: id};
      axios.post("/jeep/ruta/down", body)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
      alert("Jeep quitado de ruta!");
      this.getStatus();
    },

    activarRuta(id) {
      const body = {id: id};
      axios.post("/jeep/ruta/up", body)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
      alert("Jeep puesto en ruta!");
      this.getStatus();
    },

    activarElectricidad(id) {
      const body = {id: id};
      axios.post("/recinto/up", body)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
      alert("Valla electrica activada!");
      this.getStatus();
    },

    desactivarElectricidad(id) {
      const body = {id: id};
      axios.post("/recinto/down", body)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
      alert("Valla electrica desactivada!");
      this.getStatus();
    },

    getStatus() {
      axios.get('/').then((res) => {
        this.status = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  },
  created() {
    this.getStatus();
  }
}
</script>


<style>
  .home {
    background-image: url('../assets/jurassicpark.jpg');
    background-size: cover;
  }

  button{
    border-radius: 50%;
    border: none;
    font-weight: bold;
  }

  table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
  }

  td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }

  th {
    background-color: #b83030;
    color: white;
  }

  #table {
    padding-bottom: 50px;
  }

  caption {
    padding-bottom: 20px;
  }

  #alerta {
    color: yellow;
    background-color: #b83030;
  }
</style>



