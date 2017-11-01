<template>
  <el-form :model="owner" :rules="rules" ref="owner" label-width="100px" label-position="top">
    <div class="title">We're sorry, but we're not in your area yet!</div>
    <div class="subtitle">
      We’re working to expand our services across the nation.
      <br /><br />
      Please leave your contact information and we’ll notify you when we arrive at your area.
    </div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="First Name" prop="first_name">
          <el-input :value="owner.first_name" @input="update('first_name', $event)"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Last Name" prop="last_name">
          <el-input :value="owner.last_name" @input="update('last_name', $event)"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Phone" prop="phone">
          <el-input type="tel" :value="owner.phone" @input="update('phone', $event)"></el-input>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Email" prop="email">
          <el-input :value="owner.email" @input="update('email', $event)"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <div class="actions">
      <el-button @click="prev">Prev</el-button>
      <el-button @click="next" type="primary">Submit</el-button>
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
          ]
        },
      }
    },
    methods: {
      update(field, value) {
        this.$store.commit('updateOwner', {[field]: value});
      },
      save() {
        let data = Object.assign({}, this.$store.state);
        let options = {
          method: "POST",
          body: JSON.stringify(data),
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        return fetch('/api/lead/', options)
          .then(
            response => response.json(),
            error => console.log('An error occurred while looking up address:', error)
          )
          .then(
            json => {
              this.$store.commit('updateOwner', {['password']: null});
              this.$store.commit('updateOwner', {['password2']: null});
            }
        )
      },
      next() {
        this.$refs['owner'].validate((valid) => {
          if (!valid) {
            return false;
          }
          this.$emit('loading', 'Saving...');
          this.save().then(() => {
            this.$emit('loaded');
            this.$router.push({name: 'confirmation'});
          });
        });
      },
      prev() {
        this.$router.push({name: 'lookup'});
      },
    }
  }
</script>

<style>
</style>