import { httpGet } from "../../functions/httpFunctions";

export default {
  state: {
    schema: {},
  },

  mutations: {
    updateSchema(state, data) {
      state.schema = data;
    },
  },

  actions: {
    async getSchema(context) {
      const url = "/api/schema";
      const resp = await httpGet(url);
      context.commit("updateSchema", resp);
    },
  },
};
