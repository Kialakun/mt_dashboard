<template>
  <v-dialog
    v-model="dialog"
    scrollable
    persistent
    max-width="800px"
    transition="dialog-transition"
  >
    <v-window v-model="window" reverse mandatory>
        <v-window-item key="default">
            <v-card>
            <v-card-title> <v-icon class="mr-2">mdi-target</v-icon> Targets </v-card-title>
            <v-card-text>
                <p>Set or update targets here:</p>
                <v-toolbar dense flat>
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="activateWindow({}, 3)">Add Target</v-btn>
                </v-toolbar>
                <v-data-table
                    :headers="headers"
                    :items="items"
                    item-key="_id"
                    :loading="loading"
                    :search="search"
                >
                <template v-slot:item.actions="{ item }">
                    <v-btn text @click="activateWindow(item, 2)"><v-icon>mdi-pencil</v-icon></v-btn>
                    <v-btn icon @click="activateWindow(item, 1)"><v-icon>mdi-delete</v-icon></v-btn>
                </template>
                </v-data-table>
            </v-card-text>
            </v-card>
        </v-window-item>
        <v-window-item key="delete">
            <v-card>
                <v-card-title>
                   <v-icone>mdi-delete</v-icon> Delete Target
                </v-card-title>
                <v-card-text>
                    <p>
                        Are you sure you want to delete this item?
                    </p>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text @click="activateWindow({}, 0)">Cancel</v-btn>
                    <v-btn text color="error" @click="deleteItem">Delete</v-btn>
                </v-card-actions>
            </v-card>
        </v-window-item>
        <v-window-item key="edit">
            <v-card>
                <v-card-title>
                  <v-icon>mdi-pencil</v-icon>  Edit Target
                </v-card-title>
                <v-card-text>
                    <p>Edit target.</p>
                    <f-fields :fields="schema" :editItem="selectedItem"></f-fields>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text @click="activateWindow({}, 0)">Cancel</v-btn>
                    <v-btn text color="success" @click="editItem">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-window-item>
        <v-window-item key="new">
            <v-card>
                <v-card-title>
                  <v-icon>mdi-plus</v-icon>  New Target
                </v-card-title>
                <v-card-text>
                    <p>Add a target.</p>
                    <v-form>
                        <f-fields :fields="schema" @change="(data) => body = data"></f-fields>
                    </v-form>                    
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text @click="activateWindow({}, 0)">Cancel</v-btn>
                    <v-btn text color="success" @click="saveNew">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-window-item>
      </v-window>
  </v-dialog>
</template>

<script>
import FFields from "@/components/forms/Fields.vue"
export default {
  name: "FTargetsDialog",
  props: ["show"],
  components: {
      FFields
  },
  computed: {
    headers() {
        var headers = []
        for (const fieldName in this.schema) {
            if (fieldName.startsWith("_")) {
                continue
            }
            headers.push({text: this.schema[fieldName].meta.verbose_name, value: fieldName})
        }
        headers.push({text: "Actions", value: "actions"})
        return headers
    },
    items() {
        return this.$store.state.api.targets
    },
    schema() {
        return this.$store.state.model.schema.targets
    },
    dialog: {
      get() {
        return this.show;
      },
      set() {
        return this.$emit("close");
      },
    },
  },
  data() {
      return {
          body: {},
          selectedItem: null,
          window: 0,
          loading: false,
          search: null,
          form: {}
      }
  },
  methods: {
      editItem() {
          const url = "/api/targets/" + this.selectedItem._id
          const etag = this.selectedItem._etag
          const data = this.body
          this.$store.dispatch("httpPATCH", {url, data, etag})
      },
      deleteItem() {
          const url = "/api/targets/" + this.selectedItem._id
          const etag = this.selectedItem._etag
          this.$store.dispatch("httpDELETE", {url, etag})
      },
      saveNew() {
          const url = "/api/targets"
          const data = this.body
          this.$store.dispatch("httpPOST", {url, data})
      },
      activateWindow(item, window) {
          this.selectedItem = item
          this.window = window
      }
  },
};
</script>
