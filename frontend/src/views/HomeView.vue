<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/jurassicparklogo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  <button onclick="window.location.href='/dinomenu'" style="float: center;width: 100px; height: 50px;" >Menu Dino</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: center;width: 100px; height: 50px;" >Menu Jeep</button>
    <button onclick="window.location.href='/recintomenu'" style="float: center;width: 100px; height: 50px;" >Menu Recinto</button>
</template>


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
</style>



