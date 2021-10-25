import Vue from "vue";
import Vuex from "vuex";
import model from "@/store/modules/model";
import api from "@/store/modules/api";
import http from "@/store/modules/http";
import alerts from "@/store/modules/alerts";
import forms from "@/store/modules/forms";
import chart from "./modules/chart";
import dashboard from "./modules/dashboard";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  modules: {
    chart,
    forms,
    alerts,
    api,
    model,
    http,
    dashboard,
  },
});
