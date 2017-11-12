<template>
  <div class="app">
    <AppHeader :user="user" />
    <div class="page animsition" style="animation-duration: 800ms; opacity: 1;">
      <div>
        <router-view :user="user" @reload="load"></router-view>
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
      this.load();
    },
    computed: {
      name () {
        return this.$route.name
      },

      list () {
        return this.$route.matched
      },
    },
    methods: {
      load() {
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
      }
    }
  }
</script>

<style>
  body {
    background-color: #282D33;
  }

  .card-layout {
    padding: 30px;
  }

  .card-layout > * {
    max-width: 860px;
    padding: 0;
    margin: 0;
  }

  @media (max-width: 575px) {
    .card-layout {
      padding: 0px;
    }

    .card-layout > * {
      max-width: 100%;
    }
  }

  .btn-vacayo {
    cursor: pointer;
    -webkit-transition: background 0.3s, border-color 0.3s;
    -moz-transition: background 0.3s, border-color 0.3s;
    transition: background 0.3s, border-color 0.3s;
    position: relative;
    display: inline-block;
    text-align: center;
    text-decoration: none;
    border: 2px solid transparent;
    border-radius: 4px;
    width: auto;
    font-size: 16px;
    line-height: 22px;
    padding-top: 12px;
    padding-bottom: 12px;
    color: #ffffff;
    font-weight: 500;
    padding-right: 24px;
    padding-left: 24px;
    min-width: 80px;
    letter-spacing: 1.1px;
    background: #FF5A5F;
  }

  .btn-vacayo.sucess {
    border-color: #46be8a;
    background-color: #46be8a;
  }
</style>