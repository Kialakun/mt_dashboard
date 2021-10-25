<template>
  <div id="table-dialogs">
    <!-- Settings -->
    <v-dialog
      v-model="dialog.settings.show"
      persistent
      :overlay="false"
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title> Table Settings </v-card-title>
        <v-card-subtitle> Edit table settings below. </v-card-subtitle>
        <v-card-text>
          <v-list subheader>
            <v-subheader>Show Fields</v-subheader>
            <v-list-item v-for="header in headers" :key="header.value">
              <v-checkbox
                :label="header.text"
                v-model="post.headers"
                :value="header"
              ></v-checkbox>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text>Save</v-btn>
          <v-btn color="grey" text @click="dialog.settings.show = false"
            >Close</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!--Export Dialog -->
    <v-dialog
      v-model="dialog.export.show"
      persistent
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title>Export Items</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text>Export</v-btn>
          <v-btn color="grey" text>Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Import Diaog -->
    <v-dialog
      v-model="dialog.import.show"
      persistent
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title> Import Items </v-card-title>
        <v-card-actions>
          <v-btn text color="success">Confirm</v-btn>
          <v-btn text color="success" @click="closeAllDialogs">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Delete Dialog -->
    <v-dialog
      v-model="dialog.delete.show"
      persistent
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title> Delete Item </v-card-title>
        <v-card-text>
          <p class="font-weight-bold">Record ID: {{ recordID }}</p>
          <p>Are you sure you want to delete item?</p>
          <p class="red--text">WARNING!: This is a non-reversible action.</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="success" @click="deleteItem(item)">Confirm</v-btn>
          <v-btn text @click="closeAllDialogs">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Edit Dialog -->
    <v-dialog
      v-model="dialog.edit.show"
      persistent
      max-width="600px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title>Edit Item</v-card-title>
        <v-card-text>
          <p>
            Record ID: {{ recordID }} <br />
            Created: {{ dateCreated }} <br />
            Last Updated: {{ lastUpdated }}
          </p>
          <v-form>
            <v-list v-if="!dialog.edit.edit" two-line>
              <div v-for="(value, key) in item" :key="key">
                <v-list-item v-if="hasVerboseName(key)">
                  <v-list-item-content>
                    <v-list-item-title>{{ value }}</v-list-item-title>
                    <v-list-item-subtitle>{{
                      fields[key].meta.verbose_name
                    }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </div>
            </v-list>
            <f-fields
              v-if="dialog.edit.edit"
              :fields="fields"
              :item="item"
              :errs="errors"
            />
          </v-form>
          <details v-if="dialog.edit.edit">
            <p>{{ postUrl }} {{ post }}</p>
          </details>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="secondary" @click="submit">Submit</v-btn>
          <v-btn text @click="() => (dialog.edit.edit = !dialog.edit.edit)">
            {{ dialog.edit.edit ? "Close Edit" : "Edit" }}
          </v-btn>
          <v-btn
            text
            color="red"
            @click="
              () => {
                dialog.edit.show = false;
                dialog.delete.show = true;
              }
            "
            >Delete</v-btn
          >
          <v-btn text color="grey" @click="closeAllDialogs">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Create Dialog -->
    <v-dialog
      v-model="dialog.create.show"
      persistent
      max-width="600px"
      transition="dialog-transition"
    >
      <v-card>
        <v-card-title>New Item</v-card-title>
        <v-card-subtitle>Please fill in the following form:</v-card-subtitle>
        <v-card-text>
          <p>{{ fields }}</p>
          <v-form>
            <f-fields :fields="fields" :errs="errors" />
          </v-form>
          <details>
            <p>{{ postUrl }} {{ post }}</p>
          </details>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="secondary" @click="submit">Submit</v-btn>
          <v-btn text color="grey" @click="closeAllDialogs">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import FFields from "@/components/forms/Fields.vue";

export default {
  name: "FTableDialogs",

  props: ["collection", "show", "item", "headers", "fields"],

  components: {
    "f-fields": FFields,
  },

  computed: {
    post: {
      get() {
        return this.$store.state.http.data;
      },

      set(data) {
        this.$store.dispatch("updateHttpData", data);
      },
    },

    dateCreated() {
      return this.item ? this.item._created : "";
    },

    lastUpdated() {
      return this.item ? this.item._updated : "";
    },

    recordID() {
      return this.item ? this.item._id : "No ID!";
    },

    postUrl() {
      return "/api/" + this.collection;
    },
  },

  data: () => {
    return {
      counter: 0,
      errors: {},
      dialog: {
        create: { show: false },
        edit: { show: false, edit: false },
        delete: { show: false },
        import: { show: false },
        export: { show: false },
        settings: { show: false },
      },
    };
  },

  methods: {
    hasVerboseName(key) {
      if (Object.hasOwn(this.fields, key)) {
        if (Object.hasOwn(this.fields[key], "meta")) {
          if (Object.hasOwn(this.fields[key].meta, "verbose_name")) {
            return true;
          }
        }
      } else {
        return false;
      }
    },

    async deleteItem(item) {
      var url = this.postUrl + "/" + item._id;
      const resp = await this.$store.dispatch("httpDELETE", {
        url: url,
        etag: item._etag,
      });
      console.log("item deleted", resp);
    },

    closeAllDialogs() {
      for (const key in this.dialog) {
        if (key in this.dialog) {
          this.dialog[key].show = false;
        }
      }
      this.counter++;
      this.$emit("close");
    },

    resetPostData() {
      this.post = {};
    },

    async submit() {
      const data = this.post;

      if (this.show === "edit") {
        const url = this.postUrl + "/" + this.item._id;
        const resp = await this.$store.dispatch("httpPUT", {
          url: url,
          data: data,
          etag: this.item._etag,
        });

        if (resp._status !== "OK") {
          this.errors = resp._issues;
          console.log("Err: HTTP PUT -> ", url, resp);
          return;
        }

        this.resetPostData();
        this.closeAllDialogs();
        return;
      }

      console.log("post data", data);
      console.log("post url -> ", this.postUrl);

      const resp = await this.$store.dispatch("httpPOST", {
        url: this.postUrl,
        data: data,
      });

      if (resp._status !== "OK") {
        this.errors = resp._issues;
        console.log("Err: HTTP POST -> ", this.postUrl, resp);
        return;
      }

      this.resetPostData();
      this.closeAllDialogs();
      return;
    },
  },

  watch: {
    $route() {
      console.log("Route changed refreshing data...");
      this.post = {};
    },

    show() {
      if (this.show) {
        this.dialog[this.show].show = true;
      }
    },

    counter() {
      this.$emit("refresh");
    },
  },
};
</script>
