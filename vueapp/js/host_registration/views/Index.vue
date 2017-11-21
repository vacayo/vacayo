<template>
  <div class="superhost-registration">

    <header class="intro-header">
      <div class="container">
        <div class="intro-message">
          <h1>Turn your passion into a Business.</h1>
          <h3>Sign with Vacayo</h3>
          <hr class="intro-divider" />
          <div class="clearfix"></div>
          <button type="button" class="btn btn-vacayo" @click="register">
            <span>BECOME A SUPERHOST</span>
          </button>
          <div class="intro-callout"><h3>We’ll match you with one (or more!) of our vacation rentals homes.</h3></div>
        </div>
      </div>
    </header>

    <section class="content-section-a">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 mr-auto">
            <hr class="section-heading-spacer">
            <div class="clearfix"></div>
            <h2 class="section-heading">You Share Your Skills <br> We Share the Profit</h2>
            <p class="lead">
              Superhosts are entrepreneurs at heart, some just don’t know it yet.
              They embody the spirit of Vacayo and love the challenge of earning 5-star reviews from our guests.
              We make it easy for you to grow your business alongside ours with our hosting dashboard.
              Our Superhosts receive 10% of the profit from every rental they manage.
            </p>
          </div>
          <div class="col-lg-5 ml-auto section-image">
            <img class="img-fluid" src="../../../img/superhost_section1.jpeg" alt="">
          </div>
        </div>
        <div class="row">
          <blockquote class="blockquote cover-quote mt-50">
            Vacayo has allowed me to make a living managing homes, while spending less time than at my last job.
            <footer class="blockquote-footer">Fabi
              <cite title="Source Title">Superhost, MV</cite>
            </footer>
          </blockquote>
        </div>
      </div>
    </section>

    <section class="content-section-b">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 mr-auto section-image">
            <img class="img-fluid" src="../../../img/superhost_section2.jpeg" alt="">
          </div>
          <div class="col-lg-5 ml-auto">
            <hr class="section-heading-spacer">
            <div class="clearfix"></div>
            <h2 class="section-heading">By partnering with Vacayo, you can....</h2>
            <div>
              <ul class="row flex-list">
                <li class="col">
                  <div class="ribbon ribbon-vertical">
                    <span class="ribbon-inner"><i class="icon ti-money" aria-hidden="true"></i></span>
                  </div>
                  <p>Earn more, without having to scout for new landlords</p>
                </li>
                <li class="col">
                  <div class="ribbon ribbon-vertical ribbon-info">
                    <span class="ribbon-inner"><i class="icon ti-home" aria-hidden="true"></i></span>
                  </div>
                  <p>Manage on-the-ground operations for up to 15 properties</p>
                </li>
                <li class="col">
                  <div class="ribbon ribbon-vertical ribbon-danger">
                    <span class="ribbon-inner"><i class="icon ti-calendar" aria-hidden="true"></i></span>
                  </div>
                  <p>Enjoy easy Automatic Payouts into your bank account each Month</p>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section-a">
      <div class="container">
        <div class="row">
          <div class="col-lg-5 mr-auto">
            <hr class="section-heading-spacer">
            <div class="clearfix"></div>
            <h2 class="section-heading">The Perks of Hosting</h2>
            <div>
              <ul class="row flex-list">
                <li class="col-6">
                  <div class="ribbon ribbon-corner ribbon-primary ribbon-reverse ribbon-bottom">
                    <span class="ribbon-inner"><i class="icon ti-stats-down" aria-hidden="true"></i></span>
                  </div>
                  <p>30% friends and family discounts on Vacayo-managed homes</p>
                </li>
                <li class="col-6">
                  <div class="ribbon ribbon-corner ribbon-primary ribbon-bottom">
                    <span class="ribbon-inner"><i class="icon ti-announcement" aria-hidden="true"></i></span>
                  </div>
                  <p>Attend exclusive Vacayo events, conferences and product launches</p>
                </li>
                <li class="col-6">
                  <div class="ribbon ribbon-corner ribbon-primary ribbon-reverse">
                    <span class="ribbon-inner"><i class="icon ti-comments" aria-hidden="true"></i></span>
                  </div>
                  <p>Dedicated, 24/7 hosting team support</p>
                </li>
                <li class="col-6">
                  <div class="ribbon ribbon-corner ribbon-primary">
                    <span class="ribbon-inner"><i class="icon ti-user" aria-hidden="true"></i></span>
                  </div>
                  <p>Access to a warm community of like-minded Superhosts</p>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-6 ml-auto section-image">
            <img class="img-fluid" src="../../../img/superhost_section3.jpeg" alt="">
          </div>
        </div>
      </div>
    </section>

    <section class="content-section-b">
      <div class="container">
        <div class="row">
          <div class="col-xm-4 mx-auto">
            <button type="button" class="btn btn-vacayo" @click="register">
              <span>JOIN NOW</span>
            </button>
          </div>
        </div>
      </div>
    </section>

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
        return this.$router.push('registration')
      }
    }
  }
</script>

<style>
  p.lead {
    font-size: 18px;
    font-family: "Lato", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  }

  .intro-header {
    padding-top: 50px;
    padding-bottom: 50px;
    text-align: center;
    color: #f8f8f8;
    background: url(../../../img/hero_1920x1280.jpeg) no-repeat center center;
    background-size: cover;
  }

  .intro-divider {
    min-width: 200px;
    max-width: 400px;
    float: left;
    border-top: 1px solid #f8f8f8;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  }

  .intro-message {
    position: relative;
    padding-top: 20%;
    padding-bottom: 20%;
    text-align: left;
  }

  .intro-message h1 {
    color: #FFFFFF;
    font-size: 44px;
    font-weight: 700;
    line-height: 56px;
    letter-spacing: -0.8px;
    margin: 0px;
    margin-bottom: 24px;
    max-width: 400px;
  }

  .intro-message h3 {
    color: #FFFFFF;
    font-size: 24px;
    font-weight: 500;
    line-height: 28px;
  }

  @media (min-width: 576px) {
    .intro-message .intro-callout {
      position: absolute !important;
      bottom: -80px !important;
    }
  }

  .intro-message .intro-callout {
    background-color: rgba(255,255,255,0.95);
    border-radius: 4px;
    border: 1px solid #D8D8D8;
    padding: 15px;
    position: relative;
    bottom: -150px;
    width: 100%;
  }

  .intro-message .intro-callout h3 {
    color: rgba(72,72,72,1);
    font-size: 28px;
    font-weight: 500;
    line-height: 32px;
    letter-spacing: -0.6px;
    text-align: center;
  }

  .content-section-a {
    padding: 50px 0;
    background-color: #f8f8f8;
  }

  .content-section-b {
    padding: 50px 0;
    border-top: 1px solid #e7e7e7;
    border-bottom: 1px solid #e7e7e7;
  }

  .section-heading {
    margin-bottom: 30px;
  }

  .section-heading-spacer {
    float: left;
    width: 200px;
    border-top: 3px solid #e7e7e7;
  }

  @media (min-width: 992px) {
    .section-image img {
      padding-top: 55px;
      max-height: 450px;
    }
  }

  ul.flex-list {
    list-style-type: none;
    padding: 0;
  }

  ul.flex-list li {
    min-width: 180px;
    font-size: 14px;
    padding: 50px 15px 15px 50px;
    background-color: #fff;
    border: 1px solid #eee;
  }

  @media (max-width: 991px) {
    ul.flex-list li {
      min-width: 180px;
    }
  }

</style>
