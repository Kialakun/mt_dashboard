<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn
        v-on="on"
        :icon="get('icon')"
        :text="get('text')"
        :small="get('small')"
        :elevation="get('elevation')"
        :to="to"
        :color="color"
      >
        <v-icon v-if="icon">{{ icon }}</v-icon>
        <span v-if="text">{{ text }}</span>
      </v-btn>
    </template>
    <span>{{ tooltip }}</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "FTooltipBtn",

  props: ["icon", "color", "options", "tooltip", "text", "to"],

  methods: {
    get(val) {
      const options = this.options;
      if (!options) {
        return console.log("no options in tooltip btn.");
      }

      if (val in options) {
        return options[val];
      }

      return null;
    },
  },
};
</script>
