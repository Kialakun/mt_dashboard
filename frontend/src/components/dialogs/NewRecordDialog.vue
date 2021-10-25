<template>
  <v-dialog
    v-model="dialog"
    persistent
    max-width="500px"
    transition="dialog-transition"
  >
    <v-card>
      <v-card-title>
        {{ title }}
      </v-card-title>
      <v-card-subtitle>
        {{ description }}
      </v-card-subtitle>
      <v-card-text>
        <f-fields :fields="schema" @change="(data) => updatePostData(data)" />
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="success" @click="submit">Submit</v-btn>
        <v-btn text @click="$emit('close')">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import FFields from "@/components/forms/Fields.vue";
export default {
  name: "FNewRecordDialog",
  props: ["title", "description", "schema", "show", "resource"],
  components: {
    FFields,
  },
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    updatePostData(data) {
      this.$store.commit("updateHttpDataDate", data);
    },
    async submit() {
      const data = this.$store.state.http.data;
      const url = "/api/" + this.resource;
      console.log("POST", data);
      const resp = await this.$store.dispatch("httpPOST", {
        url: url,
        data: data,
      });
      console.log(resp._status);
      console.log(resp._error.message);
      return;
    },
  },
  watch: {
    show() {
      this.dialog = !this.dialog;
    },
  },
};
</script>
