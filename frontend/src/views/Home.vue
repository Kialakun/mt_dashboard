<template>
  <v-container fluid>
    <v-card>
      {{ api }}
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data() {
    return {};
  },

  components: {},

  computed: {
    api() {
      return this.$store.state;
    },
  },
};
</script>
