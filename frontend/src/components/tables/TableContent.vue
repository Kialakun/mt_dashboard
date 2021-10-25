<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items="items"
      @click:row="rowClicked"
      dense
    >
      <template v-slot:top>
        <v-toolbar dense flat>
          <span class="font-weight-bold">{{ title }}</span>
          <v-spacer></v-spacer>
          <v-text-field
            name="search"
            label="Search"
            id="search-id"
            solo
            outlined
            dense
            flat
            hide-details
          ></v-text-field>
        </v-toolbar>
        <v-divider></v-divider>
        <v-system-bar
          status
          color="grey lighten-4 text--primary"
          style="height: 30px"
        >
          <v-btn text small @click="activateDialog('create')">New</v-btn>
          <v-btn text small @click="activateDialog('import')" disabled
            >Import</v-btn
          >
          <v-btn text small @click="activateDialog('export')" disabled
            >Export</v-btn
          >
          <v-btn text small @click="activateDialog('settings')">Settings</v-btn>
        </v-system-bar>
        <v-divider></v-divider>
      </template>
    </v-data-table>

    <!-- Table Dialogs -->
    <f-table-dialogs
      :show="dialog"
      :collection="collection"
      :fields="schema"
      :item="selectedItem"
      :headers="headers"
      @refresh="$emit('refresh')"
      @close="deactivateDialog"
    />
  </v-card>
</template>

<script>
import FTableDialogs from "@/components/tables/TableDialogs.vue";

export default {
  name: "FTableContent",

  props: ["title", "collection", "schema", "headers", "items"],

  components: {
    "f-table-dialogs": FTableDialogs,
  },

  data() {
    return {
      dialog: null,
      selectedItem: null,
    };
  },

  methods: {
    deactivateDialog() {
      this.dialog = null;
      this.selectedItem = null;
    },

    activateDialog(dialog) {
      this.dialog = null;
      this.$nextTick(() => {
        this.dialog = dialog;
      });
    },

    rowClicked(item) {
      this.selectedItem = item;
      this.activateDialog("edit");
    },
  },

  watch: {
    $route() {
      this.selectedItem = null;
    },
  },
};
</script>
