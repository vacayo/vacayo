<template>
  <div class="card-layout">
    <div class="card card-shadow mx-auto">
      <div class="card-block p-60 p-xs-40">
        <h4>Become a Vacayo Superhost</h4>
        <p>Great, now let's save your home address so that Vacayo can find some properties near you.</p>
        <div class="row">
          <div class="col-md-10 col-xs-12">
            <AddressInput name="address" v-model="location" placeholder="Enter your home address..." />
          </div>
          <div class="col-md-2 col-xs-12">
            <button class="btn btn-primary" @click="save">
              <i class="icon fa-search" aria-hidden="true"></i>
              <small>Save</small>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
  import _$ from '../../lib/dom';
  import moment from 'moment';
  import PropertyCard from '../../components/PropertyCard'
  import AddressInput from '../../components/inputs/AddressInput'

  export default {
    data() {
      return {
        showModal: false,
        start_date: moment(),
        end_date: moment().add(1, 'years'),
        location: {},
        properties: {}
      }
    },
    props: ['user'],
    components: {
      AddressInput,
      PropertyCard,
    },
    methods: {
      save() {
        let data = {
          active: true,
          radius: 30,
          location: this.location
        };
        let options = {
          method: "PATCH",
          body: JSON.stringify(data),
          credentials: 'same-origin',
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        fetch('/api/host/', options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => window.location.href = '/dashboard'
          )
      }

    }
  }
</script>

<style>
  .highlight {
    font-weight: bold;
    text-decoration: underline;
  }
</style>
