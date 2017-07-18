<template>
  <el-form :model="property" ref="property">

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
.el-form .el-autocomplete {
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

.el-form .el-input-group__append {
  color: #fff !important;
  border-color: #337ab7 !important;
  background-color: #337ab7 !important;
}
</style>