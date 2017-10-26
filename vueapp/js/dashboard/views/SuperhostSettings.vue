<template>
  <form v-if="user.host" class="form-horizontal" id="superhost-settings" autocomplete="off">

    <div class="form-group row">
      <label class="col-sm-3 form-control-label">Accept new homes</label>
      <div class="col-sm-9">
        <ToogleInput name="active" v-model="user.host.active" />
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-3 form-control-label">within</label>
      <div class="col-sm-9">
        <div class="input-group bootstrap-touchspin">
          <NumericSpinnerInput name="radius" v-model="user.host.radius" />
        </div>
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-3 form-control-label">of address</label>
      <div class="col-sm-9">
        <AddressInput name="address" v-model="user.host.location" />
        <div class="text-left">(Lat: {{ user.host.location.latitude }}&deg;, Lng: {{ user.host.location.longitude }}&deg;)</div>
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-12 form-control-label text-center"><em>(you can also drag & zoom the map below to the location you want)</em></label>
    </div>

    <div class="form-group row">
      <div class="col-sm-12">
        <GoogleMaps name="coverage_area" v-model="user.host.location" :radius="user.host.radius"></GoogleMaps>
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
  import GoogleMaps from '../../components/inputs/GoogleMaps'
  import ToogleInput from '../../components/inputs/ToogleInput'
  import AddressInput from '../../components/inputs/AddressInput'
  import NumericSpinnerInput from '../../components/inputs/NumericSpinnerInput'

  export default {
    components: {
      GoogleMaps,
      ToogleInput,
      AddressInput,
      NumericSpinnerInput
    },
    props: ['user'],
    methods: {
      save() {
        let url  = '/api/host';
        let options = {
          method: "PATCH",
          body: JSON.stringify(this.user.host),
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