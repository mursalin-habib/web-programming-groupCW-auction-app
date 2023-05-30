<template>
  <div class="container mt-3">
    <div class="row">
      <div class="col-6">
        <label for="input-live"><b>Search Item</b></label>
        <b-form-input
            id="input-live"
            v-model="search_value"
            aria-describedby="input-live-help input-live-feedback"
            placeholder="Enter your keyword"
            trim
            class="col-5"
            @input="searchingValueChanged"
        ></b-form-input>
      </div>
    </div>
    <b-card-group deck class="mt-3">
      <div class="row">
        <div v-if="items.length===0">
          <p>Item are not Available</p>
        </div>
        <div v-else class="row">
          <div v-for="item in items" :key="item.id" class="col-3">
            <b-card title="Title" :img-src="item.image" img-alt="Image" img-width="150" img-height="200" img-top>
              <b-card-text>
                {{ item.title }}
                <p>{{ item.description }}</p>
                <p>Price: {{ item.starting_bid }}</p>

              </b-card-text>
              <template #footer>
                <b-btn class="btn-primary" @click="detail(item)">Detail</b-btn>
              </template>
            </b-card>
          </div>
        </div>
      </div>
    </b-card-group>

    <b-modal v-model="modalShow">
      <b-card title="Title" :img-src="selectItem.image" img-alt="Image" img-top>
        <b-card-text>
          {{ selectItem.title }}
          <p>{{ selectItem.description }}</p>
          <p>Price: {{ selectItem.starting_bid }}</p>
          <b-form-input
              id="input-2"
              v-model="selectItem.starting_bid"
              placeholder="Enter Starting Price"
              required
              class="col-3"
          ></b-form-input>

        </b-card-text>
        <template #footer>
          <b-btn class="btn-primary" @click="updateItem">Detail</b-btn>
        </template>
      </b-card>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ItemList",
  data() {
    return {
      items: {},
      modalShow: false,
      selectItem: {},
      search_value: ""
    }

  },
  methods: {
    getItems() {
      axios
          .get("http://127.0.0.1:8000/api/items/?title__icontains=" + this.search_value)
          .then((response) => {
            // console.log(response.data)
            this.items = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
    detail(item) {
      // router.push({path: 'detail/', params: {id: item.id}, query: {id: item.id}})
      // this.$router.push({path: 'detail/', params: {id: item.id}, query: {id: item.id}})
      this.$router.replace('/item-list/detail/' + item.id)
      // console.log(item)
      // this.selectItem = item
      // this.modalShow = true
    },
    updateItem() {
      delete this.selectItem.image
      axios
          .patch("http://127.0.0.1:8000/api/items/" + this.selectItem.id + "/", this.selectItem, {headers: {'Content-Type': 'multipart/form-data'}})
          .then((response) => {
            // console.log(response.data)
            this.user = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
    searchingValueChanged() {
      this.getItems()
    }
  },
  mounted() {
    this.getItems()
  }
}
</script>

<style scoped>

</style>