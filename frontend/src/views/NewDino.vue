<template>
    <div class="newdino">
      <h1>NEW DINO</h1>
      <img alt="Vue logo" src="../assets/jurassicparklogo.png">
     
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
    <button onclick="window.location.href='/newdino'" style="float: center;width: 100px; height: 50px;" >Nuevo Dino</button>    


      <div>
      <p> "" </p>
      <button v-on:click="submitForm">Submit</button>
      </div>
        <form id="myForm">
        <label for="name">Nombre:</label>
        <input type="text"  id="name" name="name"><br>
        <label for="type">Tipo:</label>
        <input type="text"  id="type" name="type"><br>
        <label for="age">Edad:</label>
        <input type="number" id="age" name="age" min="1" max="200"><br>
        <label for="weight">Peso:</label>
        <input type="number" id="weight" name="weight" min="1" max="2000"><br>
        <label for="gender">Genero marcado = Masculino:</label>
        <input type="checkbox" id="gender" name="gender"><br>
        <label for="agressiveness">Marcado = agresivo:</label>
        <input type="checkbox" id="agressiveness" name="agressiveness"><br><br>
        <button v-on:click="submitForm">Submit</button>
    </form>
</template>


<script>
import axios from 'axios';

export default {
  name: 'NewDino',
  data() {
    return {
      name: "",
      type: "",
      age: 0,
      weight: 0,
      gender: false,
      agressiveness: false,
    }
  },
  methods: {
    submitForm() {
      axios.post('/dinosaur/create', {
        name: this.name,
        type: this.type,
        age: this.age,
        weight: this.weight,
        gender: this.gender,
        agressiveness: this.agressiveness,
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
  color: rgb(68, 88, 198)
}
 button:hover {
    font-weight: 900;
  }
.newdino {
  background-image: url('../assets/jurassicpark.jpg');
  background-size: cover;
}

</style>

