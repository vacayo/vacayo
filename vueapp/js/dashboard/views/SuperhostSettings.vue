<template>
  <form v-if="user.host" class="form-horizontal" id="superhost-settings">

    <div class="form-group row">
      <label class="col-sm-4 form-control-label">Accept new homes</label>
      <div class="col-sm-5">
        <switchery name="active" v-model="user.host.active" />
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-4 form-control-label">within</label>
      <div class="col-sm-5">
        <div class="input-group bootstrap-touchspin">
          <input type="text" class="form-control" name="manage_radius" data-plugin="TouchSpin" data-min="0" data-max="100" data-postfix="miles" data-buttondown_class="btn btn-default btn-outline" data-buttonup_class="btn btn-default btn-outline" :value="user.host.manage_radius" style="display: block;">
        </div>
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-4 form-control-label">of address</label>
      <div class="col-sm-5">
        <input type="text" class="form-control" name="manage_address">
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
  import Switchery from '../../components/Switchery'

  export default {
    components: {
      Switchery
    },
    props: ['user'],
    methods: {
      save() {
        let data = {};
        for (var entry of (new FormData(document.getElementById('superhost-settings'))).entries()) {
          data[entry[0]] = entry[1];
        }
        let url  = '/api/host';
        let options = {
          method: "PATCH",
          body: JSON.stringify(data),
          credentials: 'same-origin',
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        fetch(url, options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => toastr.success('Your Superhost settings have been updated.', 'Saved!')
          )
      }
    }
  }
</script>

<style></style>