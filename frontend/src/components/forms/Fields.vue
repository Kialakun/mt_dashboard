<template>
  <v-container fluid>
    <v-row justify="start" no-gutters>
      <v-col cols="12" v-for="(field, key) in fields" :key="key + '-field'">
        <div v-if="field.type == 'dict' || 'schema' in field">
          <v-divider></v-divider>
          <v-subheader class="px-0">{{ field.meta.verbose_name }}</v-subheader>
          <div
            v-for="(dictField, dictFieldName) in field.schema"
            :key="key + '-' + dictFieldName + '-field'"
          >
            <FFormField
              :field="dictField"
              :fieldName="dictFieldName"
              @post="
                (data) => {
                  let o = {};
                  if (key in postData) {
                    o = Object.assign({}, postData[key]);
                  }
                  o[dictFieldName] = data;
                  $set(postData, key, o);
                }
              "
              :edit-data="item ? item[key][dictFieldName] : null"
              :err="errs ? errs[key][dictFieldName] : null"
            />
          </div>
          <v-divider></v-divider>
        </div>
        <div v-else>
          <FFormField
            :field="field"
            :field-name="key"
            @post="(data) => updateHttpData(key, data)"
            :err="errs ? errs[key] : null"
            :edit-data="key in item ? item[key] : null"
          />
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FFormField from "./FormField.vue";

export default {
  name: "FFields",

  props: ["editItem", "fields", "errs"],

  components: {
    FFormField,
  },

  computed: {
    item() {
      return this.editItem ? this.editItem : {};
    },
  },

  data() {
    return {
      postData: {},
    };
  },
  methods: {
    updateHttpData(key, value) {
      this.$set(this.postData, key, value);
      this.$emit("change", this.postData);
    },
  },

  watch: {
    $route() {
      console.log("reset http data ...");
      this.$store.commit("updateHttpData", {});
    },
  },
};
</script>
