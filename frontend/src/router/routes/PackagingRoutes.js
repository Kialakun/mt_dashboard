import Editor from "@/views/Editor.vue";
import Selector from "@/views/Selector.vue";
//import store from "@/store"

export default {
  path: "/packaging",
  component: Editor,
  children: [
    {
      path: "",
      props: { resource: "packaging" },
      component: Selector,
    },
    {
      path: "form",
      props: { resource: "packaging" },
      component: () => import("@/components/forms/PackagingForm.vue"),
    },
  ],
};
