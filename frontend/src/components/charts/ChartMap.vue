<template>
  <div id="chart-map">
    <div id="chart-map-creator"></div>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-draw";
import "../../../node_modules/leaflet-draw/dist/leaflet.draw.css";
export default {
  name: "ChartMap",
  components: {},
  data() {
    return {
      mainChartMap: null,
      lastLayer: null
    };
  },
  methods: {
    initChartMap() {
      this.mainChartMap = L.map("chart-map-creator").setView(
        [52.22446892618538, 21.013750325345462],
        12
      );

      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox/streets-v11",
          tileSize: 512,
          zoomOffset: -1,
          accessToken:
            "pk.eyJ1IjoibWFjaWVrMSIsImEiOiJja2poYm8zbGk0eG02MnpsZzVsOHF4YWliIn0.T3ME0f2YUNbKvXYRHRrgog",
        }
      ).addTo(this.mainChartMap);

      
    },
  },
  mounted() {
    this.initChartMap();
  },
};
</script>

<style>
#chart-map-creator {
  width: 100%;
  height: 100%;
}
</style>
