<template>
  <v-container class="pa-0" fluid>
    <v-toolbar dense flat outlined>
      <v-spacer></v-spacer>
      <v-toolbar-title class="font-weight-bold titlize">
        {{ resource }} Resource</v-toolbar-title
      >
    </v-toolbar>
    <v-item-group>
      <v-container>
        <v-row>
          <v-col v-for="(option, index) in options" :key="'option' + index">
            <v-card height="200" outlined>
              <v-img height="100" src="@/assets/logo.svg"></v-img>
              <v-card-title
                ><v-icon class="mr-3">{{ option.icon }}</v-icon
                >{{ option.text }}</v-card-title
              >
              <v-card-text>
                {{ option.description }}
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
  </v-container>
</template>
<script>
export default {
  computed: {
    resource() {
      /*
      if (!(this.$route.params.resource in this.resources)) {
        this.$router.push("/404");
      }
      */
      return this.$route.params.resource;
    },
  },
  data() {
    return {
      resources: ["packaging", "utilities", "safety", "quality", "logistics"],
      options: [
        {
          icon: "mdi-import",
          text: "Import",
          description: "Import data from MS Excel file.",
        },
        {
          icon: "mdi-export",
          text: "Export",
          description: "Export data to a MS Excel file.",
        },
        {
          icon: "mdi-file",
          text: "Download Import Template File",
          description: "Download MS Excel import template file.",
        },
      ],
    };
  },
};
</script>
