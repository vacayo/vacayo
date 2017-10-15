<template>
  <nav class="site-navbar navbar navbar-inverse navbar-fixed-top navbar-mega" role="navigation">

    <div class="navbar-header">
      <div data-toggle="gridmenu" class="navbar-brand navbar-brand-center site-gridmenu-toggle">
        <a href="/"><img :src="logo" alt="Vacayo: Begin at Home" title="Vacayo" class="navbar-brand-logo navbar-brand-logo-normal"></a>
      </div>

      <button type="button" data-toggle="collapse" class="navbar-toggler hamburger hamburger-close navbar-toggler-left unfolded hided" data-target="#site-navbar-collapse" aria-expanded="true">
        <span class="sr-only">Toggle navigation</span>
        <span class="hamburger-bar"></span>
      </button>

    </div>

    <div class="navbar-container container-fluid">

      <!-- Navbar Collapse -->
      <div class="collapse navbar-collapse navbar-collapse-toolbar" id="site-navbar-collapse">

        <!-- Navbar Toolbar Right -->
        <ul class="nav navbar-toolbar navbar-right navbar-toolbar-right">

          <li v-if="!user" class="nav-item dropdown">
            <a class="nav-link" href="/accounts/login/">Sign In</a>
          </li>

          <li v-if="!user" class="nav-item dropdown">
            <a class="nav-link" href="/accounts/signup/">Sign Up</a>
          </li>

          <li v-if="user && !user.host" class="nav-item dropdown">
            <a class="nav-link" href="/host">Become a Superhost</a>
          </li>

          <li v-if="user" class="nav-item dropdown">
            <a href="/dashboard#/properties" class="nav-link">My Properties</a>
          </li>

          <li v-if="user" class="nav-item dropdown" id="avatar">
            <a class="nav-link navbar-avatar" data-toggle="dropdown" href="#" aria-expanded="false"
            data-animation="scale-up" role="button">
              <span class="avatar avatar-online">
                <img src="../../img/5.jpg" alt="...">
                <i></i>
              </span>
            </a>
            <div class="dropdown-menu" role="menu">
              <router-link to="/settings/profile" class="dropdown-item" role="menuitem">
                <i class="icon wb-user" aria-hidden="true"></i> Edit Profile
              </router-link>
              <router-link v-if="user.host" to="/settings/superhost" class="dropdown-item" role="menuitem">
                <i class="icon wb-settings" aria-hidden="true"></i> Superhost Settings
              </router-link>
              <a href="/accounts/password/change/" class="dropdown-item" role="menuitem">
                <i class="icon wb-lock" aria-hidden="true"></i> Change Password
              </a>
              <div class="dropdown-divider" role="presentation"></div>
              <a class="dropdown-item" href="/accounts/logout/" role="menuitem"><i class="icon wb-power" aria-hidden="true"></i> Logout</a>
            </div>
          </li>

        </ul>

      </div>

    </div>

  </nav>
</template>

<script type="text/babel">
  import logo from '../../img/logo.png'

  export default {
    props: ['user'],
    data() {
      return {
        logo: logo
      }
    },
  }
</script>

<style>
.navbar-inverse {
  background-color: #282D33;
}

</style>
