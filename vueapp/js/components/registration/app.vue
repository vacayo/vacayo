<template>
  <div>
    <app-header></app-header>
    <el-row type="flex" justify="space-around">
      <el-col :span="6"></el-col>
      <el-col :span="12">
        <el-card class="content">
          <stepper :step-index="currentStep" class="stepper"></stepper>
          <div>
            <component :is='currentForm' v-on:next="next" v-on:prev="prev"></component>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6"></el-col>
    </el-row>
  </div>
</template>

<script type="text/babel">
import AppHeader from '../app_header.vue'
import Stepper from './stepper.vue'
import AddressForm from './address_form.vue'
import PropertyForm from './property_form.vue'
let FORMS = ['address-form', 'property-form'];

export default {
  data() {
    return {
      currentStep: 0
    }
  },
  computed: {
    currentForm: function () {
      return FORMS[this.currentStep]
    }
  },
  components: {
    AppHeader,
    Stepper,
    AddressForm,
    PropertyForm
  },
  methods: {
    next() {
      if (this.currentStep++ > 2) this.currentStep = 0;
    },
    prev() {
      if (this.currentStep-- < 0) this.currentStep = 2;
    }
  }
}
</script>

<style>
  body {
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    font-size: 12px;
  }

  .stepper {
    margin: 20px 0 80px 0;
  }

  .content {
    padding: 20px 50px;
  }
</style>