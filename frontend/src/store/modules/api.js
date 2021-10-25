import { httpGet } from "@/functions/httpFunctions";

export default {
  state: {},
  mutations: {
    updateAPI(state, { collection, data }) {
      state[collection] = data;
    },
  },
  actions: {
    async getAPI(context) {
      const schema = Object.assign({}, context.rootState.model.schema);
      for (const s in schema) {
        const url = "/api/" + s;
        const resp = await httpGet(url);
        context.commit("updateAPI", { collection: s, data: resp._items });
        console.log("retreiving data ->", s, "->", url);
      }
    },
    async refreshAPI(context, collection) {
      const url = "/api/" + collection;
      const resp = await httpGet(url);
      context.commit("updateAPI", { collection, data: resp._items });
    },
    resetPostData(context) {
      context.state.postdata = {};
    },
  },
  getters: {
    focusOn:
      (state) =>
      ({ resource, focus }) => {
        if (focus in state[resource]) {
          return state[resource][focus];
        }
      },
  },
};
