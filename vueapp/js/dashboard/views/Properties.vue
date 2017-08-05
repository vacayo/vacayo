<template>
  <div class="row" data-plugin="matchHeight" data-by-row="true">
    <div v-for="(property, id) in properties" class="col-lg-6">
      <div class="card card-shadow text-center">
        <div class="card-header card-header-transparent cover overlay" style="height: calc(100% - 100px);">
          <img class="cover-image" :src="property.main_image" alt="..." style="height: 100%;">
          <div class="overlay-panel overlay-background overlay-top">
            <div class="font-size-20 white">{{ property.address1 }}</div>
            <div class="font-size-14 grey-400">{{ property.bedrooms }} BR / {{ property.bathrooms }} BATH</div>
          </div>
        </div>
        <div class="card-block bg-white px-30 py-20 h-120">
          <div class="row pearls">

            <div v-for="status in property.onboarding_statuses" class="col-3 pearl done" v-bind:class="[{ current: status.is_current }]">

              <div v-if="status.name == 'pending_review'">
                <div class="pearl-icon"><i class="icon fa-home" aria-hidden="true"></i></div>
                <div class="pearl-title">
                  <div>Vacayo Offer</div>
                  <small>{{ property.offer | currency }} / mo.</small>
                </div>
              </div>

              <div v-if="status.name == 'pending_site_visit'">
                <div class="pearl-icon"><i class="icon fa-calendar" aria-hidden="true"></i></div>
                <div class="pearl-title">
                  <div>Home Visit</div>
                  <small>{{ property.visit_date }}</small>
                </div>
              </div>

              <div v-if="status.name == 'pending_lease_signing'">
                <div class="pearl-icon"><i class="icon fa-file-text-o" aria-hidden="true"></i></div>
                <span class="pearl-title">Lease</span>
              </div>

              <div v-if="status.name == 'ready'">
                <div class="pearl-icon"  v-bind:class="[{ ready: property.status == 'ready' }]"><i class="icon fa-check" aria-hidden="true"></i></div>
                <span class="pearl-title">Ready</span>
              </div>

            </div>

          </div>
        </div>
        <div class="card-footer px-30 py-20 h-100">
          <div class="row" v-if="property.status == 'pending_site_visit'">
            <div class="col-6">Your site visit is currently scheduled for <b>{{ property.visit_date }}</b></div>
            <div class="col-6">
              <button type="button" class="btn btn-danger btn-round" data-toggle="modal" data-target="#datepickerModal" @click="updateDatePicker(property.id, property.visit_date)">
                <i class="icon fa-calendar" aria-hidden="true"></i>
                <span>Change Date</span>
              </button>
            </div>
          </div>
          <div class="row" v-if="property.status == 'pending_lease_signing'">
            <div class="col-6">Your lease is ready for signing!</div>
            <div class="col-6">
              <button type="button" class="btn btn-danger btn-round">
                <i class="icon fa-pencil" aria-hidden="true"></i>
                <span>Sign Lease</span>
              </button>
            </div>
          </div>
          <div class="row" v-if="property.status == 'ready'">
            <div class="col-12 text_center">Your rentals is unleashed!</div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="datepickerModal" aria-labelledby="datepickerLabel" role="dialog" tabindex="-1" style="display: none;" aria-hidden="true">
      <div class="modal-dialog modal-simple modal-sidebar modal-sm" style="width: 260px">
        <form class="modal-content">
          <div class="modal-header text-center">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">
            <div id="datepicker"></div>
            <input type="hidden" id="datepicker_input">
            <button class="btn btn-primary btn-block" data-dismiss="modal" type="button" @click="updateVisitDate">Change Date</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
  import Datepicker from 'bootstrap-datepicker'

  export default {
    data() {
      return {
        properties: {},
        pendingDateChange: {}
      }
    },
    components: {},
    filters: {
      currency(value) {
        let formatter = new Intl.NumberFormat('en-US', {
          style: 'currency',
          currency: 'USD',
          minimumFractionDigits: 2,
        });
        return formatter.format(value)
      }
    },
    methods: {
      updateDatePicker(id, visit_date) {
        let self = this;
        $('#datepicker').datepicker('update', visit_date);
        $('#datepicker').off('changeDate').on('changeDate', function() {
          self.pendingDateChange = {id, visit_date:$(this).datepicker('getFormattedDate')};
        });
      },
      updateVisitDate() {
        let url  = '/api/properties/';
        let options = {
          method: "POST",
          credentials: 'same-origin',
          body: JSON.stringify(this.pendingDateChange),
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        return fetch(url, options)
          .then(
            response => response.json(),
            error => console.log('An error occurred while fetching property:', error)
          )
          .then(
            json => {
              let props = json.results;
              this.properties[props.id] = props;
            }
          )
      },
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
    },
    mounted() {
      $('#datepicker').datepicker({
        startDate: '+7d'
      });
    }
  }
</script>

<style>
.pearl.current .pearl-icon, .pearl.current .pearl-number {
    color: #f96868;
    background-color: #fff;
    border-color: #f96868;
}

.pearl-icon.ready, .pearl-number.ready {
    color: #46be8a !important;
    background-color: #fff !important;
    border-color: #46be8a !important;
}
</style>
