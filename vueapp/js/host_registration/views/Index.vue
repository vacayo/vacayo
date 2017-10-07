<template>
  <div class="card card-shadow text-center">
    <div class="panel">
      <div class="panel-body text-justify"><h2>GET READY TO MEET YOUR GUESTS</h2></div>
    </div>

    <div class="panel">
      <div class="panel-body text-justify">

        <div>
          <h3>Sign up to become an Airbnb host</h3>
          <p>Start by creating your listing. It’s like a profile page for your place.</p>
          <ul class="row">
            <li class="col-sm-4">What’s in a listing?</li>
            <li class="col-sm-4">Who can book</li>
            <li class="col-sm-4">We’re here to help</li>
          </ul>
        </div>

        <div>
          <h3>Guests find your Airbnb listing and make a reservation</h3>
          <p>You’ll get a reservation confirmation and a message from your guest.</p>
          <ul class="row">
            <li class="col-sm-4">Message your guests</li>
            <li class="col-sm-4">Plan for check-in</li>
          </ul>
        </div>

        <div>
          <h3>Welcome your guests</h3>
          <p>Some hosts offer breakfast, others are more hands-off. How you host is up to you.</p>
          <ul class="row">
            <li class="col-sm-4">Start with the basics</li>
            <li class="col-sm-4">How guests pay</li>
            <li class="col-sm-4">How you get paid</li>
            <li class="col-sm-4">Earnings and fees</li>
            <li class="col-sm-4">What to charge</li>
          </ul>
        </div>

      </div>
      <div class="panel-footer">
        <button type="button" class="btn" @click="register">
          <span>Register!</span>
        </button>
      </div>
    </div>


  </div>
</template>

<script type="text/babel">
  export default {
    props: ['user'],
    methods: {
      register() {
        if (this.user) {
          return this.$router.push('agreement')
        }
        window.location.href = '/accounts/signup/?next=/host#/agreement';
      }
    }
  }
</script>

<style></style>
