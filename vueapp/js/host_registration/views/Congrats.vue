<template>
  <div class="card card-shadow text-center">
    <div class="panel">
      <div class="panel-body text-justify">
        <p>Congrats!</p>
      </div>
      <div class="panel-footer">
        <button type="button" class="btn" @click="settings">
          <span>My Settings!</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
  export default {
    props: ['user'],
    methods: {
      settings() {
        window.location.href = '/dashboard#/settings/superhost';
      }
    }
  }
</script>

<style></style>
