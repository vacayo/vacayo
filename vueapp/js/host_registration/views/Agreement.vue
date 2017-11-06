<template>
  <div class="card card-shadow text-center">
    <div class="panel">
      <div class="panel-body text-justify">
        <h3 class="panel-title text-center">VACAYO “SUPERHOST” MANAGEMENT AGREEMENT</h3>
        <p>This Agreement is made and entered into this <span class="highlight">{{ start_date.format('Do') }} day of {{ start_date.format('MMMM') }}, {{ start_date.format('YYYY') }}</span> between <span class="highlight">{{ user.first_name }} {{ user.last_name }}</span> (Superhost) and Vacayo Inc.</p>
        <p>Vacayo employs the services of Superhost <span class="highlight">{{ user.first_name }} {{ user.last_name }}</span> to manage cleaning, repairs and emergency services of assigned Vacayo properties.</p>
        <p>Responsibilities of Superhost. Vacayo hereby appoints “Superhost” as his lawful agent with full authority to do any and all lawful things necessary for the fulfillment of this Agreement, including the following:</p>
        <p>A. Collection and Disbursement. Vacayo agrees to collect all rents as they become due; to render to Superhost a monthly accounting of rents received on vacation rental platforms, less any sums paid out. Vacayo agrees to collect the rents from the tenant and to disburse funds by ordinary mail or as instructed by the “Superhost” on or before the 15th day of the current month, provided, however, that the rent has been received from the tenant.</p>
        <p>B. Maintenance and Labor. “Superhost” agrees to manage cleaning services, guest checkins, maintain, and to repair the property and to hire and to supervise all employees and other needed labor. Superhost agrees to maintain the property in excellent working order.</p>
        <p>C. Advertisement and Legal Proceedings. Vacayo agrees to advertise for tenants, screen tenants and select tenants of suitable credit worthiness. Vacayo will set rents that in the opinion of the Vacayo at the time of the rent negotiations with the tenant, reflect the market conditions of that time and approximate rents of comparable rental</p>
        <p>Compensation of Superhost. Vacayo agrees to compensate “Superhost” as follows. Vacayo agrees to pay the Superhost an amount equal to ten (10%) percent of revenue from the vacation rental online platform plus any repair expenses, may be reimbursed by Vacayo to “Superhost”.</p>
        <p>Term of Agreement. This Agreement shall be effective as of the <span class="highlight">{{ start_date.format('Do') }} day of {{ start_date.format('MMMM') }}, {{ start_date.format('YYYY') }}</span> and shall expire on the <span class="highlight">{{ end_date.format('Do') }} day of {{ end_date.format('MMMM') }}, {{ end_date.format('YYYY') }}</span>. Upon expiration of the above initial term, this Agreement shall automatically be renewed and extended for a like period of time unless terminated in writing by either party by providing written notice 30 days prior to the date for such renewal. This Agreement may also be terminated by mutual agreement of the parties at any time. Upon termination Vacao shall pay to “Superhost” any fees, commissions and expenses due under terms of this Agreement.</p>
        <p>This document represents the entire Agreement between the parties hereto.</p>
        <p>IN WITNESS WHEREOF, the parties hereto hereby execute this Agreement on the date first above written.</p>
      </div>
      <div class="panel-footer">
        <button type="button" class="btn btn-animate btn-animate-side btn-success" @click="agree">
          <span><i class="icon wb-check" aria-hidden="true"></i>I Agree</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
  import moment from 'moment';

  export default {
    data() {
      return {
        start_date: moment(),
        end_date: moment()
      }
    },
    props: ['user'],
    methods: {
      agree() {
        let url  = '/api/host';
        let options = {
          method: "POST",
          credentials: 'same-origin',
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        };

        fetch(url, options)
          .then(
            response => response.json(),
            error => console.log('An error occurred creating your host account:', error)
          )
          .then(
            json => this.$router.push('congrats')
          )
      }
    }
  }
</script>

<style>
  .highlight {
    font-weight: bold;
    text-decoration: underline;
  }
</style>
