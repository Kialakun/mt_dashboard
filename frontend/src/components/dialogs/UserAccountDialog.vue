<template>
  <v-dialog
    v-model="dialog"
    scrollable
    max-width="300px"
    transition="dialog-transition"
  >
    <v-card>
      <v-list>
        <v-list-item>
          <v-list-item-icon
            ><v-icon>mdi-account-circle</v-icon></v-list-item-icon
          >
          <v-list-item-content>
            <v-list-item-title class="text-h6"> User Account</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>
          <v-spacer></v-spacer>
          <v-btn text color="success">Logout</v-btn>
        </v-list-item>
      </v-list>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "FUserAccountDialog",
  props: ["show"],
  computed: {
    dialog: {
      get() {
        return this.show;
      },
      set() {
        return this.$emit("close");
      },
    },
  },
};
</script>
