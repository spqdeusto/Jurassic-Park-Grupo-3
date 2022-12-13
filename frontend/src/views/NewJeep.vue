<template>
    <div class="newjeep">
      <h1>JEEP</h1>
    </div>
    <button onclick="window.location.href='/'" style="float: left;width: 100px; height: 50px;" >Inicio</button>
    <button onclick="window.location.href='/jeepmenu'" style="float: left;width: 100px; height: 50px;" >Menu Jeep</button>

    <form id="myForm">
        <label for="ruta">Ruta:</label>
        <input type="checkbox"  id="ruta" name="ruta"><br>
        <label for="numvisitantes">Numero de visitantes:</label>
        <input type="number" id="numvisitantes" name="numvisitantes" min="1"><br>
        <label for="sisseg">Sistema de seguridad:</label>
        <input type="checkbox" id="sisseg" name="sisseg"><br><br>
        <input type="submit" value="Submit">
    </form>

  </template>
  
<style>
  #myForm {
    margin: auto;
    width: 50%;
  }
</style>