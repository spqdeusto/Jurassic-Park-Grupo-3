<template>
    <div class="newdino">
      <h1>NEW DINO</h1>
      <img alt="Vue logo" src="../assets/jurassicparklogo.png">
     
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

    
     <div>
     <p> {{ '\u00a0' }}</p>
      <p>Nombre: {{ message }}</p>
      <input type="message" id="name" name="name" placeholder="name" />
      </div>

      <div>
        <p>Seleccione un dinosaurio: {{ message }}</p>
        <select v-model="type">
          <option disabled value="">Seleccione</option>
          <option>Dilophosaurus</option>
          <option>T-Rex</option>
          <option>Velociraptor</option>
          <option>Brachiosaurus</option>
          <option>Parasaulophus</option>
          <option>Galliminus</option>
          <option>Triceratops</option>
      </select>
        <div v-if="type === 'Dilophosaurus'">     
        

        
         
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="type === 'T-Rex'">
         <div class="container">
          <img alt="Vue logo" src="../assets/trex.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="type === 'Velociraptor'">
         <div class="container">
          <img alt="Vue logo" src="../assets/velociraptor.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="type === 'Brachiosaurus'">
         



          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="type === 'Parasaulophus'">
          <div class="container">
          <img alt="Vue logo" src="../assets/para.jpg" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="type === 'Galliminus'">
         <div class="container">
          <img alt="Vue logo" src="../assets/galli.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="type === 'Triceratops'">
         <div class="container">
          <img alt="Vue logo" src="../assets/trice.jpg" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
      </div>
           
      <p>Edad: {{ message }}</p>
      <input type="number" id="age" name="age" placeholder="age" />

      <p>Peso: {{ message }}</p>
      <input type="number" id="weight" name="wieght" placeholder="weight" />

     <p>  </p>
       <label for="gender">Genero masculino:</label>
    <input type="checkbox"  id="gender" v-model="gender"><br>

       <label for="agressiveness">Agresividad:</label>
    <input type="checkbox"  id="agressiveness" v-model="agressiveness"><br>

        <div>
        <p>Seleccione el recinto correspondiente: {{ message }}</p>
        <select v-model="type">
          <option disabled value="">Seleccione</option>
          <option>Dilophosaurus</option>
          <option>T-Rex</option>
          <option>Velociraptor</option>
          <option>Brachiosaurus y Parasaulophus</option>
          <option>Galliminus</option>
          <option>Triceratops</option>
      </select>
      </div>

      
      <div>
      <button v-on:click="submit">Submit</button>
      </div>
  
</template>


<script>
import axios from 'axios';

export default {
  name: 'NewDino',
  data() {
    return {
      name: "",
      type: '',
      age: 0,
      weight: 0,
      gender: false,
      agressiveness: false,
      recinto: "",
    }
  },
  methods: {
    submit() {
      const body = { id: '-1', name: this.name, type: this.type, age: this.age, weight: this.weight, gender: this.gender, agressiveness: this.agressiveness, recinto: this.recinto};
      axios.post("/dinosaur/create", body)
      .then(response => {
        console.log(response);
        this.success = "Data saved successfully";
      })
      .catch(error => {
        console.log(error);
        this.response = "Error: " + error.response.status
      });
       alert("Dino creado correctamente!")
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

.container {
  width : 100 vw;
  height : 100 vh;
}

</style>

