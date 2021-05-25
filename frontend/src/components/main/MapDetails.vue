<template>
  <div id="map-details">
    <div class="mask-image-fixed"></div>
    <div class="details-containter">
      <section id="pollution-type-section">
        <p>Wybierz rodzaj zanieczyszczeń</p>
        <div class="radio-buttons-pollution-type">
            <input type="radio" id="o3" value="o3" v-model="selectedPollutionType">
            <label for="o3">O3</label>
            <input type="radio" id="so2" value="so2" v-model="selectedPollutionType">
            <label for="so2">SO2</label>
            <input type="radio" id="pm10" value="pm10" v-model="selectedPollutionType">
            <label for="pm10">PM10</label>
            <input type="radio" id="c6h6" value="c6h6" v-model="selectedPollutionType">
            <label for="c6h6">C6H6</label>
            <input type="radio" id="co" value="co" v-model="selectedPollutionType">
            <label for="co">CO</label>
            <input type="radio" id="no2" value="no2" v-model="selectedPollutionType">
            <label for="no2">NO2</label>
            <input type="radio" id="pm25" value="pm25" v-model="selectedPollutionType">
            <label for="pm25">PM2.5</label>
        </div>
        <p>Wybierz liczbę segmentów</p>
        <select v-model="selectedSegmentsNumber">
          <option v-for="n in 20" :key="n" >{{ n }}</option>
        </select>
      </section>
      <section id="time-section">
        <p>Wybierz datę i godzinę</p>
        <date-picker v-model="pollutionTime" type="datetime" value-type="format" format="YYYY-MM-DD HH:00:00"></date-picker>
        <button id="confirm-button" v-on:click="closeOptionsModal">OK</button>
      </section>
    </div>
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

export default {
  name: "MapDetails",
  components: {DatePicker},
  methods: {
      closeOptionsModal() {
          document.getElementById("map-details").style.display = "none";
          this.$emit('details-data', {param: this.selectedPollutionType, segments: this.selectedSegmentsNumber, time: this.pollutionTime});
      }
  },
  data() {
      return {selectedPollutionType: "pm25",
      selectedSegmentsNumber: 8,
      pollutionTime: null,}
  }
};
</script>

<style>

#map-details {
    display: none;
}

.details-containter {
    position: fixed;
    z-index: 3;
    height: 60vh;
    width: 40vw;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    background-color: white;
    border: black solid 2px;
    border-radius: 50px;
    color: black;
    text-align: center;

}

div .mask-image-fixed {
    position: fixed;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 2;
    top: 0px;
    left: 0px;
}

#pollution-type-section {
    float: left;
    width: 50%;
    padding: 20px;
}

.details-containter p {
    font-weight: bold;
    font-size: 20px;
    text-align: center;
    color: black;
    margin: 15px 0px 15px 0px;
}

#time-section {
    float: right;
    width: 50%;
    padding: 20px;
    position: relative;
    height: 100%;
}


#pollution-type-section select {
    font-size: 16px;
}

.radio-buttons-pollution-type {
    text-align: left;
    margin-bottom: 50px;
    font-size: 16px;

}

.radio-buttons-pollution-type label {
    margin-left: 8px;
    margin-right: 12px;
}

#confirm-button {
    position: absolute;
    bottom: 15px;
    right: 30px;
    border: solid 3px black;
    border-radius: 5px;
    background-color: white;
    font-weight: bold;
    font-size: 16px;
    padding: 5px 15px;
}
</style>
