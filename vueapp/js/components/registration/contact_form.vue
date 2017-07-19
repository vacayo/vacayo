<template>
  <el-form :model="owner" :rules="rules" ref="owner" label-width="100px" label-position="top">
    <div class="title">{{ quote }} per month</div>
    <div class="subtitle">
      We estimate that we can offer you a 1 year lease at the monthly rent above.
      We will provide you with an exact offer once a property walk-through is conducted.
      <br /><br />
      Please fill in your contact info below to schedule a walk-through.
    </div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="First Name" prop="first_name">
          <el-input :value="owner.first_name" @input="updateOwner('first_name', $event)"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Last Name" prop="last_name">
          <el-input :value="owner.last_name" @input="updateOwner('last_name', $event)"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Phone" prop="phone">
          <el-input :value="owner.phone" @input="updateOwner('phone', $event)" v-mask="'+1(###)-###-####'"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Email" prop="email">
          <el-input :value="owner.email" @input="updateOwner('email', $event)"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <div class="actions">
      <el-button @click="prev">Prev</el-button>
      <el-button type="primary" @click="next">Next</el-button>
    </div>
  </el-form>
</template>

<script type="text/babel">
import fetch from 'isomorphic-fetch';

export default {
  data() {
    return {
      owner: this.$store.state.owner,
      rules: {
        first_name: [
          { required: true, type: 'string', message: 'Please enter your first name', trigger: 'blur' },
        ],
        last_name: [
          { required: true, type: 'string', message: 'Please enter your last name', trigger: 'blur' },
        ],
        phone: [
          { required: true, type: 'string', message: 'Please enter your phone number', trigger: 'change' }
        ],
        email: [
          { required: true, type: 'string', message: 'Please enter your email', trigger: 'blur' },
        ],
      },
    }
  },
  props: [
    'quote'
  ],
  methods: {
    updateOwner(field, value) {
      this.$store.commit('updateOwner', {[field]: value});
    },
    next() {
      this.$refs['owner'].validate((valid) => {
        if (!valid) {
          return false;
        }
        this.$emit('next');
      });
    },
    prev() {
      this.$emit('prev');
    },
  },
}
</script>

<style>
</style>