<template>
  <el-steps :space="200" :center="true" :align-center="true" :active="stepIndex" finish-status="success">
    <el-step title="Step 1" description="Property Address"></el-step>
    <el-step title="Step 2" description="Property Details"></el-step>
    <el-step title="Step 3" description="Contact Info"></el-step>
  </el-steps>
</template>

<script type="text/babel">
export default {
  props: ['stepIndex'],

  data() {
    return {
    }
  },

  methods: {
  }
}
</script>

<style>

</style>