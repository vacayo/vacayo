<template>
  <header>
    <navbar />
    <sidebar />
  </header>
</template>

<script>
import navbar from './Navbar'
import sidebar from './Sidebar'
import { dropdown } from 'vue-strap'
export default {
  name: 'header',
  components: {
    navbar,
    sidebar,
    dropdown
  },
  methods: {
    click () {
      // do nothing
    },
    sidebarToggle (e) {
      e.preventDefault()
      document.body.classList.toggle('sidebar-hidden')
    },
    sidebarMinimize (e) {
      e.preventDefault()
      document.body.classList.toggle('sidebar-minimized')
    },
    mobileSidebarToggle (e) {
      e.preventDefault()
      document.body.classList.toggle('sidebar-mobile-show')
    },
    asideToggle (e) {
      e.preventDefault()
      document.body.classList.toggle('aside-menu-hidden')
    }
  }
}
</script>
