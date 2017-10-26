<template>
  <div>
    <input type="checkbox" :name="name" :checked="checked" @change="changed($event.target.checked)" class="form-control" />
    <span>{{ checked ? 'Yes' : 'No' }}</span>
  </div>
</template>

<script type="text/babel">
  export default {
    name: 'ToogleInput',
    model: {
      prop: 'checked',
      event: 'change'
    },
    props: {
      checked: Boolean,
      name: String
    },
    methods: {
      changed(value) {
        this.$emit('change', value);
      }
    },
    data: function() {
      return {
      }
    },
    mounted() {
      new Switchery(document.querySelector("input[name='"+this.name+"']"), {secondaryColor:'#f96868'});
    }
  }
</script>

<style>

</style>