<template>
  <el-form label-width="100px" label-position="top">
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Bedrooms">
          <el-input-number v-model="bedrooms" :step="1" size="large"></el-input-number>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Bathrooms">
          <el-input-number v-model="bathrooms" :step="0.5" size="large"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <!--
    <el-select v-model="bedrooms" placeholder="Select">
      <el-option
        v-for="item in bedroom_options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <el-select v-model="bathrooms" placeholder="Select">
      <el-option
        v-for="item in bathroom_options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    -->
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Home Type">
          <el-select v-model="home_type" placeholder="Select" size="large">
            <el-option
              v-for="item in home_type_options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Size (sq. ft.)">
          <el-input-number v-model="home_size" :step="10" size="large"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Has this property been rented before?">
          <el-switch v-model="has_rented" on-text="Yes" on-color="#13ce66" off-text="No" off-color="#bfcbd9" size="large"></el-switch>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item v-if="has_rented" label="Last Rent Amount (USD)?">
          <el-input-number v-model="last_rent" :step="10" size="large" v-mask="'$####.00'"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Available Starting">
          <el-date-picker v-model="available_date" type="date" placeholder="Pick a day" size="large">
          </el-date-picker>
        </el-form-item>
      </el-col>
    </el-row>
    <div class="actions">
      <el-button @click="prev">Prev</el-button>
      <el-button type="primary" @click="next">Next</el-button>
    </div>
  </el-form>
</template>

<script type="text/babel">
import fetch from 'isomorphic-fetch';

export default {
  data() {
    return {
      bedroom_options: [
        {value: 0, label: 'Studio'},
        {value: 1, label: '1 Bedroom'},
        {value: 2, label: '2 Bedrooms'},
        {value: 3, label: '3 Bedrooms'},
        {value: 4, label: '4 Bedrooms'},
        {value: 5, label: '5 Bedrooms'},
        {value: 6, label: '6 Bedrooms'},
        {value: 7, label: '7+ Bedrooms'},
      ],
      bathroom_options: [
        {value: 1.0, label: '1 Bathroom'},
        {value: 1.5, label: '1.5 Bathrooms'},
        {value: 2.0, label: '2 Bathrooms'},
        {value: 2.5, label: '2.5 Bathrooms'},
        {value: 3.0, label: '3 Bathrooms'},
        {value: 3.5, label: '3.5 Bathrooms'},
        {value: 4.0, label: '4+ Bathrooms'},
      ],
      home_type_options: [
        {value: 'SingleFamily', label: 'Single Family'},
        {value: 'Duplex', label: 'Duplex'},
        {value: 'Triplex', label: 'Triplex'},
        {value: 'Quadruplex', label: 'Quadruplex'},
        {value: 'Condominium', label: 'Condominium'},
        {value: 'Cooperative', label: 'Cooperative'},
        {value: 'Mobile', label: 'Mobile'},
        {value: 'Apartment', label: 'Apartment'},
        {value: 'Timeshare', label: 'Timeshare'},
      ],
      has_rented: false,
    }
  },
  computed: {
    address: {
      get () {return this.$store.state.address}
    },
    bedrooms: {
      get () {return this.$store.state.bedrooms},
      set (value) {this.$store.commit('setBedrooms', value)}
    },
    bathrooms: {
      get () {return this.$store.state.bathrooms},
      set (value) {this.$store.commit('setBathrooms', value)}
    },
    home_type: {
      get () {return this.$store.state.home_type},
      set (value) {this.$store.commit('setHomeType', value)}
    },
    home_size: {
      get () {return this.$store.state.home_size},
      set (value) {this.$store.commit('setHomeSize', value)}
    },
    last_rent: {
      get () {return this.$store.state.last_rent},
      set (value) {this.$store.commit('setLastRent', value)}
    },
    available_date: {
      get () {return this.$store.state.available_date},
      set (value) {this.$store.commit('setAvailableDate', value)}
    },
    quote: {
      get () {return this.$store.state.quote},
      set (value) {this.$store.commit('setQuote', value)}
    }
  },
  methods: {
    next() {
      this.$emit('next');
    },
    prev() {
      this.$emit('prev');
    },
  }
}
</script>

<style>
.el-form .el-input-number, .el-form .el-select {
  width: 100%;
}

.el-form .el-row {
  min-height: 88px;
}

.el-form .el-form-item__label, .el-form .el-checkbox__label {
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
}

.el-form .el-button--primary {
  color: #fff !important;
  border-color: #337ab7 !important;
  background-color: #337ab7 !important;
}

.el-form .actions {
  margin-top: 12px;
}
</style>