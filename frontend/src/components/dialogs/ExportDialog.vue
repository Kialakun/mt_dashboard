<template>
  <v-dialog
    v-model="show"
    persistent
    max-width="400px"
    transition="dialog-transition"
  >
    <v-card>
      <v-card-title class="titlize"> {{ resource }} | Export </v-card-title>
      <v-card-text>
        <p>Export data to a MS Excel File.</p>
        <p>
          <v-select
            :items="focusItems"
            outlined
            v-model="body.focus"
            item-value="item"
            item-text="label"
            label="Focus"
            dense
          ></v-select>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                name="start_date"
                label="Start Date"
                id="id-start-date"
                outlined
                dense
                append-icon="mdi-calendar"
                v-bind="attrs"
                v-model="body.start"
                v-on="on"
              ></v-text-field>
            </template>
            <v-list>
              <v-list-item>
                <v-date-picker
                  v-model="body.start"
                  portrait
                  :reactive="true"
                ></v-date-picker>
              </v-list-item>
            </v-list>
          </v-menu>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                name="end_date"
                label="End Date"
                id="id-end-date"
                outlined
                dense
                append-icon="mdi-calendar"
                v-on="on"
                v-bind="attrs"
                v-model="body.end"
              ></v-text-field>
            </template>
            <v-list>
              <v-list-item>
                <v-date-picker
                  v-model="body.end"
                  portrait
                  :reactive="true"
                ></v-date-picker>
              </v-list-item>
            </v-list>
          </v-menu>
        </p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="close">Cancel</v-btn>
        <v-btn text color="success" @click="submit">Export</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: ["show", "url", "resource"],
  data() {
    return {
      focusItems: [
        { item: "cost", label: "Cost" },
        { item: "safety", label: "Safety" },
        { item: "production", label: "Production" },
        { item: "wow", label: "Way of Work" },
      ],
      body: {
        start: null,
        end: null,
        focus: null,
      },
    };
  },
  methods: {
    reset() {
      this.body = {
        start: null,
        end: null,
        focus: null,
      };
    },
    submit() {
      var url = "/api/export?resource=" + this.resource;
      if (this.body.focus) {
        url = url + "&focus=" + this.body.focus;
      }
      if (this.body.start) {
        url = url + "&start=" + this.body.start;
      }
      if (this.body.end) {
        url = url + "&end=" + this.body.end;
      }
      window.location.href = url;
    },

    close() {
      this.reset();
      this.$emit("close");
    },
  },
};
</script>
