<template>
  <div id="map">
    <div id="map-creator"></div>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-draw";
import "../../../node_modules/leaflet-draw/dist/leaflet.draw.css";
export default {
  name: "Map",
  components: {},
  data() {
    return {
      mainMap: null,
      lastLayer: null
    };
  },
  methods: {
    initMap() {
      this.mainMap = L.map("map-creator").setView(
        [52.22446892618538, 21.013750325345462],
        12
      );
      var editableLayers = new L.FeatureGroup();
      this.mainMap.addLayer(editableLayers);

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
      ).addTo(this.mainMap);

      var drawControlFull = new L.Control.Draw({
        draw: {
          marker: false,
          polygon: false,
          polyline: false,
          rectangle: {
            shapeOptions: {
              clickable: false,
            },
          },
          circle: false,
          circlemarker: false,
        },
        edit: {
          featureGroup: editableLayers,
          remove: false,
        },
      });

      var drawControlEditOnly = new L.Control.Draw({
        edit: {
          featureGroup: editableLayers,
        },
        draw: false,
      });
      this.mainMap.addControl(drawControlFull);
      this.mainMap.on(L.Draw.Event.CREATED, (e) => {
        editableLayers.addLayer(e.layer);
        drawControlFull.remove(this.mainMap);
        this.mainMap.addControl(drawControlEditOnly);
        this.$emit('lat-lon-coordinates', e.layer.getLatLngs());
      });
      this.mainMap.on(L.Draw.Event.DELETED, () => {
          if (editableLayers.getLayers().length === 0) {
              drawControlEditOnly.remove(this.mainMap);
              this.mainMap.addControl(drawControlFull);
          }
      });
    },
  },
  mounted() {
    this.initMap();
  },
};
</script>

<style>
#map-creator {
  width: 100%;
  height: 100%;
}
</style>
