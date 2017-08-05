<template>
  <div class="site-menubar">
    <div class="site-menubar-body">
      <div>
        <div>
          <ul class="site-menu" data-plugin="menu">
            <li class="site-menu-category">Menu</li>
            <li class="site-menu-item">
              <router-link to="/properties">
                <i class="site-menu-icon fa-home fa-lg" aria-hidden="true"></i>
                <span class="site-menu-title">Properties</span>
              </router-link>
            </li>
            <li class="site-menu-category">Coming Soon</li>
            <li class="site-menu-item">
              <router-link to="/maintenance">
                <i class="site-menu-icon fa-wrench fa-lg" aria-hidden="true"></i>
                <span class="site-menu-title">Maintenance</span>
              </router-link>
            </li>
            <li class="site-menu-item">
              <router-link to="/statements">
                <i class="site-menu-icon fa-list-alt fa-lg" aria-hidden="true"></i>
                <span class="site-menu-title">Statements</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="site-menubar-footer">
      <a class="fold-show" data-placement="top" data-toggle="tooltip" data-original-title="Contact Us" href="https://homes.vacayo.com/support-vacayo/">
        <span class="icon fa-phone" aria-hidden="true"></span>
      </a>
      <a href="https://homes.vacayo.com/support-vacayo/">
        <span>Contact Us</span>
      </a>
      <a href="https://homes.vacayo.com/support-vacayo/">
      </a>
    </div>
  </div>
</template>

<script type="text/babel">
  export default {
  }
</script>

<style lang="css">
  .nav-link {
    cursor:pointer;
  }
</style>
