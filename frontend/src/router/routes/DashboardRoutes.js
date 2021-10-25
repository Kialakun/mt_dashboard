import Dashboard from "@/views/Dashboard.vue";
export default {
  path: "/dashboard",
  component: Dashboard,
  children: [
    {
      path: ":dashboard/:chart",
      component: () => import("@/views/DashboardChart.vue"),
    },
  ],
};
