<template>
  <form class="form-horizontal">
    <div class="form-group row">
      <label class="col-sm-2 form-control-label">First Name: </label>
      <div class="col-sm-10">
        <input type="text" class="form-control" name="first_name" placeholder="First Name" autocomplete="off" :value="user.first_name">
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-2 form-control-label">Last Name: </label>
      <div class="col-sm-10">
        <input type="text" class="form-control" name="last_name" placeholder="Last Name" autocomplete="off" :value="user.last_name">
      </div>
    </div>

    <div class="form-group row">
      <div class="col-sm-10 col-sm-offset-2">
        <button type="button" class="btn btn-primary">Save</button>
      </div>
    </div>

  </form>
</template>

<script type="text/babel">
  export default {
    data() {
      return {}
    },
    props: ['user'],
    components: {},
    methods: {}
  }
</script>

<style></style>