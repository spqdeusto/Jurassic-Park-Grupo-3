<template>
  <div class="jeepmenu">
    <h1>JEEP MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

  <button onclick="window.location.href='/newjeep'" style="float: center;width: 100px; height: 50px;" >Nuevo Jeep</button>
  <button onclick="window.location.href='/deleteJeep'" style="float: center;width: 100px; height: 50px;" >Borrar Jeep</button>
  <button onclick="window.location.href='/quitJeepRuta'" style="float: center;width: 100px; height: 50px;" >Quitar Ruta</button>
  <button onclick="window.location.href='/addJeepRuta'" style="float: center;width: 100px; height: 50px;" >Añadir Ruta</button>

</template>

<style>
button {
  color: rgb(2, 3, 12)
}
button:hover{
  font-weight:900;
}
.jeepmenu {
  background-image: url('../assets/jurassicpark.jpg');
  background-size: cover;
}


</style>
