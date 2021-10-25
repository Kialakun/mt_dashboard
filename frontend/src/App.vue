<template>
  <v-app :style="{ background: $vuetify.theme.themes['light'].background }">
    <v-app-bar app dense flat color="green" dark>
      <v-tabs center-active dense slider-color="primary" dark>
        <v-tab to="/dashboard"> Dashboard </v-tab>
      </v-tabs>
      <v-spacer></v-spacer>
      <v-btn dark icon @click="$router.go(-1)"
        ><v-icon>mdi-arrow-left</v-icon></v-btn
      >
      <v-btn
        icon
        v-for="(item, i) in topRightItems"
        :key="'top-right' + i"
        @click="item.click"
      >
        <v-icon>{{ item.icon }}</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <!-- Page Loading-->
      <div v-if="loading">
        <f-spinner></f-spinner>
      </div>
      <!-- Show Page -->
      <div v-else><router-view /></div>
    </v-main>

    <!--Snackbars -->
    <v-snackbar v-model="showSnackbar" v-if="snackbar" center absolute>
      {{ snackbar.text }}
      <v-btn icon @click.native="removeSnackbar"
        ><v-icon>mdi-close</v-icon></v-btn
      >
    </v-snackbar>

    <!-- Left Navigation Drawer -->
    <v-navigation-drawer app permanent expand-on-hover color="primary" dark>
      <v-list>
        <v-list-item>
          <v-list-item-icon><v-icon>mdi-chart-bar</v-icon></v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="text-h6"> SP Berwery </v-list-item-title>
            <v-list-item-subtitle class="white--text"
              >Lae MT Dashboard</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list nav dense>
        <v-list-group
          v-for="item in navitems"
          v-model="item.active"
          :key="item.title"
          color="white"
          @click="resource = item.resource"
        >
          <template v-slot:activator>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="m in options"
            :key="item.title + '-' + m.title"
            @click="dialog[m.dialog] = true"
          >
            <v-list-item-icon
              ><v-icon>{{ m.icon }}</v-icon></v-list-item-icon
            >
            <v-list-item-title v-text="m.title"></v-list-item-title>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>

    <!-- Notifications Drawer -->
    <v-navigation-drawer right app v-model="showNotif" temporary>
      <f-notifications />
    </v-navigation-drawer>

    <!-- Dialogs -->
    <f-import-dialog
      :url="importUrl"
      :resource="resource"
      :show="dialog.import"
      @close="dialog.import = false"
    />
    <f-export-dialog
      :url="exportUrl"
      :resource="resource"
      :show="dialog.export"
      @close="dialog.export = false"
    />
    <f-user-account-dialog :show="showAccount" @close="showAccount = false" />
  </v-app>
</template>

<script>
import FExportDialog from "@/components/dialogs/ExportDialog.vue";
import FImportDialog from "@/components/dialogs/ImportDialog.vue";
import FNotifications from "@/views/Notifications.vue";
import FUserAccountDialog from "@/components/dialogs/UserAccountDialog.vue";
import FSpinner from "@/components/loading/Spinner.vue";

export default {
  name: "App",
  components: {
    FSpinner,
    FImportDialog,
    FExportDialog,
    FNotifications,
    FUserAccountDialog,
  },
  async mounted() {
    this.$store.commit("changeLoading", true);
    await this.$store.dispatch("getSchema");
    await this.$store.dispatch("getAPI");
    this.$store.commit("changeLoading", false);
  },
  computed: {
    loading() {
      return this.$store.state.http.loading;
    },
    snackbar() {
      return this.$store.state.alerts.snackbar;
    },
  },
  data() {
    return {
      showAccount: false,
      showNotif: false,
      resource: null,
      dialog: {
        import: null,
        export: null,
      },
      importUrl: null,
      exportUrl: null,
      value: null,
      options: [
        { title: "Import Data", icon: "mdi-arrow-right", dialog: "import" },
        { title: "Export Data", icon: "mdi-arrow-left", dialog: "export" },
      ],
      showSnackbar: true,
      topRightItems: [
        {
          title: "Notifications",
          icon: "mdi-bell",
          click: this.showNotification,
        },
        {
          title: "User Account",
          icon: "mdi-account-circle",
          click: this.showUserAccount,
        },
      ],
      navitems: [
        {
          title: "Safety",
          icon: "mdi-traffic-cone",
          resource: "safety",
          to: "/safety/data",
          importUrl: "",
          exportUrl: "",
          active: false,
        },
        {
          title: "Packaging",
          icon: "mdi-package",
          resource: "packaging",
          to: "/packaging/data",
          importUrl: "",
          exportUrl: "",
          active: false,
        },
        {
          title: "Brewing",
          icon: "mdi-beer",
          resource: "brewing",
          to: "/brewing/data",
          importUrl: "",
          exportUrl: "",
          active: false,
        },
        {
          title: "Quality",
          icon: "mdi-text-box-check",
          resource: "quality",
          to: "/quality/data",
          importUrl: "",
          exportUrl: "",
          active: false,
        },
        {
          title: "Logistics",
          icon: "mdi-truck-check",
          resource: "logistics",
          to: "/logistics/data",
          importUrl: "",
          exportUrl: "",
          active: false,
        },
        {
          title: "Utilities",
          icon: "mdi-engine",
          resource: "utitlities",
          to: "/utilities/data",
          importUrl: "",
          exprotUrl: "",
          active: false,
        },
      ],
    };
  },
  methods: {
    showUserAccount() {
      this.showAccount = true;
    },
    showNotification() {
      this.showNotif = true;
    },
    removeSnackbar() {
      this.$store.dispatch("removeSnackbar");
    },
  },
};
</script>

<style>
.all-caps {
  text-transform: uppercase;
}
.titlize {
  text-transform: capitalize;
}
</style>
