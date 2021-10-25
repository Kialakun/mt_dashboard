<template>
  <div>
    <!-- Related Field -->
    <div v-if="field.allowed || field.type === 'objectid'">
      <v-select
        v-if="field.type === 'objectid' && !(fieldName === '_id')"
        :items="field._items"
        v-model="postData"
        :hint="hasHint(field) ? field.meta.hint : ''"
        :label="hasVerboseName(field) ? field.meta.verbose_name : fieldName"
        :required="field.required"
        :placeholder="field.default"
        :item-text="field.meta.item_text"
        :item-value="field.meta.item_value"
        :disabled="isDisabled(field)"
        :error-messages="err"
        outlined
        dense
        persistent-hint
      ></v-select>
      <!-- Select Field -->
      <v-select
        v-if="field.allowed && field.type !== 'objectid'"
        :items="field.allowed"
        v-model="postData"
        :hint="hasHint(field) ? field.meta.hint : ''"
        :label="hasVerboseName(field) ? field.meta.verbose_name : fieldName"
        :required="field.required"
        :placeholder="field.default"
        :disabled="isDisabled(field)"
        :error-messages="err"
        outlined
        dense
        persistent-hint
      ></v-select>
    </div>
    <div v-else>
      <!-- TestArea Field -->
      <v-textarea
        v-if="isTextArea(field)"
        :name="fieldName"
        :placeholder="field.default"
        v-model="postData"
        :hint="hasHint(field) ? field.meta.hint : ''"
        :label="hasVerboseName(field) ? field.meta.verbose_name : fieldName"
        :required="field.required"
        :disabled="isDisabled(field)"
        :error-messages="err"
        outlined
        dense
        persistent-hint
      >
      </v-textarea>
      <!-- Text, Decimal Field -->
      <v-text-field
        v-if="
          (!isTextArea(field) && field.type === 'string') ||
          field.type === 'decimal' ||
          field.type === 'integer'
        "
        :name="fieldName"
        :placeholder="field.default"
        v-model="postData"
        :type="
          field.type === 'decimal' || field.type === 'integer'
            ? 'number'
            : 'text'
        "
        :hint="hasHint(field) ? field.meta.hint : ''"
        :label="hasVerboseName(field) ? field.meta.verbose_name : fieldName"
        :required="field.required"
        :disabled="isDisabled(field)"
        :error-messages="err"
        outlined
        dense
        persistent-hint
      ></v-text-field>
      <!-- Date Field -->
      <v-dialog
        v-if="field.type === 'datetime'"
        ref="dialog"
        v-model="datepicker.active"
        persistent
        :disabled="isDisabled(field)"
        width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="postData"
            :hint="hasHint(field) ? field.meta.hint : ''"
            :label="hasVerboseName(field) ? field.meta.verbose_name : fieldName"
            :placeholder="field.default"
            append-icon="mdi-calendar"
            :required="field.required"
            :error-messages="err"
            outlined
            dense
            readonly
            persistent-hint
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="postData" scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="datepicker.active = false">
            Select
          </v-btn>
        </v-date-picker>
      </v-dialog>
    </div>
  </div>
</template>

<script>
export default {
  name: "FFormField",

  props: ["field", "fieldName", "editData", "disable", "err"],

  mounted() {
    this.itemSetup();
  },

  computed: {
    update() {
      return this.postData;
    },
  },

  data: () => {
    return {
      datepicker: {
        active: false,
      },
      postData: null,
    };
  },

  methods: {
    isDisabled(field) {
      if ("meta" in field) {
        if ("disabled" in field.meta) {
          return field.meta.disabled;
        }
      }
      return false;
    },

    itemSetup() {
      if (this.editData) {
        this.postData = this.editData;
      }
      console.log(this.postData);
    },

    isTextArea(field) {
      if (field.type === "string" && field.maxlength > 50) {
        return true;
      }
      return false;
    },

    hasVerboseName(field) {
      if (field.meta) {
        if (field.meta.verbose_name) {
          return true;
        }
      }
      return false;
    },

    hasHint(field) {
      if (field.meta) {
        if (field.meta.hint) {
          return true;
        }
      }
      return false;
    },
  },

  watch: {
    $route() {
      this.postData = null;
    },

    update() {
      this.$emit("post", this.postData);
    },
  },
};
</script>
