<template>
  <el-form label-width="100px" label-position="top">
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="First Name">
          <el-input v-model="first_name"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Last Name">
          <el-input v-model="last_name"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Phone">
          <el-input v-model="phone"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Email">
          <el-input v-model="email"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <div class="actions">
      <el-button @click="prev">Prev</el-button>
      <el-button type="primary" @click="next">Submit</el-button>
    </div>
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
    first_name: {
      get () {return this.$store.state.first_name},
      set (value) {this.$store.commit('setFirstName', value)}
    },
    last_name: {
      get () {return this.$store.state.last_name},
      set (value) {this.$store.commit('setLastName', value)}
    },
    phone: {
      get () {return this.$store.state.phone},
      set (value) {this.$store.commit('setPhone', value)}
    },
    email: {
      get () {return this.$store.state.email},
      set (value) {this.$store.commit('setEmail', value)}
    },
  },
  methods: {
    next() {
      this.$emit('next');
    },
    prev() {
      this.$emit('prev');
    },
  },
}
</script>

<style>
.el-input, .el-select {
  width: 100%;
}

.el-form-item__label, .el-checkbox__label {
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
}

.el-button--primary {
  color: #fff !important;
  border-color: #337ab7 !important;
  background-color: #337ab7 !important;
}

.actions {
  margin-top: 12px;
}
</style>