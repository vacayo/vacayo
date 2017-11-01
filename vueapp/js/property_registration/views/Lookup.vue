<template>
  <el-form>
    <div class="title">Property Address</div>
    <div class="subtitle"></div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="24">
        <el-form-item prop="address">
          <el-autocomplete
            size="large"
            class="inline-input"
            placeholder="Address"
            :props="{label:'address', value:'address'}"
            :fetch-suggestions="autocomplete"
            :trigger-on-focus="false"
            :value="property.address"
            @input="update('address', $event)"
          >
            <el-button slot="append" type="primary" @click="next">Get Your Instant Offer</el-button>
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
    created() {
      let auto = this.$route.query.auto;
      if (auto) {
        this.next();
      }
    },
    methods: {
      update(field, value) {
        this.$store.commit('updateProperty', {[field]: value});
      },
      autocomplete(address, cb) {
        if (address == '') {
          return Promise.resolve();
        }

        fetch('/api/address?query=' + address)
          .then(
            response => response.json(),
            error => console.log('An error occurred while looking up address:', error)
          )
          .then(
            json => {
              let options = json.results;
              cb(options);
              return options;
            }
          )
      },
      details(address) {
        if (address == '') {
          return Promise.resolve();
        }

        return fetch('/api/property?address=' + address)
          .then(
            response => response.json(),
            error => console.log('An error occurred while fetching property:', error)
          )
          .then(
            json => {
              let property = json.results;
              return property;
            }
          )
      },
      next() {
        this.$emit('loading', {text: 'Searching...'});

        this.details(this.property.address).then((property) => {
          this.$emit('loaded');

          this.$store.commit('updateProperty', property);

          if (property.in_service) {
            this.$router.push({name: 'details'});
          }
          else {
            this.$router.push({name: 'contact'});
          }
        });
      },
    },
  }
</script>

<style>
</style>