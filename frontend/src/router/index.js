import Vue from "vue";
import VueRouter from "vue-router";
import DashboardRoutes from "./routes/DashboardRoutes";
import PageNotFound from "../views/PageNotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/dashboard",
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/404",
    name: "PageNotFound",
    component: PageNotFound,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

routes.push(DashboardRoutes);

const router = new VueRouter({
  routes,
});

export default router;
