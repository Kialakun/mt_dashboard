<template>
  <v-dialog
    v-model="dialog"
    persistent
    max-width="300px"
    transition="dialog-transition"
  >
    <v-card>
      <v-card-title class="titlize">{{ resource }} | Import </v-card-title>
      <v-card-text>
        <p>Upload data from a MS Excel file.</p>
        <p>Please ensure data is complete and does not have any blanks.</p>
        <p>
          <v-file-input
            accept="image/*"
            label="Select File"
            outlined
            dense
          ></v-file-input>
        </p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="close">Cancel</v-btn>
        <v-btn text color="primary" dark>Import</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "FImportDialog",
  props: ["show", "url", "resource"],
  data() {
    return {
      dialog: false,
      file: null,
    };
  },
  methods: {
    close() {
      this.dialog = false;
      this.$emit("close");
    },
    importFile() {},
  },
  watch: {
    show() {
      this.dialog = this.show;
    },
  },
};
</script>
