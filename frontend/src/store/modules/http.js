import {
  httpPost,
  httpDelete,
  httpPut,
  httpPatch,
} from "@/functions/httpFunctions";

export default {
  state: {
    loading: false,
    data: {},
  },
  mutations: {
    updateHttpDataDate(state, data) {
      state.data = { date: data };
    },
    resetHttpData(state) {
      state.data = {};
    },
    updateHttpData(state, { key, value }) {
      state.data[key] = value;
    },
    changeLoading(state, data) {
      state.loading = data;
    },
  },
  actions: {
    async httpPATCH(context, { url, data, etag }) {
      context.commit("changeLoading", true);
      context.dispatch("addSnackbar", { text: "Updating data..." });
      console.log("PATCH ->", data);
      const resp = await httpPatch(url, data, etag);
      context.dispatch("addSnackbar", {
        text:
          resp._status === "ERR"
            ? resp._error.message
            : "Updated Successfully!",
      });
      context.commit("resetHttpData");
      context.commit("changeLoading", false);
      return resp;
    },
    async httpPOST(context, { url, data }) {
      context.commit("changeLoading", true);
      context.dispatch("addSnackbar", { text: "Submiting data..." });
      const resp = await httpPost(url, data);
      context.dispatch("addSnackbar", {
        text:
          resp._status === "ERR"
            ? resp._error.message
            : "Submitted Successfully!",
      });
      context.commit("resetHttpData");
      context.commit("changeLoading", false);
      return resp;
    },
    async httpPUT(context, { url, data, etag }) {
      context.commit("changeLoading", true);
      context.dispatch("addSnackbar", { text: "Updating data..." });
      console.log("PUT ->", data);
      const resp = await httpPut(url, data, etag);
      context.dispatch("addSnackbar", {
        text:
          resp._status === "ERR"
            ? resp._error.message
            : "Updated Successfully!",
      });
      context.commit("resetHttpData");
      context.commit("changeLoading", false);
      return resp;
    },
    async httpDELETE(context, { url, etag }) {
      context.commit("changeLoading", true);
      context.dispatch("addSnackbar", { text: "Deleting data..." });
      const resp = await httpDelete(url, etag);
      context.dispatch("addSnackbar", {
        text:
          resp._status === "ERR"
            ? resp._error.message
            : "Deleted Successfully!",
      });
      context.commit("resetHttpData");
      context.commit("changeLoading", false);
      return resp;
    },
  },
};
