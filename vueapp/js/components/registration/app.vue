<template>
  <div>
    <div class="quote">
      <div class="quote_text">Estimated Quote</div>
      <div class="quote_value">{{ quote }}</div>
    </div>
    <media :query="{minWidth: 768}">
      <div v-sticky="{zIndex: 9999, stickyTop:0}">
        <app-header></app-header>
        <div class="stepper">
          <el-steps :space="150" :center="true" :align-center="true" :active="currentStep" finish-status="success">
            <el-step title="Step 1" description="Property Address"></el-step>
            <el-step title="Step 2" description="Property Details"></el-step>
            <el-step title="Step 3" description="Contact Info"></el-step>
          </el-steps>
        </div>
      </div>
    </media>
    <media :query="{maxWidth: 768}">
      <div v-sticky="{zIndex: 9999, stickyTop:0}">
        <app-header></app-header>
      </div>
    </media>
    <el-row type="flex" justify="space-around">
      <el-col :xs="0" :sm="3"></el-col>
      <el-col :xs="24" :sm="18">
        <div class="content" v-loading.body="loading" :element-loading-text="loading_text">
          <div>
            <component :is='currentForm' v-on:next="next" v-on:prev="prev"></component>
          </div>
        </div>
      </el-col>
      <el-col :xs="0" :sm="3"></el-col>
    </el-row>
  </div>
</template>

<script type="text/babel">
import AppHeader from '../app_header.vue'
import AddressForm from './address_form.vue'
import PropertyForm from './property_form.vue'
import ContactForm from './contact_form.vue'
import Confirmation from './confirmation.vue'
import Media from 'vue-media'
import Headroom from 'vue-headroom'

let FORMS = ['address-form', 'property-form', 'contact-form', 'confirmation'];
let PINS = [true, false, false, true];

export default {
  data() {
    return {
      currentStep: 0,
      loading: false,
      loading_text: 'Loading...'
    }
  },
  computed: {
    address: {
      get () {return this.$store.state.address},
      set (value) {this.$store.commit('setAddress', value)}
    },
    quote: {
      get () {return this.$store.state.quote},
      set (value) {this.$store.commit('setQuote', value)}
    },
    currentForm() {
      return FORMS[this.currentStep]
    },
    formatter() {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
      });
    }
  },
  components: {
    Media,
    Headroom,
    AppHeader,
    AddressForm,
    PropertyForm,
    ContactForm,
    Confirmation
  },
  methods: {
    next() {
      // search & pre-load property details
      if (this.currentStep == 0) {
        this.loading_text = 'Searching ...';
        this.loading = true;
        this.search(this.address).then(() => {
          this.loading = false;
          this.currentStep = 1;
          document.body.scrollTop = document.documentElement.scrollTop = 0;
        })
      }

      // load contact form
      else if (this.currentStep == 1) {
        this.currentStep = 2;
        document.body.scrollTop = document.documentElement.scrollTop = 0;
      }

      // save the registration
      else if (this.currentStep == 2) {
        this.loading_text = 'Saving ...';
        this.loading = true;
        this.save().then(() => {
          this.loading = false;
          this.currentStep = 3;
          document.body.scrollTop = document.documentElement.scrollTop = 0;
        });
      }
    },
    prev() {
      if (--this.currentStep < 0) this.currentStep = 0;
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },
    search(address) {
      if (address == '') {
        return
      }
      let url  = '/api/property?address=' + address;

      return fetch(url)
        .then(
          response => response.json(),
          error => console.log('An error occurred while fetching property:', error)
        )
        .then(
          json => {
            let props = json.results;
            this.$store.commit('setBedrooms', props.bedrooms);
            this.$store.commit('setBathrooms', props.bathrooms);
            this.$store.commit('setHomeType', props.home_type);
            this.$store.commit('setHomeSize', props.home_size);
            this.$store.commit('setQuote', this.formatter.format(props.rentzestimate_amount));
          }
        )
    },
    save() {
      let data = this.$store.state;
      let url  = '/api/registration/';
      let options = {
        method: "POST",
        body: JSON.stringify(data),
        headers: new Headers({
          'Content-Type': 'application/json'
        })
      };

      return fetch(url, options)
        .then(
          response => response.json(),
          error => console.log('An error occurred while looking up address:', error)
        )
    }
  },
  created() {
    let address = this.$route.query.address;
    if (address) {
      this.address = address;
      this.next()
    }
  }
}
</script>

<style>
body {
  font-family: "intercom-font", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  color: darkblue;
}

.stepper {
  padding: 20px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.12), 0 0 6px 0 rgba(0, 0, 0, 0.04);
  background-color: #fff;
}

.content {
  padding: 50px 50px;
}

.quote {
  text-align: right;
  position: fixed;
  top: 0;
  right: 0;
  z-index: 10000;
}

.quote .quote_text {
  font-size: 12px;
  color: #EEEEEE;
  margin: 12px;
}

.quote .quote_value {
  font-weight: bold;
  font-size: 20px;
  color: #fff;
  margin: 12px;
}
</style>