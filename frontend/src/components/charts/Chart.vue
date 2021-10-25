<template>
  <v-container fluid>
    <canvas :id="id"></canvas>
  </v-container>
</template>

<script>
// import { Chart, LineElement, LineController } from 'chart.js'
import Chart from "chart.js/auto";
// Register Chart Components
// Chart.register(Chart, LineElement, LineController)
// Register date adapter
import "chartjs-adapter-date-fns";

export default {
  name: "FChart",

  props: ["config", "update", "id"],

  mounted() {
    this.renderChart();
  },

  data() {
    return {
      chart: null,
    };
  }, // END data

  methods: {
    renderChart() {
      var ctx = document.getElementById(this.id);
      this.chart = new Chart(ctx, this.config);
    },
  },

  watch: {
    update() {
      this.chart.update();
    },
    config() {
      this.chart.update();
    },
  },
};
</script>
