<template>
  <div id="map-selection">
    <h1>Sprawdź jakość powietrza w swojej okolicy</h1>
    <div class="section-wrapper">
      <section id="map-selection-instruction">
        <p class="center-absolute">
          Zaznacz na mapie region, dla którego chcesz wygenerować mapę jakości
          powietrza. Wybierz dodatkowe opcje, aby dokładniej zdefiniować liczbę
          segmentów, rodzaj mierzonego zanieczyszczenia oraz ramy czasowe w
          jakich przeprowadzane były pomiary.
        </p>
      </section>
      <section id="map-selection-map">
        <img
          class="map-image center-absolute"
          src="../../../img/wiatraki.jpg"
        />
        <div id="map-options-buttons">
          <button>Generuj</button>
          <button>Opcje</button>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "MapSelection",
  components: {},
};
</script>

<style>
#map-selection h1 {
  width: 100%;
  text-align: center;
  height: 80px;
  position: absolute;
  top: 30px;
  font-family: "Roboto Condensed";
  font-weight: 500;
  font-size: 40px;
}

#map-selection {
  margin: 0 auto;
  width: 75%;
  height: calc(100vh - 80px);
  position: relative;
  background-color: transparent;
}

.section-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

section {
  height: 100%;
  position: relative;
  width: 50%;
}

#map-selection-instruction {
  float: left;
}

#map-selection-instruction p {
  font-size: 18px;
  font-weight: bold;
  width: 75%;
  border: solid 1px black;
  text-align: center;
  padding: 75px;
  border-radius: 50px;
  background-color: white;
  color: black;
  box-shadow: 10px 5px 5px black;
}

#map-selection-map {
  float: right;
}

.center-absolute {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#map-options-buttons {
  position: absolute;
  bottom: 5%;
  width: 100%;
  text-align: center;
}

#map-options-buttons button {
  margin: 10px;
  border: solid 3px black;
  border-radius: 5px;
  background-color: white;
  font-weight: bold;
  font-size: 16px;
  width: 150px;
  height: 35px;
  box-shadow: 10px 5px 5px black;
}

.map-image {
  height: 450px;
  width: 450px;
  box-shadow: 10px 5px 5px black;
}
</style>
