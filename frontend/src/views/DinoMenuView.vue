<template>
  <div class="dinomenu">
    <h1>DINO MENU</h1>
  </div>
  <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>

  <button onclick="window.location.href='/newdino'" style="float: center;width: 100px; height: 50px;" >Nuevo Dino</button>

  <button onclick="window.location.href='/deleteDino'" style="float: center;width: 100px; height: 50px;" >Delete Dino</button>
    
</template>

<style>
button {
  color: rgb(68, 88, 198)
}
 button:hover {
    font-weight: 900;
  }
.dinomenu {
  background-image: url('../assets/jurassicpark.jpg');
  background-size: cover;
}

</style>
