<template>
  <div class="container">
    <b-card>
      <b-card-title><h4>Profile</h4></b-card-title>
      <b-card-body>
        <div class="row">
          <b-form @submit="updateUser" enctype="multipart/form-data">
            <div class="row">
              <b-form-group
                  id="input-group-1"
                  label="Email address:"
                  label-for="input-1"
                  class="col-5"
              >
                <b-form-input
                    id="input-1"
                    v-model="user.email"
                    type="email"
                    placeholder="Enter a valid email address"
                    required
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Your City:" label-for="input-2" class="col-5">
                <b-form-input
                    id="input-2"
                    v-model="user.city"
                    placeholder="Enter city name"
                    required
                ></b-form-input>
              </b-form-group>
            </div>
            <b-form-group id="input-group-2" label="Date of Birth:" label-for="input-2" class="col-6">
              <b-form-datepicker id="example-datepicker" v-model="user.dob" class="mb-2"></b-form-datepicker>
            </b-form-group>
            <b-form-group id="input-group-2" label=" Current Profile Picture" label-for="input-2" class="mt-5">
              <b-avatar variant="info" :src="display_image"></b-avatar>
              <b-form-file v-model="image" @change="uploadImage"></b-form-file>
            </b-form-group>
            <div class="row mt-3">
              <b-button type="submit" variant="primary">Update</b-button>
            </div>
          </b-form>
        </div>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  data() {
    return {
      user: {},
      image: null,
      display_image: ""
    }

  },
  methods: {
    uploadImage(e) {
      console.log(e.target.files[0])
      this.image = e.target.files[0]
    },
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
    updateUser() {
      event.preventDefault()
      console.log(this.image)
      let formData = new FormData();
      if (this.image !== null) {
        formData.append('image', this.image);
      }
      formData.append('email', this.user.email);
      formData.append('city', this.user.city);
      formData.append('dob', this.user.dob);
      // this.user['image'] = this.image.name

      axios
          .patch("http://127.0.0.1:8000/user/update/" + this.user.id + "/", formData, {headers: {'Content-Type': 'multipart/form-data'}})
          .then((response) => {
            // console.log(response.data)
            this.user = response.data
            this.getUser()
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