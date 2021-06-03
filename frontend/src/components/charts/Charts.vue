<template>
  <div id="charts-main">
    <div class="section-wrapper">
      <section id="generated-chart"></section>
      <section id="station-selection-map">
        <ChartMap
          class="map-image-chart"
          @lat-lon-coordinates="registerCords" @station-id="stationIdUpdate"
        />
        <div id="chart-option-buttons">
          <div class="calendar">
            <date-picker
              v-model="pollutionTimeChart"
              type="datetime"
              placeholder="Ostatnie 24 godziny"
              value-type="format"
              range
              format="YYYY-MM-DD HH:00:00"
            ></date-picker>
          </div>
          <p class="calendar"></p>
          <div class="radio-buttons-pollution-type radio-chart">
            <input
              type="radio"
              id="o3"
              value="o3"
              v-model="selectedPollutionTypeChart"
            />
            <label for="o3">O3</label>
            <br />
            <input
              type="radio"
              id="so2"
              value="so2"
              v-model="selectedPollutionTypeChart"
            />
            <label for="so2">SO2</label>
            <br />
            <input
              type="radio"
              id="pm10"
              value="pm10"
              v-model="selectedPollutionTypeChart"
            />
            <label for="pm10">PM10</label>
            <br />
            <input
              type="radio"
              id="c6h6"
              value="c6h6"
              v-model="selectedPollutionTypeChart"
            />
            <label for="c6h6">C6H6</label>
            <br />
            <input
              type="radio"
              id="co"
              value="co"
              v-model="selectedPollutionTypeChart"
            />
            <label for="co">CO</label>
            <br />
            <input
              type="radio"
              id="no2"
              value="no2"
              v-model="selectedPollutionTypeChart"
            />
            <label for="no2">NO2</label>
            <br />
            <input
              type="radio"
              id="pm25"
              value="pm25"
              v-model="selectedPollutionTypeChart"
            />
            <label for="pm25">PM2.5</label>
          </div>
          <button v-on:click="fetchChart" id="generate-button-chart" disabled="true">
            Generuj
          </button>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import ChartMap from "@/components/charts/ChartMap.vue";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
// eslint-disable-next-line
delete L.Icon.Default.prototype._getIconUrl;
// eslint-disable-next-line
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});
export default {
  name: "Charts",
  components: {
    ChartMap,
    DatePicker,
  },
  methods: {
    stationIdUpdate(stationIdUpdated) {
      this.stationId = stationIdUpdated;
    },

    fetchChart() {
      var dateStart, dateEnd
      var urlString = `http://localhost:80/stations/data/?&id=${this.stationId}&param=${this.selectedPollutionTypeChart}`
      if (this.time != undefined) {
        dateStart = this.time[0].replace(" ", "T");
        dateEnd = this.time[1].replace(" ", "T");
        urlString += `&date_from=${dateStart}&date_to=${dateEnd}`
      }
      
      fetch(urlString)
        .then((data) => data.json())
        .then((data) => {
            console.log(data.stations)
        }
        );
    },
  },
  data() {
    return {
      selectedPollutionTypeChart: "pm25",
      pollutionTimeChart: [],
      stationId: null,
    };
  },
};
</script>

<style>
#charts-main {
  background-color: white;
  margin: 0 auto;
  width: 100%;
  top: 80px;
  height: calc(100vh - 80px);
  position: relative;
}

p.calendar {
  color: black;
  font-weight: bold;
  margin-top: 10px;
}

.section-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

#charts-main section {
  height: calc(100% - 80px);
  position: relative;
}

.radio-buttons-pollution-type.radio-chart {
  position: absolute;
  left: 20px;
  bottom: 20px;
}

.radio-buttons-pollution-type.radio-chart {
  margin: 0px;
  font-weight: bold;
}

#generated-chart {
  float: left;
  width: 70%;
}

.calendar {
  width: 100%;
}

.radio-buttons-pollution-type.radio-chart label {
  font-size: 18px;
  color: black;
  margin-left: 8px;
  margin-right: 12px;
}

#station-selection-map {
  float: right;
  width: 30%;
}

.center-absolute {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#chart-option-buttons {
  position: absolute;
  width: 100%;
  height: 50%;
  padding: 20px;

  text-align: center;
}

#chart-option-buttons button {
  border: solid 3px black;
  border-radius: 5px;
  background-color: white;
  font-weight: bold;
  font-size: 16px;
  width: 150px;
  height: 35px;
  box-shadow: 10px 5px 5px black;
  bottom: 20px;
  right: 20px;
  position: absolute;
}

.map-image-chart {
  height: 50%;
  width: 100%;
}

#generated-chart {
  background-color: #bbbbbb;
}

#generate-button-chart {
  cursor: default;
}
</style>
