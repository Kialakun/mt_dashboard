<template>
  <v-container fluid pa-0>
    <v-list>
      <v-list-item>
        <v-list-item-icon><v-icon>mdi-bell</v-icon></v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="text-h6"> Notifications </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list dense three-line>
      <v-list-item
        v-for="(notification, i) in notifications"
        :key="notification.user + '-notification-' + i"
      >
        <v-list-item-content>
          <v-list-item-title>{{ notification.user }}</v-list-item-title>
          <p>
            {{ notification.message }}
          </p>
          <p class="font-italic">
            {{ notification.timestamp }}
          </p>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
export default {
  name: "FNavigation",
  props: ["show"],
  computed: {
    showNotif: {
      get() {
        return this.show;
      },
      set() {
        this.$emit("close");
      },
    },
    notifications() {
      if (!this.$store.state.api.notifications) {
        return [
          { user: "No Notifications", timestamp: "Now", message: "None" },
        ];
      }
      return this.$store.state.api.notifications;
    },
  },
};
</script>
