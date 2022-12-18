<template>
    <div class="newdino">
      <h1>NEW DINO</h1>
      <img alt="Vue logo" src="../assets/jurassicparklogo.png">
     
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

    
     <div>
     <p> {{ '\u00a0' }}</p>
      <p>Nombre: {{ message }}</p>
      <input type="message" id="name" name="name" placeholder="name" v-model="name"/>
      </div>

      <div>
        <p>Seleccione un dinosaurio: {{ message }}</p>
        <select v-model="species">
          <option disabled value="">Seleccione</option>
          <option>Dilophosaurus</option>
          <option>T-Rex</option>
          <option>Velociraptor</option>
          <option>Brachiosaurus</option>
          <option>Parasaulophus</option>
          <option>Galliminus</option>
          <option>Triceratops</option>
      </select>
        <div v-if="species === 'Dilophosaurus'">     
        

        
         
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="species === 'T-Rex'">
         <div class="container">
          <img alt="Vue logo" src="../assets/trex.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="species === 'Velociraptor'">
         <div class="container">
          <img alt="Vue logo" src="../assets/velociraptor.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es peligroso.
        </div>
        <div v-if="species === 'Brachiosaurus'">
         



          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="species === 'Parasaulophus'">
          <div class="container">
          <img alt="Vue logo" src="../assets/para.jpg" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="species === 'Galliminus'">
         <div class="container">
          <img alt="Vue logo" src="../assets/galli.png" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
        <div v-if="species === 'Triceratops'">
         <div class="container">
          <img alt="Vue logo" src="../assets/trice.jpg" align="center" width="200" height="150">
          </div>
          El dinosaurio seleccionado es pacifico.
        </div>
      </div>
           
      <p>Edad: {{ message }}</p>
      <input type="number" id="age" name="age" placeholder="age" v-model="age"/>

      <p>Peso: {{ message }}</p>
      <input type="number" id="weight" name="wieght" placeholder="weight" v-model="weigh"/>

     <p>  </p>
       <label for="gender">Genero masculino:</label>
    <input type="checkbox"  id="gender" v-model="gender"><br>

       <label for="agressiveness">Agresividad:</label>
    <input type="checkbox"  id="agressiveness" v-model="dangerousness"><br>

      <div v-if="!recintos.length">
          <p>No es posible crear dinosaurios porque no hay recintos disponibles</p>
      </div>
      <div>
        <p>Seleccione el recinto correspondiente: {{ message }}</p>
        <select v-model="recinto">
          <option v-for="recinto_ in recintos" :key="recinto_.id">{{ recinto_.id }}</option>
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
      species: '',
      age: 0,
      weigh: 0,
      gender: false,
      dangerousness: false,
      recinto: null,
      recintos: []
    }
  },
  methods: {

    submit() {
      if(this.recinto) {
        const body = { id: '-1', name: this.name, species: this.species, age: this.age, weigh: this.weigh, gender: this.gender, dangerousness: this.dangerousness, recinto: Number(this.recinto)};
        console.log(body)
        axios.post("/dinosaur/create", body)
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
        alert("Dino creado correctamente!");
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

