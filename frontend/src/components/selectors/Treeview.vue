<template>
  <div>
    <v-treeview
      hoverable
      rounded
      :items="treeItems"
      dense
      activatable
      open-on-click
    >
      <template v-slot:label="{ item }">
        <v-row>
          <v-col>
            <span class="font-weight-bold">{{ item.name }}</span>
            <span class="float-right">{{ item.value }}</span>
          </v-col>
          <v-col v-if="item.status">
            <v-progress-linear
              v-model="item.status"
              rounded
              color="blue lighten-2"
              height="20"
            >
              <template v-slot:default="{ value }">
                <strong>{{ Math.ceil(value) }}%</strong>
              </template>
            </v-progress-linear>
          </v-col>
        </v-row>
      </template>
      <template v-slot:append="{ item }">
        <div v-if="item.level === 0">
          <v-btn icon @click="edit(api[item.id])"
            ><v-icon>mdi-pencil</v-icon></v-btn
          >
          <v-btn icon @click="deleteItem(item)"
            ><v-icon>mdi-delete</v-icon></v-btn
          >
        </div>
      </template>
    </v-treeview>
  </div>
</template>

<script>
export default {
  name: "FTreeview",
  props: ["resource"],
  computed: {
    schema() {
      return this.$store.state.model.schema[this.resource];
    },
    api() {
      return this.$store.state.api[this.resource];
    },
    treeItems() {
      const api = this.api;
      const schema = this.schema;
      let weeks = [];
      let schemaCount = this.getSchemaCount(schema);
      for (const n in api) {
        // get a n item from _items api
        const item = api[n];
        const childItems = this.convert(schema, item);
        let docCount = this.getStatusCount(item);
        console.log("Total schema count", schemaCount);
        console.log("Total doc count", docCount);
        weeks.push({
          name: "Week " + item.date.week,
          children: childItems,
          level: 0,
          id: n,
          etag: item._etag,
          status: (docCount / schemaCount) * 100,
        });
      }
      return weeks;
    },
  },
  methods: {
    async deleteItem(item) {
      const url = "/api/" + this.resource + "/" + item.id;
      const resp = await this.$store.dispatch("httpDELETE", {
        url: url,
        etag: item.etag,
      });
      console.log(resp);
    },
    hasChild(item) {
      if (Object.keys(item).length > 0) {
        // check if has keys
        if (!(parseInt(Object.keys(item)[0]) === 0)) {
          // check if keys not eqial to integer 0
          // this shows item is either an array or string and not object
          // only objects get true
          return true;
        }
      }
      return false;
    },
    getSchemaCount(item) {
      let count = 0;
      for (const field in item) {
        if (item[field].type === "dict") {
          count += this.getSchemaCount(item[field].schema);
        } else {
          count++;
        }
      }
      return count;
    },
    getStatusCount(item) {
      let count = 0;
      for (const field in item) {
        if (field.startsWith("_")) {
          continue;
        } else if (this.hasChild(item[field])) {
          count += this.getStatusCount(item[field]);
        } else {
          count++;
        }
      }
      return count;
    },
    edit(item) {
      this.$store.commit("selectItem", item);
      this.$router.push("/" + this.resource + "/form");
    },
    convert(schema, item) {
      let items = [];
      let data = {};
      for (const field in schema) {
        // field "_id" does not have meta, so we skip it
        if (field === "_id") {
          continue;
        }
        // set the data object
        data = { name: schema[field].meta.verbose_name, children: [] };
        if (!(field in item)) {
          // field is not in the api record
          data.value = "----";
        } else {
          if (schema[field].type === "dict") {
            data.value = item[field]._total;
            data.children = this.convert(schema[field].schema, item[field]);
          } else {
            // field isnt in the api record
            data.value = item[field];
          }
        }
        items.push(data);
      }
      return items;
    },
  },
};
</script>
