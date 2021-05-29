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
      <a
        class="ca3-scroll-down-link ca3-scroll-down-arrow"
        v-on:click="scrollToMapSelection"
        data-ca3_iconfont="ETmodules"
        data-ca3_icon=""
      ></a>
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

  methods: {
    scrollToMapSelection() {
      const element = document.getElementById("map-selection");
      const offset = 80;
      const bodyRect = document.body.getBoundingClientRect().top;
      const elementRect = element.getBoundingClientRect().top;
      const elementPosition = elementRect - bodyRect;
      const offsetPosition = elementPosition - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
    },
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

html body [data-ca3_iconfont="ETmodules"]::before {
  font-family: "ETmodules";
}
[data-ca3_icon]::before {
  font-weight: normal;
  content: attr(data-ca3_icon);
}

.ca3-scroll-down-arrow {
  background-image: url("../../../img/down-arrow.svg");
  background-size: contain;
  background-repeat: no-repeat;
}

.ca3-scroll-down-link {
  cursor: pointer;
  height: 60px;
  width: 80px;
  margin: 0px 0 0 -40px;
  line-height: 60px;
  position: absolute;
  left: 50%;
  bottom: 30px;
  color: #fff;
  text-align: center;
  font-size: 70px;
  z-index: 2;
  text-decoration: none;
  text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.4);

  -webkit-animation: ca3_fade_move_down 3s ease-in-out infinite;
  -moz-animation: ca3_fade_move_down 3s ease-in-out infinite;
  animation: ca3_fade_move_down 3s ease-in-out infinite;
}

@-webkit-keyframes ca3_fade_move_down {
  0% {
    -webkit-transform: translate(0, -20px);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    -webkit-transform: translate(0, 20px);
    opacity: 0;
  }
}
@-moz-keyframes ca3_fade_move_down {
  0% {
    -moz-transform: translate(0, -20px);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    -moz-transform: translate(0, 20px);
    opacity: 0;
  }
}
@keyframes ca3_fade_move_down {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: translate(0, 20px);
    opacity: 0;
  }
}
</style>
