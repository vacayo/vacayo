<template>
  <div class="app">
    <Navigation/>
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div class="page-header">
        <h1 class="page-title">My Properties</h1>
        <Breadcrumb/>
      </div>
      <div class="page-content">
        <router-view></router-view>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Navigation from '../components/Navigation'
import Footer from '../components/Footer'
import Breadcrumb from '../components/Breadcrumb'

export default {
  components: {
    Navigation,
    Footer,
    Breadcrumb
  },
  computed: {
    name () {
      return this.$route.name
    },

    list () {
      return this.$route.matched
    }
  }
}
</script>

<style>
</style>