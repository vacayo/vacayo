<template>
  <div class="app">
    <AppHeader :user="user" />
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div class="page-header container">
        <h1 class="page-title mb-10">{{ name }}</h1>
        <!--
        <Breadcrumb :list="list"/>
        -->
      </div>
      <div class="page-content container">
        <router-view :user="user"></router-view>
      </div>
    </div>
    <AppFooter/>
  </div>
</template>

<script type="text/babel">
  import AppHeader from '../components/Header'
  import AppFooter from '../components/Footer'
  import Breadcrumb from '../components/Breadcrumb'

  export default {
    components: {
      AppHeader,
      AppFooter,
      Breadcrumb
    },
    data() {
      return {
        user: {}
      }
    },
    created: function() {
      let options = {
        credentials: 'same-origin',
      };

      fetch('/api/user/', options)
        .then(
          response => response.json(),
          error => console.log('An error occurred creating your host account:', error)
        )
        .then(
          json => this.user = json.results.user
        )
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
  body {
    background-color: #282D33;
  }
  .page {
    min-height: 670px;
  }
</style>