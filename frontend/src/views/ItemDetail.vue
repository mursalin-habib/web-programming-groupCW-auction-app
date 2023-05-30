<template>
  <div class="container mt-3">
    <b-card  :img-src="selectItem.image" img-alt="Image" img-height="400" img-width="200" img-top>
      <b-card-text>
        {{ selectItem.title }}
        <p>{{ selectItem.description }}</p>
        <p>Price: {{ item.starting_bid }}</p>
        <b-form-input
            id="input-2"
            v-model="price"
            placeholder="Enter Starting Price"
            required
            class="col-3"
            :disabled="disableBid"
        ></b-form-input>

      </b-card-text>
      <p style="color: #42b983">{{ bidWinnerLine }}</p>
      <p style="color: red">{{ error }}</p>
      <template #footer>
        <b-btn class="btn-primary" @click="updateItem" :disabled="disableBid">Bid</b-btn>
      </template>
    </b-card>
    <comment-view></comment-view>
  </div>
</template>

<script>
import axios from "axios";
import CommentView from "@/views/CommentView";

export default {
  name: "ItemDetail",
  components: {CommentView},
  data() {
    return {
      selectItem: {},
      item: {},
      disableBid: false,
      user: {},
      bidWinnerLine: null,
      error: "",
      price: 0
    }
  },
  methods: {
    getUser() {
      axios
          .get("http://127.0.0.1:8000/logged_in_user/")
          .then((response) => {
            // console.log(response.data)
            this.user = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
    getItems() {
      axios
          .get("http://127.0.0.1:8000/api/items/" + this.$router.history.current.params.id)
          .then((response) => {
            // console.log(response.data)
            this.selectItem = response.data
            this.item = response.data
            this.price = this.selectItem.starting_bid
            var bidDate = new Date(this.selectItem.finish_date)
            var recentDate = new Date()
            console.log(bidDate)
            if (bidDate.getMonth() === recentDate.getMonth() && bidDate.getDate() < recentDate.getDate()) {
              this.disableBid = true
              if (this.user.id === this.item.user) {
                this.bidWinnerLine = "Configurations you win the Bid"
              }
            }
          })
          .catch((error) => {
            console.log(error);
          });
    },
    updateItem() {

      this.error = null
      console.log(this.item.starting_bid)
      console.log(this.price)
      if (parseFloat(this.item.starting_bid) >= parseFloat(this.price)) {
        this.error = "The bid price must be higher than previous bid price"

      } else {
        this.selectItem.starting_bid = this.price
        delete this.item.image
        axios
            .patch("http://127.0.0.1:8000/api/items/" + this.item.id + "/", this.selectItem, {headers: {'Content-Type': 'multipart/form-data'}})
            .then((response) => {
              // console.log(response.data)
              this.selectItem = response.data
              this.item = response.data
            })
            .catch((error) => {
              console.log(error);
            });
      }
    }
  },
  mounted() {
    this.getUser()
    console.log(this.$router.history.current.params.id)
    this.getItems()
  }
}
</script>

<style scoped>

</style>