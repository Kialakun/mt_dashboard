import { setTarget } from "../../functions/chartFunctions";

export default {
  state: {
    cost: {
      dashboard: {
        title: "Cost Dashboard",
        data: [{}],
        datasets: [
          {
            api: "packaging",
            targets: {
              target: "",
              condition: "gt",
            },
            config: {
              type: "bar",
              label: "Packaging",
              parsing: { xAxisKey: "date.start", yAxisKey: "cost._total" },
            },
          },
          {
            api: "utilities",
            targets: {
              target: "",
              condition: "lt",
            },
            config: {
              type: "bar",
              label: "Utilities",
              parsing: { xAxisKey: "date.start", yAxisKey: "cost._total" },
            },
          },
        ],
      },
      Packaging: {
        title: "Packaging Cost Depolyoment",
        data: [{}],
        datasets: [
          {
            api: "packaging",
            data: [{}],
            config: {
              type: "bar",
              label: "Packaging Thermal Consumption",
              parsing: {
                xAxisKey: "date.start",
                yAxisKey: "cost.thermal_consumption._total",
              },
            },
          },
          {
            api: "packaging",
            data: [{}],
            config: {
              type: "bar",
              label: "Packaging Water Consumption",
              parsing: {
                xAxisKey: "date.start",
                yAxisKey: "cost.water_consumption._total",
              },
            },
          },
          {
            api: "packaging",
            data: [{}],
            config: {
              type: "bar",
              label: "Packaging Power Consumption",
              parsing: {
                xAxisKey: "date.start",
                yAxisKey: "cost.power_consumption._total",
              },
            },
          },
        ],
      },
      "Packaging Water Consumption": {
        title: "Packaging Water Consumption Deployment",
        data: [{}],
        datasets: [
          {
            api: "packaging",
            config: {
              type: "bar",
              label: "Bottle Conveyor",
              parsing: {
                xAxisKey: "date.start",
                yAxisKey: "cost.water_consumption.bottle_conveyor",
              },
            },
          },
        ],
      },
    },
  },
  mutations: {
    setChartData(state, { dashboard, chart, data }) {
      state[dashboard][chart].data = data;
    },
  },
  actions: {
    renderChart(context, { vue, dashboard, chart }) {
      // get dashboard
      if (!(dashboard in context.state)) {
        return console.log("No dashboard");
      }
      // get base config
      const base = context.rootState.chart.baseConfig;
      // get chart config
      let c = context.state[dashboard][chart];
      if (!c) {
        vue.$router.push("/404");
      }
      // perform deep copy, to create new object with no reference to baseConfig
      let config = JSON.parse(JSON.stringify(base));
      // get datasets and update config data
      for (const n in c.datasets) {
        let resource = c.datasets[n].api;
        // set chart data
        context.commit("setChartData", {
          dashboard,
          chart,
          data: context.rootState.api[resource],
        });
        // merge chart data with dataset config
        let d = Object.assign({ data: c.data }, c.datasets[n].config);
        config.data.datasets.push(d);
        // merge title
        Object.assign(config.options.plugins, {
          title: { text: chart.title, display: true },
        });
        // merge onClick option
        config.options.onClick = (e, activeElements) => {
          console.log(activeElements);
          if (activeElements.length === 0) {
            console.log("No element.");
            return;
          }
          // const dataIndex = activeElements[0].element.$context.dataIndex;
          // const data = activeElements[0].element.$context.dataset.data[dataIndex];
          const label = activeElements[0].element.$context.dataset.label;
          //const value = data.date.start;
          vue.$router.push("/dashboard/" + dashboard + "/" + label);
        };
      }
      setTarget(context.rootState.api.targets, "gt", config.data.datasets);
      console.log(config);
      return config;
    },
  },
};
