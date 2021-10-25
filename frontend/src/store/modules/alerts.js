export default {
  state: {
    alerts: [],
    snackbar: null,
  },
  mutations: {
    removeAlert(state, index) {
      state.alerts.splice(index, 1);
    },
    addAlert(state, alert) {
      state.alerts.push(alert);
    },
    removeSnackbar(state) {
      state.snackbar = null;
    },
    addSnackbar(state, snackbar) {
      state.snackbar = snackbar;
    },
  },
  actions: {
    removeAlert(context, index) {
      context.commit("removeAlert", index);
    },
    addAlert(context, alert) {
      context.commit("addAlert", alert);
    },
    removeSnackbar(context, index) {
      context.commit("removeSnackbar", index);
    },
    addSnackbar(context, snackbar) {
      context.commit("addSnackbar", snackbar);
    },
  },
};
