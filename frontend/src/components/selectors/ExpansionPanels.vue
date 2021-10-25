<template>
  <v-expansion-panels accordion flat>
    <v-expansion-panel v-for="(item, i) in items" :key="i">
      <v-expansion-panel-header
        ><span class="font-weight-bold">WK {{ item.week }}</span>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="info" text :to="'/' + resource + '/form'">Edit</v-btn>
          <v-btn color="error" text :to="'/' + resource + '/form'"
            >Delete</v-btn
          >
        </v-card-actions>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
export default {
  name: "FExpansionPanels",
  props: ["resource"],
  components: {},
  computed: {
    schema() {
      return this.$store.state.model.schema[this.resource];
    },
  },
  data() {
    return {
      items: [
        {
          week: 1,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
        {
          week: 2,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
        {
          week: 3,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
        {
          week: 4,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
        {
          week: 5,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
        {
          week: 6,
          cost: {
            water_consumption: 0.2,
            thermal_consumption: 0.3,
          },
        },
      ],
    };
  },
};
</script>
