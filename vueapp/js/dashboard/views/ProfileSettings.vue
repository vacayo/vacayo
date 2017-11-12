<template>
  <form class="form-horizontal" id="profile-settings">
    <div class="form-group row">
      <label class="col-sm-4 form-control-label">First Name: </label>
      <div class="col-sm-6">
        <input type="text" class="form-control" name="first_name" placeholder="First Name" autocomplete="off" :value="user.first_name">
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-4 form-control-label">Last Name: </label>
      <div class="col-sm-6">
        <input type="text" class="form-control" name="last_name" placeholder="Last Name" autocomplete="off" :value="user.last_name">
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-4 form-control-label"></label>
      <div class="col-sm-6">
        <a href="/accounts/password/change/">Change Password</a>
      </div>
    </div>

    <div class="form-group row">
      <div class="col-sm-10 col-sm-offset-2">
        <button type="button" class="btn btn-primary" @click="save">Save</button>
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
    methods: {
      save() {
        let data = {};
        for (var entry of (new FormData(document.getElementById('profile-settings'))).entries()) {
          data[entry[0]] = entry[1];
        }

        let options = {
          method: "PATCH",
          body: JSON.stringify(data),
          credentials: 'same-origin',
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        fetch('/api/user/', options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => toastr.success('Your Profile settings have been updated.', 'Saved!')
          )
      }
    }
  }
</script>

<style></style>