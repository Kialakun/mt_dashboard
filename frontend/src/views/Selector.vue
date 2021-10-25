<template>
  <v-container>
    <v-card elevation="2">
      <v-card-title class="titlize">{{ resource }} Records</v-card-title>
      <v-card-subtitle>Records by ISO Week Number</v-card-subtitle>
      <v-card-text>
        <f-treeview :resource="resource" />
        <v-pagination :length="length" v-model="page"></v-pagination>
      </v-card-text>
      <v-card-actions>
        <v-btn text color="secondary" @click="newRecord">New</v-btn>
        <v-btn text color="secondary" disabled>Export</v-btn>
        <v-btn text color="secondary" disabled>Import</v-btn>
        <f-new-record-dialog
          title="New Record"
          description="Create a new record by filling in the following."
          :resource="resource"
          :schema="schema[resource].date.schema"
          :show="dialog.new"
          @close="dialog.new = false"
        />
      </v-card-actions>
    </v-card>
  </v-container>
</template>
<script>
import FTreeview from "@/components/selectors/Treeview.vue";
import FNewRecordDialog from "@/components/dialogs/NewRecordDialog.vue";
export default {
  props: ["resource"],
  components: {
    FTreeview,
    FNewRecordDialog,
  },
  computed: {
    schema() {
      return this.$store.state.model.schema;
    },
    loading() {
      return this.$store.state.http.loading;
    },
  },
  data() {
    return {
      length: 3,
      page: 1,
      dialog: {
        new: false,
      },
    };
  },
  methods: {
    newRecord() {
      this.dialog.new = true;
    },
  },
};
</script>
