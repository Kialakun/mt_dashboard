<template>
  <v-container fluid pa-0>
    <v-toolbar dense flat>
      <v-tabs v-model="focus" center-active dense show-arrows>
        <v-tab
          v-for="(tab, i) in tabs"
          :key="i"
          class="titlize"
          :to="'/dashboard/' + tab + '/dashboard'"
        >
          {{ tab }}
        </v-tab>
      </v-tabs>
      <v-spacer></v-spacer>
      <v-menu offset-y dense>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on"><v-icon>mdi-dots-vertical</v-icon></v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="item in options"
            :key="item.key"
            @click="item.click"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title class="titlize">{{
              item.key
            }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-row align="center">
      <v-col>
        <router-view />
      </v-col>
    </v-row>
    <!-- dialogs -->
    <f-targets-dialog
      :show="showTargets"
      @close="showTargets = false"
    ></f-targets-dialog>
  </v-container>
</template>

<script>
import FTargetsDialog from "@/components/dialogs/TargetsDialog.vue";

export default {
  components: {
    FTargetsDialog,
  },
  data() {
    return {
      showTargets: false,
      tabs: ["safety", "cost", "production", "quality", "wow"],
      focus: 0,
      options: [
        {
          icon: "mdi-target",
          key: "targets",
          click: () => {
            this.showTargets = true;
          },
        },
        {
          icon: "mdi-chart-line",
          key: "trend",
          click: () => {},
        },
        {
          icon: "mdi-list",
          key: "table",
          click: () => {},
        },
      ],
      dashboardKey: 0,
      chart: {
        configs: {},
        update: 0,
      },
    };
  },
  computed: {
    length() {
      return this.tabs.length;
    },
  },
};
</script>
