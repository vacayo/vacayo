<template>
  <div class="card card-shadow card-property text-center">

    <div class="card-header card-header-transparent cover overlay">

      <div class="cover-background" :style="{ 'background-image': 'url(' + property.main_image + ')' }">
        <h3 class="white overlay-background py-20 m-0">{{ property.location.address }}</h3>
        <button type="button" class="btn btn-primary my-50 my-lg-100">View Details</button>
        <div class="row no-space overlay-background py-10">
          <div class="col">
            <div class="counter counter-inverse">
              <span class="counter-number">{{ property.bedrooms }}</span>
              <div class="counter-label">Bedrooms</div>
            </div>
          </div>
          <div class="col">
            <div class="counter counter-inverse">
              <span class="counter-number">{{ property.bathrooms }}</span>
              <div class="counter-label">Bathrooms</div>
            </div>
          </div>
          <div v-if="property.home_size" class="col">
            <div class="counter counter-inverse">
              <span class="counter-number">{{ property.home_size }}</span>
              <div class="counter-label">Sq. Feet</div>
            </div>
          </div>
        </div>
      </div>

      <!--
      <img v-if="property.main_image" class="cover-image" :src="property.main_image" alt="..." style="height: 100%;">
      <i v-if="!property.main_image" class="fa fa-home fa-5x" aria-hidden="true"></i>


      <div class="overlay-panel overlay-background overlay-top">
        <div class="font-size-20 white">{{ property.address1 }}</div>
        <div class="font-size-14 grey-400">{{ property.bedrooms }} BR / {{ property.bathrooms }} BATH</div>
      </div>
      -->

    </div>

    <div class="card-block bg-white">
      <div class="row">
        <div class="col">
        </div>
      </div>
    </div>

    <div class="card-footer">
      <slot name="actions">

      </slot>
    </div>
  </div>
</template>

<script type="text/babel">
  import Datepicker from 'bootstrap-datepicker'

  export default {
    data() {
      return {
      }
    },
    props: ['property'],
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
