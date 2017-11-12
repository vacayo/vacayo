<template>
  <div class="app">
    <AppHeader :user="user" />
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div>
        <router-view :user="user"></router-view>
      </div>
    </div>
    <AppFooter/>
  </div>
</template>

<script type="text/babel">
  import AppHeader from '../components/Header'
  import AppFooter from '../components/Footer'

  export default {
    components: {
      AppHeader,
      AppFooter
    },
    data() {
      return {
        user: null
      }
    },
    created: function() {
      let url  = '/api/user';
      let options = {
        method: "GET",
        credentials: 'same-origin',
        headers: new Headers({
          'Content-Type': 'application/json'
        })
      };

      fetch(url, options)
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
</style>