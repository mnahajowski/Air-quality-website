<template>
  <div>
    <div id="map-selection">
      <h1>Sprawdź jakość powietrza w swojej okolicy</h1>
      <div class="section-wrapper">
        <section id="map-selection-instruction">
          <p class="center-absolute">
            Zaznacz na mapie region, dla którego chcesz wygenerować mapę jakości
            powietrza. Wybierz dodatkowe opcje, aby dokładniej zdefiniować
            liczbę segmentów, rodzaj mierzonego zanieczyszczenia oraz ramy
            czasowe w jakich przeprowadzane były pomiary.
          </p>
        </section>
        <section id="map-selection-map">
          <Map
            class="map-image center-absolute"
            @lat-lon-coordinates="registerCords"
          />
          <div id="map-options-buttons">
            <button v-on:click="fetchMap" id="generate-button" disabled=true>Generuj</button>
            <button v-on:click="openOptionsModal">Opcje</button>
          </div>
        </section>
      </div>
    </div>

    <MapDetails @details-data="registerMapDetails"/>

    <div id="generated-map">
      <img class="generated-map-img"/>
      <img class="placeholder-img"/>
      <p class="placeholder-img">Wygeneruj mapę</p>
    </div>
  </div>
</template>

<script>
import Map from "@/components/main/Map.vue";
import MapDetails from "@/components/main/MapDetails.vue"

export default {
  name: "MapSelection",
  components: {
    Map,
    MapDetails
  },
  data() {
    return {
      latLon: [],
      param: "pm25",
      time: "latest",
      segments: "8",
    };
  },
  methods: {
    openOptionsModal() {
      document.getElementById("map-details").style.display = "initial";
    },

    registerCords(cords) {
      document.getElementById("generate-button").disabled = false;
      document.getElementById("generate-button").style.cursor = "pointer";
      this.latLon = cords[0];
    },

    registerMapDetails(details) {
      this.param = details.param;
      this.time = details.time;
      this.segments = details.segments;
    },

    fetchMap() {
      var rect = `${this.latLon[0].lat},${this.latLon[0].lng},${this.latLon[2].lat},${this.latLon[2].lng}`;
      
      if (this.time == undefined)
        this.time = 'latest';

      var datetime = this.time.replace(" ", "T");
      document.querySelector("img.placeholder-img").style.display = "none";
      document.querySelector("p.placeholder-img").style.display = "none";
      document.querySelector(
        ".generated-map-img"
      ).src = `http://localhost:80/map/?&rect=${rect}&param=${this.param}&segments_x=${this.segments}&width=1600&date=${datetime}`;
      document.getElementById("generated-map").scrollIntoView({behavior: 'smooth', block: "start"});
    },
  },
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

#map-selection section {
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

#generated-map {
  width: 100%;
  min-height: calc(100vh - 160px);
  margin: 0 auto;
  position: relative;
  text-align: center;
  background-color: black;

}

.generated-map-img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-height: calc(100vh - 160px);
  max-width: 100%;
  margin: 0 auto;
  z-index: 2;
  background-color: white;
  
}

.placeholder-img {
  background-color: #bbbbbb;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: calc(100vh - 200px);
  width: 75%;
}

p.placeholder-img {
  height: auto;
  font-size: 40px;
  color: black;
}

#generate-button {
  cursor: default;
}

</style>
