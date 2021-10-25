<template>
  <v-container>
    <v-card class="ma-1" :key="key">
      <v-card-text>
        <span class="titlize font-weight-bold"
          >{{ dashboard }} | {{ chart }}</span
        >
        <f-chart v-if="config" :config="config" id="chart" />
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import FChart from "@/components/charts/Chart.vue";

export default {
  name: "FDashboardChart",
  components: {
    FChart,
  },
  async mounted() {
    this.config = await this.$store.dispatch("renderChart", {
      vue: this,
      dashboard: this.dashboard,
      chart: this.chart,
    });
  },
  computed: {
    dashboard() {
      return this.$route.params.dashboard;
    },
    chart() {
      return this.$route.params.chart;
    },
  },
  data() {
    return {
      key: 0,
      config: null,
    };
  },
  watch: {
    async $route() {
      this.config = await this.$store.dispatch("renderChart", {
        vue: this,
        dashboard: this.dashboard,
        chart: this.chart,
      });
      this.key++;
    },
  },
};
</script>
