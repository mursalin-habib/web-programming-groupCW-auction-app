<template>
  <div class="container mt-3">
    <b-card>
      <b-card-title><h4>Add Item</h4></b-card-title>
      <b-card-body>
        <b-form @submit="addItem" enctype="multipart/form-data">
          <div class="row">
            <b-form-group
                id="input-group-1"
                label="Title"
                label-for="input-1"
                class="col-6"
            >
              <b-form-input
                  id="input-1"
                  v-model="title"
                  placeholder="Enter Title"
                  required
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-2" label="Description" label-for="input-2" class="col-6">
              <b-form-input
                  id="input-2"
                  v-model="description"
                  placeholder="Enter Description"
                  required
              ></b-form-input>
            </b-form-group>
          </div>
          <div class="row">
            <b-form-group id="input-group-2" label="Starting Price" label-for="input-2" class="col-6">
              <b-form-input
                  id="input-2"
                  v-model="starting_price"
                  placeholder="Enter Starting Price"
                  required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="End Date" label-for="input-2" class="col-6">
              <b-form-datepicker id="example-datepicker" v-model="finish_date" class="mb-2"
                                 required></b-form-datepicker>
            </b-form-group>
          </div>
          <b-form-group id="input-group-2" label="Profile Image" label-for="input-2" class="mt-3">
            <b-form-file v-model="image" @change="uploadImage" required></b-form-file>
          </b-form-group>
          <div class="row mt-3">
            <b-button type="submit" variant="primary">Add</b-button>
          </div>
        </b-form>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddItem",
  data() {
    return {
      user: {},
      image: null,
      title: null,
      description: null,
      starting_price: 0,
      finish_date: null,
      display_image: ""
    }

  },
  methods: {
    getUser() {
      axios
          .get("http://127.0.0.1:8000/logged_in_user/")
          .then((response) => {
            // console.log(response.data)
            this.user = response.data
            this.display_image = "http://127.0.0.1:8000/media/" + this.user['image']
          })
          .catch((error) => {
            console.log(error);
          });
    },
    uploadImage(e) {
      console.log(e.target.files[0])
      this.image = e.target.files[0]
    },
    addItem() {
      event.preventDefault()
      console.log(this.image)
      let formData = new FormData();
      if (this.image !== null) {
        formData.append('image', this.image);
      }
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('starting_bid', this.starting_price);
      formData.append('finish_date', this.finish_date);
      formData.append('user', this.user.id);
      // this.user['image'] = this.image.name

      axios
          .post("http://127.0.0.1:8000/api/items/", formData, {headers: {'Content-Type': 'multipart/form-data'}})
          .then((response) => {
            // console.log(response.data)
            this.$router.replace('/item-list')
            this.user = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
  },
  mounted() {
    this.getUser()
  }
}
</script>

<style scoped>

</style>