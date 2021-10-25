<template>
  <v-container fluid>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <f-table-content
        :key="tableKey"
        :collection="collection"
        :title="title"
        :items="items"
        :headers="headers"
        :schema="schema"
        @refresh="() => setup()"
      />
    </div>
  </v-container>
</template>

<script>
import FTableContent from "@/components/tables/TableContent.vue";

export default {
  props: ["title", "collection", "schema", "headers", "items"],

  components: {
    "f-table-content": FTableContent,
  },

  computed: {
    url() {
      return "/api/" + this.collection;
    },
  },

  data() {
    return {
      tableKey: 0,
      loading: false,
    };
  },

  async created() {
    await this.setup();
  },

  methods: {
    async setup() {
      this.loading = true;
      this.reset();
      await this.checkRelatedFields(this.schema);
      this.loading = false;
    },

    reset() {
      this.tableKey++;
    },

    async getRelatedFieldItems(collection) {
      return this.$store.state.api[collection];
    },

    async checkRelatedFields(fields) {
      console.log("checking data...");
      for (const i in fields) {
        if (fields[i].data_relation) {
          const collection = fields[i].data_relation.resource;
          fields[i]._items = await this.getRelatedFieldItems(collection);
        }
      }
    },
  },

  watch: {
    async $route() {
      await this.setup();
    },
  },
};
</script>
