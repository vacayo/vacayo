<template>
  <el-form>
    <div v-if="this.property.in_service">
      <div class="title">Thank you {{ owner.first_name }}!</div>
      <div class="subtitle">A Vacayo representative will be touch with you shortly to schedule a property walk-through.</div>
      <div class="subtitle">In the mean time you can visit your Vacayo dashboard to manage your property.</div>
      <a href="/dashboard">Visit Dashboard</a>
      <el-row :gutter="50">
        <el-col :sm="24" :md="24">
        </el-col>
      </el-row>
      <div class="actions">
        <el-button type="primary" @click="close">Close</el-button>
      </div>
    </div>
    <div v-else>
      <div class="title">Thank you {{ owner.first_name }}!</div>
      <div class="subtitle">We’ll notify you when we arrive in your area.</div>
      <el-row :gutter="50">
        <el-col :sm="24" :md="24">
        </el-col>
      </el-row>
      <div class="actions">
        <el-button type="primary" @click="close">Close</el-button>
      </div>
    </div>
  </el-form>
</template>

<script type="text/babel">
  export default {
    data() {
      return {
        property: this.$store.state.property,
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