<template>
  <v-list>
    <v-list-item v-for="(item, i) in items" :key="i">
      <v-list-item-content v-if="'schema' in item">
        <v-subheader>{{ item.meta.verbose_name }}</v-subheader>
        <f-list :items="item.schema"></f-list>
      </v-list-item-content>
      <v-list-item-content v-else>
        <v-subheader>{{ i }}</v-subheader>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>
<script>
import FList from "./List.vue";

export default {
  props: ["items"],
  components: {
    FList,
  },
};
</script>
