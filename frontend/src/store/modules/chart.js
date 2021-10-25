export default {
  state: {
    selected: {
      dashboard: null,
      chart: null,
    },
    baseConfig: {
      data: {
        datasets: [],
      },
      options: {
        plugins: {
          legend: {
            display: true,
            position: "bottom",
            align: "start",
          },
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    },
  },
  mutations: {
    selectChart(state, chart) {
      state.selected.chart = chart;
    },
    selectDashboard(state, dashboard) {
      state.selected.dashboard = dashboard;
    },
  },
  actions: {},
};
