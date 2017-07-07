<template>
  <el-form>

    <el-autocomplete
      class="inline-input"
      placeholder="Address"
      v-model="address"
      :fetch-suggestions="search"
      :trigger-on-focus="false"
      @select="handleSelect"
    >
      <el-button slot="append" type="primary" icon="search" @click="next"></el-button>
    </el-autocomplete>

  </el-form>
</template>

<script type="text/babel">
import fetch from 'isomorphic-fetch';

export default {
  data() {
    return {
    }
  },
  computed: {
    address: {
      get () {return this.$store.state.address},
      set (value) {this.$store.commit('setAddress', value)}
    }
  },
  components: {
  },
  methods: {
    next() {
      this.$emit('next');
    },
    search(searchText, cb) {
      let url  = '/api/address?query=' + searchText;
      if(searchText !== '') {
        fetch(url)
          .then(
            response => response.json(),
            error => console.log('An error occurred while looking up address:', error)
          )
          .then(
            json => cb(json.results)
          )
      }
    },
    handleSelect(item) {
      //console.log(item);
    }
  }
}
</script>

<style>
.el-autocomplete {
  width: 100%;
}
</style>