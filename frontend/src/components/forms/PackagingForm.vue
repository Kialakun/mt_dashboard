<template>
  <v-container>
    <v-card class="mt-2">
      <v-card-title
        >{{ resource }} Focus Form<v-spacer></v-spacer>
        <h1>WK #{{ selectedItem.date.week }}</h1></v-card-title
      >
      <v-card-subtitle>
        Use the tabs to switch between focus groups, and fill the forms. Click
        "Submit" to submit changes.
      </v-card-subtitle>
      <v-card-text class="mx-0">
        <v-tabs
          v-model="tab"
          color="primary"
          slider-color="primary"
          fixed-tabs
          center-active
          show-arrows
        >
          <v-tab v-for="(item, index) in schema" :key="index">
            {{ index }}
          </v-tab>
        </v-tabs>
        <v-tabs-items v-model="tab">
          <v-tab-item v-for="(item, index) in schema" :key="index">
            <v-container fluid>
              <v-row>
                <v-col cols="12" md="6" v-for="(m, i) in item.schema" :key="i">
                  <h4 class="ml-2">{{ m.meta.verbose_name }}</h4>
                  <f-fields
                    :fields="m.schema"
                    :item="selectedItem"
                    @change="(data) => (form[index] = { [i]: data })"
                  ></f-fields>
                </v-col>
              </v-row>
            </v-container>
          </v-tab-item>
        </v-tabs-items>
        <details>
          {{ form }}
        </details>
      </v-card-text>
      <v-card-actions>
        <v-btn text color="primary" @click="submit">Submit</v-btn>
        <v-btn text @click="cancel">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import FFields from "@/components/forms/Fields.vue";

export default {
  components: {
    FFields,
  },
  props: ["resource"],
  mounted() {
    if (!this.selectedItem) {
      this.$store.dispatch("addSnackbar", { text: "No item selected." });
      this.$router.push("/" + this.resource);
    }
  },
  computed: {
    postData() {
      return this.$store.state.http.data;
    },
    selectedItem() {
      return this.$store.state.forms.selectedItem;
    },
    schema() {
      return this.$store.state.model.schema[this.resource];
    },
    tabs() {
      let tabs = [];
      for (const item in this.schema) {
        tabs.push(item);
      }
      return tabs;
    },
  },
  data() {
    return {
      tab: null,
      category: null,
      form: {},
    };
  },
  methods: {
    updateHttpData(data) {
      const d = { key: this.tabs[this.tab], value: data };
      this.$store.commit("updateHttpData", d);
    },
    cancel() {
      this.$store.commit("resetHttpData");
      this.$router.push("/" + this.resource);
    },
    async submit() {
      const data = this.form;
      const url = "/api/" + this.resource + "/" + this.selectedItem._id;
      const etag = this.selectedItem._etag;
      const resp = await this.$store.dispatch("httpPATCH", {
        url: url,
        data: data,
        etag: etag,
      });
      this.$store.dispatch("refreshAPI", this.resource);
      console.log(resp);
    },
  },
  watch: {
    $route() {
      this.$store.commit("clearSelectedItem");
      this.$store.commit("resetHttpData");
    },
  },
};
</script>
