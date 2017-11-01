<template>
  <div>
    <div class="offer">
      <div class="offer_text">Estimated Offer</div>
      <div class="offer_value">{{ offer | currency }} / mo.</div>
    </div>
    <div v-sticky="{zIndex: 9999, stickyTop:0}">
      <AppHeader/>
      <media :query="{minWidth: 600, minHeight: 600}">
      <div class="stepper">
        <el-steps space="33%" :center="true" :align-center="true" :active="currentStep" process-status="finish" finish-status="process">
          <el-step title="Step 1" description="Property Address"></el-step>
          <el-step title="Step 2" description="Property Details"></el-step>
          <el-step title="Step 3" description="Contact Info"></el-step>
        </el-steps>
      </div>
      </media>
    </div>
    <el-row type="flex" justify="space-around">
      <el-col :xs="0" :sm="3"></el-col>
      <el-col :xs="24" :sm="18">
        <div class="content" v-loading.body="spinner" :element-loading-text="spinner_text">
          <div>
            <router-view :offer="offer" @loading="loading" @loaded="loaded"></router-view>
          </div>
        </div>
      </el-col>
      <el-col :xs="0" :sm="3"></el-col>
    </el-row>
  </div>
</template>

<script type="text/babel">
  import AppHeader from './views/Header'
  import Media from 'vue-media'
  import Headroom from 'vue-headroom'

  export default {
    data() {
      return {
        property: this.$store.state.property,
        currentStep: 0,
        spinner: false,
        spinner_text: 'Loading...'
      }
    },
    components: {
      Media,
      Headroom,
      AppHeader,
    },
    computed: {
      offer() {
        let round = function(number, precision) {
          var factor = Math.pow(10, precision);
          var tempNumber = number * factor;
          var roundedTempNumber = Math.round(tempNumber);
          return roundedTempNumber / factor;
        };
        let markup = 1.05; // 5%
        let last_rent = round(this.property.last_rent * markup, -1);
        let rent_estimate = round(this.property.rent_estimate * markup, -1);
        let rent_estimate_low = round(this.property.rent_estimate_low, -1);
        let rent_estimate_high = round(this.property.rent_estimate_high, -1);
        let value = last_rent || rent_estimate;

        if (value > rent_estimate_high) value = rent_estimate_high;
        if (value < rent_estimate_low) value = rent_estimate_low;

        return value;
      },
    },
    methods: {
      loading(text) {
        this.spinner_text = text;
        this.spinner = true;
      },
      loaded() {
        this.spinner_text = 'Loading...';
        this.spinner = false;
        document.body.scrollTop = document.documentElement.scrollTop = 0;
      }
    },
    created() {
      let address = this.$route.query.address;
      if (address) {
        this.$store.commit('updateProperty', {address});
        this.$router.replace({name: 'lookup', query: { auto: true }});
      }
      else {
        this.$router.replace({name: 'lookup'});
      }
    }
  }
</script>

<style>
body {
  font-family: 'Poppins', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.stepper {
  padding: 20px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.12), 0 0 6px 0 rgba(0, 0, 0, 0.04);
  background-color: #fff;
}

.content {
  padding: 50px 50px;
}

.offer {
  text-align: right;
  position: fixed;
  top: 0;
  right: 0;
  z-index: 10000;
}

.offer .offer_text {
  font-size: 12px;
  color: #EEEEEE;
  margin: 10px;
}

.offer .offer_value {
  font-weight: 900;
  font-size: 20px;
  color: #fff;
  margin: 10px;
}

.el-form .el-row {
  min-height: 88px;
}

.el-form .el-input, .el-form .el-input-number, .el-form .el-autocomplete, .el-form .el-select {
  width: 100%;
}

.el-form .el-form-item__label, .el-form .el-checkbox__label {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
}

.el-form .el-button--primary, .el-form .el-input-group__append {
  color: #fff;
  border-color: #24678D;
  background-color: #24678D;
  padding: 10px 75px;
}

.el-form .title {
  color: #24678D;
  font-size: 22px;
  font-weight: 700;
  margin: 10px 0;
}

.el-form .subtitle {
  color: #8391a5;
  font-size: 14px;
  margin: 10px 0 50px 0;
}

.el-form .actions {
  margin-top: 12px;
}

.el-step__head.is-text.is-success {
  background-color: #13ce66;
  border-color: #13ce66;
}
</style>