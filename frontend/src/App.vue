<template>
  <div id="app" style="margin: 0px; padding: 0px;">
    <Navbar/>
    <router-view></router-view>
    <footer>
      <p>&copy; Marcin Nahajowski Maciej Markiewicz 2021</p>
    </footer>
  </div>
</template>

<script>
import Navbar from './components/main/Navbar.vue';
export default {
  components: { Navbar },
  name: "App",
};
</script>

<style>

html,
body {
    font: 300 12px "Roboto";
    color: white;
    background-image: url("../img/dark_air_bg.jpg");
    background-position: left;
    
}

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

button {
  cursor: pointer;
}

footer {
  position: relative;
  background-color: #013d3c;
  height: 80px;
  width: 100%;
}

footer p {
  position: absolute;
  top: 50%;
  left: 20px;
  transform: translateY(-50%);
}


</style>
