<template>
  <div class="card-layout">
    <div class="card card-shadow mx-auto">
      <div class="card-block p-60 p-xs-40">
        <h4>Become a Vacayo Superhost</h4>
        <p>Let's find some available properties that are waiting for a wonderful superhost like yourself!</p>
        <!--
        <div class="row text-center">
          <div class="col-12">
            <button class="btn btn-primary" @click="geolocate">
              <i class="icon fa-location-arrow" aria-hidden="true"></i>
              <small>Use my current location</small>
            </button>
          </div>
        </div>
        <div class="row text-center">
          <div class="col-12 m-20"><b>-- OR --</b></div>
        </div>
        -->
        <div class="row text-center">
          <div class="col-12">
            <p>Enter your home address or home town:</p>
          </div>
          <div class="col-md-10 col-xs-12">
            <AddressInput name="address" v-model="location" />
          </div>
          <div class="col-md-2 col-xs-12">
            <button class="btn btn-primary" @click="search">
              <i class="icon fa-search" aria-hidden="true"></i>
              <small>Search</small>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="row mx-auto my-10">
      <PropertyCard v-for="(property, id) in properties" :property="property" class="col-lg-6 p-10">
        <div slot="actions" class="px-20 py-10">
          <button class="btn btn-vacayo" @click="assign">
            <i class="icon fa-check" aria-hidden="true"></i>
            <span>Manage this property</span>
          </button>
        </div>
      </PropertyCard>
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
      geolocate() {

      },

      search() {
        let options = {
          credentials: 'same-origin',
        };

        fetch('/api/properties/search/' + _$.query(this.location), options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => {
              this.properties = json.results;
              console.log(this.properties);
            }
          )
      }

    },
    mounted() {
      //this.location = {'address': '922 Swinton Ave, Bronx, NY 10465, USA'};
      //this.search();
    }
  }
</script>

<style>
  .highlight {
    font-weight: bold;
    text-decoration: underline;
  }
</style>
