<template>
  <div id="admin-page">
    <div class="login-form">
      <input v-model="login" placeholder="Login"/>
      <input type="password" v-model="password" placeholder="Hasło" />
      <button v-on:click="loginUser">Zaloguj</button>
      <p>Błąd logowania</p>
    </div>
    <div class="admin-func">
      <p class="admin-info"> Zmień konfigurację kolorów na mapie dla danego poziomu zanieczyszczeń<br/>(1 - najniższy poziom/najwyższa jakoś powietrza)</p>
      <div class="input-group">
        <label>Wybierz poziom:</label>
        <input v-model="colorLevel" type="number" placeholder="Wybierz poziom" min="1" max="5" @change="updateColors"/>
      </div>
      <div class="input-group">
        <label>R:</label>
        <input v-model="r" type="number" placeholder="R" min="0" max="255" @change="updatePreview"/>
        <label>G:</label>
        <input v-model="g" type="number" placeholder="G" min="0" max="255" @change="updatePreview"/>
        <label>B:</label>
        <input v-model="b" type="number" placeholder="B" min="0" max="255" @change="updatePreview"/>
      </div>
      <div class="color-preview">
      </div>
      <button v-on:click="changeColor">Zatwierdź</button>
      <p id="confirm-info">Zatwierdzono zmianę</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminPage",
  methods: {
    changeColor() {
      var options = {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${this.token}`
        },
        method: "POST",
        body: JSON.stringify({[`level${this.colorLevel}`]: [this.r, this.g, this.b]}),
      };
      fetch("http://localhost:80/admin/config", options)
        .then((data) => {
          if (data.ok) {
            this.colorConfigs[this.colorLevel] = [this.r, this.g, this.b];
            document.querySelector("#confirm-info").style.display = "block";
            document.querySelector("#confirm-info").style.color = "green";
            document.querySelector("#confirm-info").textContent = "Zatwierdzono zmianę";
          } else {
            document.querySelector("#confirm-info").style.display = "block";
            document.querySelector("#confirm-info").style.color = "red";
            document.querySelector("#confirm-info").textContent = "Za małe uprawnienia";
          }
        });
    },
    updateColors() {
      document.querySelector("#confirm-info").style.display = "none";
      this.r = this.colorConfigs[this.colorLevel][0];
      this.g = this.colorConfigs[this.colorLevel][1];
      this.b = this.colorConfigs[this.colorLevel][2];
      this.updatePreview()
    },
    updatePreview() {
      document.querySelector(".color-preview").style.backgroundColor = `rgb(${this.r}, ${this.g}, ${this.b})`;
    },
    loginUser() {
      var options = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        method: "POST",
        body: `username=${this.login}&password=${this.password}`,
      };
      fetch("http://localhost:80/token", options)
        .then((data) => {
          if (data.ok) {
            return data.json();
          } else {
            document.querySelector("p").style.display = "block";
          }
        })
        .then((data) => {
          if (data && data.access_token != undefined) {
            this.token = data.access_token;
            document.querySelector(".login-form").style.display = "none";
            document.querySelector(".admin-func").style.display = "block";
          } else {
            document.querySelector("p").style.display = "block";
          }
        });
    },
  },
  data() {
    return {
      login: null,
      password: null,
      token: null,
      colorLevel: 1,
      r: null,
      g: null,
      b: null,
      colorConfigs: null
    };
  },
  mounted() {
    fetch("http://localhost:80/admin/config")
    .then(data => data.json())
    .then(data => {
      this.colorConfigs = data.config;
      this.updateColors();
    });

  }
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

.login-form p {
  display: none;
  color: red;
  font-size: 16px;
}

.admin-info {
  color: black;
  margin-bottom: 50px;
  
}

.admin-func button {
  margin: 0px auto;
}

.login-form, .admin-func {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 20px;
}

#admin-page button {
  background-color: #013d3c;
  color: white;
  display: block;
  padding: 10px;
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 10px;
}

#admin-page input {
  font-size: 22px;
  margin-bottom: 10px;
  
}

.login-form input{
  display: block;
}

.admin-func input {
  margin-right: 20px;
}

.admin-func {
  display: none;
  color:black;
  text-align: center;
}

.color-preview {
  background-color: white;
  height: 100px;
  width: 50%;
  margin: 0px auto 10px;
}

#admin-page label {
  font-size: 22px;
  color:black;
  margin-right: 5px;
}

#confirm-info {
  display: none;
  color: green;
  font-size: 16px;
}
</style>
