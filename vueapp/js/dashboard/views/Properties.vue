<template>
  <div class="row" data-plugin="matchHeight" data-by-row="true">
    <div v-for="property in properties" class="col-lg-6">
      <div class="card card-shadow text-center">
        <div class="card-header card-header-transparent cover overlay" style="height: calc(100% - 100px);">
          <img class="cover-image" :src="property.main_image" alt="..." style="height: 100%;">
          <div class="overlay-panel overlay-background overlay-top">
            <div class="font-size-20 white">{{ property.address1 }}</div>
            <div class="font-size-14 grey-400">{{ property.bedrooms }} BR / {{ property.bathrooms }} BATH</div>
          </div>
        </div>
        <div class="card-block bg-white px-30 py-20 h-100">
          <div class="row pearls">
            <div class="col-4 pearl" v-bind:class="[{ current: (property.status == 'info'), done: (property.status != 'info') }]">
              <div class="pearl-icon"><i class="icon fa-home" aria-hidden="true"></i></div>
              <span class="pearl-title">Property Info</span>
            </div>
            <div class="col-4 pearl" v-bind:class="[{ current: (property.status == 'visit'), done: (property.status != 'visit') }]">
              <div class="pearl-icon"><i class="icon fa-calendar" aria-hidden="true"></i></div>
              <span class="pearl-title">Site Visit</span>
            </div>
            <div class="col-4 pearl" v-bind:class="[{ current: (property.status == 'lease'), done: (property.status != 'lease') }]">
              <div class="pearl-icon"><i class="icon fa-file-text-o" aria-hidden="true"></i></div>
              <span class="pearl-title">Lease</span>
            </div>
          </div>
        </div>
        <div class="card-footer px-30 py-20 h-100">

          <div class="row" v-if="property.status == 'visit'">
            <div class="col-6">Your site visit is scheduled for <b>{{ property.visit_date }}</b></div>
            <div class="col-6">
              <button type="button" class="btn btn-outline btn-primary btn-round">
                <i class="icon fa-calendar" aria-hidden="true"></i>
                <span>Change Date</span>
              </button>
            </div>
          </div>

          <div class="row" v-if="property.status == 'lease'">
            <div class="col-6">Your lease is ready for signing!</div>
            <div class="col-6">
              <button type="button" class="btn btn-outline btn-primary btn-round">
                <i class="icon fa-pencil" aria-hidden="true"></i>
                <span>Sign Your Lease</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
export default {
  data() {
    return {
      properties: []
    }
  },
  components: {},
  methods: {
    load() {
      let url  = '/api/properties/';

      return fetch(url, {credentials: 'same-origin'})
        .then(
          response => response.json(),
          error => console.log('An error occurred while fetching property:', error)
        )
        .then(
          json => {
            let props = json.results;
            this.properties = props;
          }
        )
    },
  },
  created() {
    this.load();
  }
}
</script>

<style></style>
