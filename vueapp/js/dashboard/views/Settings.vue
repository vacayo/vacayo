<template>

  <div class="panel nav-tabs-horizontal nav-tabs-inverse" data-plugin="nav-tabs">

    <div class="panel-heading panel-heading-tab">
      <ul class="nav nav-tabs nav-tabs-solid" role="tablist">
        <li class="nav-item">
          <router-link to="/settings/profile" class="nav-link" data-toggle="tab" href="#settings" aria-controls="superhost" role="tab" aria-expanded="true">Edit Profile</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/settings/superhost" class="nav-link" data-toggle="tab" href="#settings" aria-controls="superhost" role="tab" aria-expanded="true">Superhost Settings</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/settings/owner" class="nav-link" data-toggle="tab" href="#settings" aria-controls="superhost" role="tab" aria-expanded="true">Owner Settings</router-link>
        </li>
      </ul>
    </div>

    <div class="panel-body pt-50">
      <div class="tab-content">
        <router-view :user="user"></router-view>
      </div>

    </div>

  </div>

</template>

<script type="text/babel">
  export default {
    props: ['user'],
    methods: {
    }
  }
</script>

<style></style>
