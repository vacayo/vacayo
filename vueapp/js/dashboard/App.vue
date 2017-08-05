<template>
  <div class="app">
    <Navigation/>
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div class="page-header">
        <h1 class="page-title mb-10">{{ name }}</h1>
        <!--
        <Breadcrumb :list="list"/>
        -->
      </div>
      <div class="page-content">
        <router-view></router-view>
      </div>
    </div>
    <AppFooter/>
  </div>
</template>

<script type="text/babel">
  import Navigation from '../components/Navigation'
  import AppFooter from '../components/Footer'
  import Breadcrumb from '../components/Breadcrumb'

  export default {
    components: {
      Navigation,
      AppFooter,
      Breadcrumb
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