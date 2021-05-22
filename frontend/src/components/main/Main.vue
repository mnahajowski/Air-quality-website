<template>
  <div id="map-main">
    <div id="main-image">
      <div class="mask-image"></div>
    </div>
    <div class="empty-box">
      <div class="main-map-greetings-text">
        <h1>Sprawdź czym oddychasz</h1>
        <p>
          W powietrzu wokół nas unoszą się liczne zanieczyszczenia. Sprawdź
          jakość powietrza dla swojego regionu w ostatnich dniach i porównuj
          statystyki z innymi stacjami pomiarowymi.
        </p>
      </div>
    </div>

    <MapSelection />
  </div>
</template>

<script>
import MapSelection from "@/components/main/MapSelection.vue";

export default {
  name: "Main",
  components: {
    MapSelection,
  },
};
</script>

<style>
#main-image {
  width: 100%;
  height: 100vh;
  background: url("../../../img/wiatraki.jpg") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  position: absolute;
  z-index: 1;
}

.mask-image {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  z-index: 2;
}

.main-map-greetings-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font: 300 24px "Roboto";
  color: white;
  z-index: 3;
}

.main-map-greetings-text p {
  font: italic 300 20px "Roboto Condensed";
  margin-top: 15px;
}

.empty-box {
  width: 100%;
  height: 100vh;
}
</style>
