<template>
  <div class="app">
    <AppHeader/>
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div class="page-header">
        <h1 class="page-title mb-10">Manage Properties on Vacayo</h1>
      </div>
      <div class="page-content">
        <router-view></router-view>
      </div>
    </div>
    <AppFooter/>
  </div>
</template>

<script type="text/babel">
  import AppHeader from '../components/Header2'
  import AppFooter from '../components/Footer'

  export default {
    components: {
      AppHeader,
      AppFooter
    },
    computed: {
      name () {
        return this.$route.name
      },

      list () {
        return this.$route.matched
      },
    }
  }
</script>

<style>
</style>