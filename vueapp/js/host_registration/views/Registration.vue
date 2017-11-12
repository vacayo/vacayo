<template>
  <div class="card-layout">
    <div class="card card-shadow mx-auto">
      <div class="card-block p-60 p-xs-40">
        <h4>Become a Vacayo Superhost</h4>
        <p>We're thrilled that you've decided to join the Vacayo platform.</p>
        <p>Complete the registration below to start receiving homes to manage.</p>
        <form id="host_registration_form" autocomplete="off" novalidate="novalidate" @submit.prevent>
          <div class="form-group" :class="{'has-danger': errors.has('first_name') }">
            <input type="text" class="form-control" v-model="user.first_name" name="first_name" placeholder="First Name" v-validate="'required|min:2'" >
            <div class="form-control-feedback" v-show="errors.has('first_name')">{{ errors.first('first_name') }}</div>
          </div>
          <div class="form-group" :class="{'has-danger': errors.has('last_name') }">
            <input type="text" class="form-control" v-model="user.last_name" name="last_name" placeholder="Last Name" v-validate="'required|min:2'" >
            <div class="form-control-feedback" v-show="errors.has('last_name')">{{ errors.first('last_name') }}</div>
          </div>
          <div class="form-group" :class="{'has-danger': errors.has('email') }">
            <input type="email" class="form-control" v-model="user.email" name="email" placeholder="Email" v-validate="'required|email'" >
            <div class="form-control-feedback" v-show="errors.has('email')">{{ errors.first('email') }}</div>
          </div>
          <div class="form-group" :class="{'has-danger': errors.has('password1') }">
            <input type="password" class="form-control" v-model="user.password1" name="password1" placeholder="Password" v-validate="'required|min:8'" >
            <div class="form-control-feedback" v-show="errors.has('password1')">{{ errors.first('password1') }}</div>
          </div>
          <div class="form-group" :class="{'has-danger': errors.has('password2') }">
            <input type="password" class="form-control" v-model="user.password2" name="password2" placeholder="Password (again)" v-validate="'required|confirmed:password1'" >
            <div class="form-control-feedback" v-show="errors.has('password2')">{{ errors.first('password2') }}</div>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-block btn-success mt-40" @click.stop.prevent="createAccount" id="host_registration_submit">Create Account</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">

  export default {
    data() {
      return {
        user: {
          first_name: null,
          last_name: null,
          email: null,
          password1: null,
          password2: null,
        }
      }
    },
    methods: {
      createAccount() {
        this.$validator.validateAll();

        // validate the form
        if (this.errors.any()) {
          return;
        }

        let options = {
          method: "POST",
          credentials: 'same-origin',
          body: JSON.stringify({user: this.user}),
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        fetch('/api/user/', options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => {
              this.$emit('reload');
              this.$router.push('agreement');
            }
          )
      }
    }
  }
</script>

<style>

</style>
