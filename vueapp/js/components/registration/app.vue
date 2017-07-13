<template>
  <div>
    <app-header></app-header>
    <el-row type="flex" justify="space-around">
      <el-col :xs="0" :sm="3"></el-col>
      <el-col :xs="24" :sm="18">
        <el-card class="content" v-loading.body="loading" element-loading-text="Saving...">
          <el-steps v-if="!saved" :space="200" :center="true" :align-center="true" :active="currentStep" finish-status="success">
            <el-step title="Step 1" description="Property Address"></el-step>
            <el-step title="Step 2" description="Property Details"></el-step>
            <el-step title="Step 3" description="Contact Info"></el-step>
          </el-steps>
          <div>
            <component :is='currentForm' v-on:next="next" v-on:prev="prev"></component>
          </div>
        </el-card>
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
let FORMS = ['address-form', 'property-form', 'contact-form', 'confirmation'];

export default {
  data() {
    return {
      currentStep: 0,
      loading: false,
      saved: false
    }
  },
  computed: {
    currentForm() {
      return FORMS[this.currentStep]
    },
  },
  components: {
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
        this.currentStep = 1;
      }

      // load contact form
      else if (this.currentStep == 1) {
        this.currentStep = 2;
      }

      // save the registration
      else if (this.currentStep == 2) {
        this.loading = true;
        this.save().then(() => {
          this.saved = true;
          this.loading = false;
          this.currentStep = 3;
          console.log(this);
        });
      }
    },
    prev() {
      if (--this.currentStep < 0) this.currentStep = 0;
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
  }
}
</script>

<style>
  body {
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    font-size: 16px;
    color: darkblue;
  }

  .el-steps {
    margin: 20px 0 80px 0;
  }

  .content {
    padding: 20px 50px;
  }
</style>