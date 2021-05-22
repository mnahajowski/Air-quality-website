<template>
  <div id="app" style="margin: 0px; padding: 0px;">
    <Navbar/>
    <router-view></router-view>
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
    /* background-color: #263838; */
    background-image: url("../img/background.jpg");
    
}

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}


</style>
