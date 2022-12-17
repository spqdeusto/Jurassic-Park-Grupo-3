<template>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: left;width: 100px; height: 50px;" >Menu Jeep</button>
      <div>
        <h3>A continuacion se muestran los jeeps que no estan en ruta:</h3>
        <div v-for="todoTerreno in todoTerrenos" :key="todoTerreno.id">
            <h4>TodoTerreno con id: {{ todoTerreno.id }}</h4>
            <p>id: {{ todoTerreno.id }}</p>
            <p>ruta: {{ todoTerreno.ruta }}</p>
            <p>numero de visitantes: {{ todoTerreno.numvisitantes }}</p>
        </div>
      </div>
      <div>
        <select v-model="selected">
            <option v-for="todoTerreno in todoTerrenos" :key="todoTerreno.id">{{ todoTerreno.id }}</option>
        </select>
        <button v-on:click="addJeepRuta">Añadir</button>
      </div>
    </template>
    
    <script>
    
    import axios from 'axios';
    
    export default {
      data() {
        return {
          todoTerrenos: [],
          selected: null
        };
      },
      methods: {
        addJeepRuta() {
    
          if(this.selected) {
              const body = { id: this.selected};
              axios.post("/jeep/ruta/up", body)
                  .then(function (response) {
                      console.log(response)
                  })
                  .catch(function (error) {
                      console.log(error)
                  });
              this.getTodoterrenos();
          }
        },
        getTodoterrenos() {
              axios.get('/jeepsNoRuta').then((res) => {
                this.todoTerrenos = res.data;
              })
              .catch((error) => {
                console.error(error);
              });
        }
      },
      created() {
        this.getTodoterrenos();
      }
    };
    </script>