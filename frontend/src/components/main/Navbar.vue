<template>
  <div>
  <nav>
    <router-link to="/" class="router-image-logo"><img src="../../../img/air-transmission.svg" class="logo-image"></router-link>
    <router-link to="/"><a>Strona główna</a></router-link>
    <router-link to="/charts"><a>Stacje pomiarowe</a></router-link>
  </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style>

nav {
  margin: 0px;
  width: 100%;
  height: 80px;
  position: fixed;
  background-color: #013d3c;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  z-index: 5;
}

nav a {
  width: auto;
  padding: 10px;
  text-align: center;
  font: 500 24px "Roboto";
  color: white;
  text-decoration: none;
}

.logo-image {
  height: 50px;
  width: 50px;
  padding: 0px;
}

.router-image-logo {
  margin-right: auto;
  padding: 15px;
}

</style>
