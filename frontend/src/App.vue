<template>
  <div id="app">
    <nav-bar></nav-bar>
<!--    <nav>-->
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link>-->
<!--    </nav>-->
    <router-view/>
  </div>
</template>

<style>

</style>
<script>
import NavBar from "@/components/NavBar";
export default {
  components: {NavBar}
}
</script>