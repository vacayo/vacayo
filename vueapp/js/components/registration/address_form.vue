<template>
  <el-form :model="property" ref="property">
    <div class="title">Property Address</div>
    <div class="subtitle"></div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="24">
        <el-form-item label="First Name" prop="first_name">
          <el-autocomplete
            size="large"
            class="inline-input"
            placeholder="Address"
            :fetch-suggestions="search"
            :trigger-on-focus="false"
            :value="property.address"
            @input="updateProperty('address', $event)"
          >
            <el-button slot="append" type="primary" @click="next">Get Your Instant Quote</el-button>
          </el-autocomplete>
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
</template>

<script type="text/babel">
import fetch from 'isomorphic-fetch';

export default {
  data() {
    return {
      property: this.$store.state.property,
    }
  },
  methods: {
    updateProperty(field, value) {
      this.$store.commit('updateProperty', {[field]: value});
    },
    next() {
      this.$emit('next');
    },
    search(address, cb) {
      if (address == '') {
        return
      }

      let url  = '/api/address?query=' + address;
      fetch(url)
        .then(
          response => response.json(),
          error => console.log('An error occurred while looking up address:', error)
        )
        .then(
          json => cb(json.results)
        )
    },
  },
}
</script>

<style>
</style>