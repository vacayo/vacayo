<template>
  <div class="site-menubar">
    <div class="site-menubar-body">
      <div>
        <div>
          <ul class="site-menu" data-plugin="menu">
            <li class="site-menu-category">Menu</li>
            <li class="site-menu-item">
              <router-link to="/properties">
                <i class="site-menu-icon fa-home" aria-hidden="true"></i>
                <span class="site-menu-title">Properties</span>
              </router-link>
            </li>
            <li class="site-menu-item">
              <router-link to="/maintenance">
                <i class="site-menu-icon fa-wrench" aria-hidden="true"></i>
                <span class="site-menu-title">Maintenance</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="site-menubar-footer">
      <router-link to="/contact" class="fold-show" data-placement="top" data-toggle="tooltip" data-original-title="Contact Us">
        <span class="icon fa-phone" aria-hidden="true"></span>
      </router-link>
      <router-link to="/contact">
        <span>Contact Us</span>
      </router-link>
      <router-link to="/contact">
      </router-link>
    </div>
  </div>
</template>
<script>
export default {
  name: 'sidebar',
  methods: {
    handleClick (e) {
      e.preventDefault()
      e.target.parentElement.classList.toggle('open')
    }
  }
}
</script>

<style lang="css">
  .nav-link {
    cursor:pointer;
  }
</style>
