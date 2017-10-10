<template>
  <div>
    <input type="hidden" :name="name" :value="+value">
    <input type="checkbox" class="js-switch" :checked="value" @change="$emit('input', $event.target.checked)">
    <span>{{ value ? 'Yes' : 'No' }}</span>
  </div>
</template>

<script type="text/babel">
  export default {
    name: 'Switchery',
    props: ['name', 'value'],
    mounted() {
      new Switchery(document.querySelector('.js-switch'), {secondaryColor:'#f96868'});
    }
  }
</script>

<style></style>