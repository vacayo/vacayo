<template>
  <div>
    <input type="text" :name="name" :value="value" class="form-control" />
  </div>
</template>

<script type="text/babel">
  export default {
    name: 'NumericSpinnerInput',
    model: {
      prop: 'value',
      event: 'input'
    },
    props: {
      value: Number,
      name: String
    },
    data: function() {
      return {
      }
    },
    mounted() {
      $("input[name='"+this.name+"']").TouchSpin({
          min: 0,
          max: 100,
          step: 0.1,
          decimals: 2,
          boostat: 5,
          maxboostedstep: 10,
          postfix: 'miles',
          buttondown_class: 'btn btn-default btn-outline',
          buttonup_class: 'btn btn-default btn-outline'
      });
      $("input[name='"+this.name+"']").on('change', function(event) {
        let value = parseFloat(event.target.value);
        this.$emit('input', value);
      }.bind(this));
    }
  }
</script>

<style></style>