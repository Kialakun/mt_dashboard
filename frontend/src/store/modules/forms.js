export default {
  state: {
    selectedItem: null,
    resource: null,
    data: {},
  },
  mutations: {
    selectResource(state, resource) {
      state.resource = resource;
    },
    selectItem(state, item) {
      state.selectedItem = item;
    },
    clearSelectedItem(state) {
      state.selectedItem = null;
    },
  },
};
