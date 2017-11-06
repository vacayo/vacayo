<template>
  <div class="card card-shadow text-center">
    <div class="panel">
      <div class="panel-body text-justify"><h2>Superhosts: Become A Local Property Partner</h2></div>
    </div>

    <div class="panel">
      <div class="panel-body text-justify">

        <div>
          <h3>Turn your passion into a Business. Sign with Vacayo and we’ll match you with one (or more!) of our vacation rentals homes.</h3>
        </div>

        <div>
          <p>Quote Area from current superhosts:</p>
        </div>

        <div>
          <h3>You Share Your Skills, We Share the Profit</h3>
          <p>Superhosts are entrepreneurs at heart—some just don’t know it yet. They embody the spirit of Vacayo and love the challenge of exceeding landlord’s expectations and earning 5-star reviews from our guests. We make it easy for them to grow their business along ours, using our proprietary technology to making hosting seamless. Our Superhosts receive 10% of the profit from every rental they manage.</p>
        </div>

        <div>
          <h3>By partnering with Vacayo, you can....</h3>
          <ul class="row">
            <li class="col-sm-4">Earn more, without having to scout for new landlords</li>
            <li class="col-sm-4">Manage on-the-ground operations for up to 15 properties</li>
            <li class="col-sm-4">Enjoy easy Automatic Payouts into your bank account each Month </li>
          </ul>
        </div>

        <div>
          <h3>Sample of a Dashboard</h3>
        </div>

        <div>
          <h3>The Perks of Hosting:</h3>
          <ul class="row">
            <li class="col-sm-4">30% friends and family discounts on Vacayo-managed homes</li>
            <li class="col-sm-4">Attend exclusive Vacayo events, conferences and product launches</li>
            <li class="col-sm-4">Dedicated, 24/7 hosting team support</li>
            <li class="col-sm-4">Access to a warm community of like-minded Superhosts</li>
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
