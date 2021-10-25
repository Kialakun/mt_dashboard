<template>
  <v-list>
    <v-list-item v-for="(item, i) in items" :key="i">
      <f-list-all v-if="'schema' in item" :items="item.schema"></f-list-all>
      <span v-else>{{ i }}</span>
    </v-list-item>
  </v-list>
</template>
<script>
import FListAll from "./ListAll.vue";
export default {
  name: "FList",
  components: {
    FListAll,
  },
  props: ["items"],
};
</script>
