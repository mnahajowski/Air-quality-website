<template>
  <div id="admin-page">
    <input v-model="login" placeholder="Login" />
    <input type="password" v-model="password" placeholder="Password" />
    <button v-on:click="loginUser"></button>
    <p>Błąd logowania</p>
  </div>
</template>

<script>
export default {
  name: "AdminPage",
  methods: {
    loginUser() {
      fetch("http://localhost:80/token", {
        method: "POST",
        body: JSON.stringify({ username: this.login, password: this.password }),
      }).then((data) => data.json())
      .then((data) => {
          console.log(data);
      });
    },
  },
  data() {
    return {
      login: null,
      password: null,
      token: null,
    };
  },
};
</script>

<style>
#admin-page {
  width: 100vw;
  height: calc(100vh - 80px);
  position: relative;
  background-color: white;
  padding-bottom: 80px;
  padding-top: 80px;
}

#admin-page p {
  display: none;
  color: red;
}
</style>
