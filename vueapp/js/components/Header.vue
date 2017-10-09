<template>
  <nav class="site-navbar navbar navbar-inverse navbar-fixed-top navbar-mega" role="navigation">

    <div class="navbar-header">
      <a class="navbar-brand navbar-brand-center" href="/">
        <img class="navbar-brand-logo navbar-brand-logo-normal" :src="logo" alt="Vacayo: Begin at Home">
      </a>
    </div>

    <div class="navbar-container container-fluid">

      <!-- Navbar Collapse -->
      <div class="collapse navbar-collapse navbar-collapse-toolbar" id="site-navbar-collapse">

        <!-- Navbar Toolbar Right -->
        <ul class="nav navbar-toolbar navbar-right navbar-toolbar-right">

          <li class="nav-item dropdown">
            <a class="nav-link" href="/host">Become a Superhost</a>
          </li>

          <li v-if="user" class="nav-item dropdown">
            <a class="nav-link" data-toggle="dropdown" href="javascript:void(0)" title="Notifications"
            aria-expanded="false" data-animation="scale-up" role="button">
              <i class="icon wb-bell" aria-hidden="true"></i>
              <span class="badge badge-pill badge-danger up">5</span>
            </a>
            <div class="dropdown-menu dropdown-menu-right dropdown-menu-media" role="menu">
              <div class="dropdown-menu-header">
                <h5>NOTIFICATIONS</h5>
                <span class="badge badge-round badge-danger">New 5</span>
              </div>
              <div class="list-group">
                <div data-role="container">
                  <div data-role="content">
                    <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                      <div class="media">
                        <div class="pr-10">
                          <i class="icon wb-order bg-red-600 white icon-circle" aria-hidden="true"></i>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">A new order has been placed</h6>
                          <time class="media-meta" datetime="2017-06-12T20:50:48+08:00">5 hours ago</time>
                        </div>
                      </div>
                    </a>
                    <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                      <div class="media">
                        <div class="pr-10">
                          <i class="icon wb-user bg-green-600 white icon-circle" aria-hidden="true"></i>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">Completed the task</h6>
                          <time class="media-meta" datetime="2017-06-11T18:29:20+08:00">2 days ago</time>
                        </div>
                      </div>
                    </a>
                    <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                      <div class="media">
                        <div class="pr-10">
                          <i class="icon wb-settings bg-red-600 white icon-circle" aria-hidden="true"></i>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">Settings updated</h6>
                          <time class="media-meta" datetime="2017-06-11T14:05:00+08:00">2 days ago</time>
                        </div>
                      </div>
                    </a>
                    <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                      <div class="media">
                        <div class="pr-10">
                          <i class="icon wb-calendar bg-blue-600 white icon-circle" aria-hidden="true"></i>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">Event started</h6>
                          <time class="media-meta" datetime="2017-06-10T13:50:18+08:00">3 days ago</time>
                        </div>
                      </div>
                    </a>
                    <a class="list-group-item dropdown-item" href="javascript:void(0)" role="menuitem">
                      <div class="media">
                        <div class="pr-10">
                          <i class="icon wb-chat bg-orange-600 white icon-circle" aria-hidden="true"></i>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">Message received</h6>
                          <time class="media-meta" datetime="2017-06-10T12:34:48+08:00">3 days ago</time>
                        </div>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
              <div class="dropdown-menu-footer">
                <a class="dropdown-menu-footer-btn" href="javascript:void(0)" role="button">
                  <i class="icon md-settings" aria-hidden="true"></i>
                </a>
                <a class="dropdown-item" href="javascript:void(0)" role="menuitem">
                    All notifications
                  </a>
              </div>
            </div>
          </li>

          <li v-if="user" class="nav-item dropdown">
            <a class="nav-link navbar-avatar" data-toggle="dropdown" href="#" aria-expanded="false"
            data-animation="scale-up" role="button">
              <span class="avatar avatar-online">
                <img src="../../img/5.jpg" alt="...">
                <i></i>
              </span>
            </a>
            <div class="dropdown-menu" role="menu">
              <router-link to="/profile" class="dropdown-item" role="menuitem">
                <i class="icon wb-user" aria-hidden="true"></i> Profile
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
