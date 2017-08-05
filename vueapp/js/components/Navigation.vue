<template>
  <header>
    <navbar />
    <sidebar />
  </header>
</template>

<script type="text/babel">
  import navbar from './Navbar'
  import sidebar from './Sidebar'
  import { dropdown } from 'vue-strap'

  export default {
    components: {
      navbar,
      sidebar,
      dropdown
    }
  }
</script>
