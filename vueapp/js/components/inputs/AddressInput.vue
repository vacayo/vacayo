<template>
  <div>
    <input type="text" :name="name" :value="location.address" class="form-control" />
  </div>
</template>

<script type="text/babel">
  export default {
    name: 'AddressInput',
    model: {
      prop: 'location',
      event: 'input'
    },
    props: {
      location: Object,
      name: String
    },
    methods: {
      search(address, syncResults, asyncResults) {
        if (address == '') {
          return
        }

        fetch('/api/address/?query=' + address)
          .then(
            response => response.json(),
            error => console.log('An error occurred while looking up address:', error)
          )
          .then(
            json => {
              asyncResults(json.results)
            }
          )
      }
    },
    data: function () {
      return {
      }
    },
    mounted() {
      $("input[name='" + this.name + "']").typeahead({
          minLength: 3,
          highlight: true
        },
        {
          name: 'address-search',
          source: this.search,
          display: 'address',
          async: true,
          limit: 7,
        });
      $("input[name='" + this.name + "']").on('typeahead:select typeahead:cursorchange', function (event, location) {
        this.$emit('input', location);
      }.bind(this));
    },

  }
</script>

<style></style>