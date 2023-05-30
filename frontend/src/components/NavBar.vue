<template>
  <b-navbar toggleable="lg" type="light" variant="light">
<!--    <b-navbar-brand href="#">NavBar</b-navbar-brand>-->

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="{name:'add-item'}">
          <div class="btn-primary">Add Item</div>
        </b-nav-item>
        <b-nav-item :to="{name:'item-list'}">
          <div class="btn-primary">Item List</div>
        </b-nav-item>
        <b-nav-item :to="{name:'profile'}">Profile</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
    <b-btn class="offset-9" @click="logout">Logout</b-btn>
  </b-navbar>
</template>

<script>
import axios from "axios";

export default {
  name: "NavBar",
  methods: {
    logout() {
      this.$cookies.remove("csrftoken")
      this.$cookies.remove("sessionid")
      axios
          .get("http://127.0.0.1:8000/logout/")
          .then((response) => {
            console.log(response)
            this.$router.replace('/login/')
            window.location.reload();
          })
          .catch((error) => {
            console.log(error);
          });
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>