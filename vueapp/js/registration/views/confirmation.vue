<template>
  <el-form>
    <div class="title">Thank you {{ owner.first_name }}!</div>
    <div class="subtitle">A Vacayo representative will be touch with you shortly to schedule a property walk-through.</div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="24">
      </el-col>
    </el-row>
    <div class="actions">
      <el-button type="primary" @click="close">Close</el-button>
    </div>
  </el-form>
</template>

<script type="text/babel">
export default {
  data() {
    return {
      owner: this.$store.state.owner,
    }
  },
  methods: {
    close() {
      this.$emit('close');
    }
  },
}
</script>

<style>
</style>