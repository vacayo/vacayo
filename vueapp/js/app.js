import Vue from 'vue/dist/vue.js'
import Vuex from 'vuex'
import VueMask from 'v-mask'
import VueRouter from 'vue-router'
import VueSticky from 'vue-sticky'
import VueMultianalytics from 'vue-multianalytics'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-default/index.css'
import RegistrationApp from './components/registration/app.vue'

Vue.use(ElementUI, { locale });
Vue.use(Vuex);
Vue.use(VueMask);
Vue.use(VueRouter);
Vue.use(VueMultianalytics, {
  modules: {
    mixpanel: {
      token: 'YOUR_TOKEN'
    }
  }
});

Vue.directive('sticky', VueSticky)

const store = new Vuex.Store({
  state: {
    address: '',
    bedrooms: 1,
    bathrooms: 1,
    home_type: '',
    home_size: '',
    last_rent: '',
    available_date: '',
    first_name: '',
    last_name: '',
    phone: '',
    email: '',
    quote: 'PENDING'
  },
  mutations: {
    setAddress (state, address) {
      state.address = address
    },
    setBedrooms (state, bedrooms) {
      state.bedrooms = bedrooms
    },
    setBathrooms (state, bathrooms) {
      state.bathrooms = bathrooms
    },
    setHomeType (state, home_type) {
      state.home_type = home_type
    },
    setHomeSize (state, home_size) {
      state.home_size = home_size
    },
    setLastRent (state, last_rent) {
      state.last_rent = last_rent
    },
    setAvailableDate (state, available_date) {
      state.available_date = available_date
    },
    setFirstName (state, first_name) {
      state.first_name = first_name
    },
    setLastName (state, last_name) {
      state.last_name = last_name
    },
    setPhone (state, phone) {
      state.phone = phone
    },
    setEmail (state, email) {
      state.email = email
    },
    setQuote (state, quote) {
      state.quote = quote
    },
  }
});

const router = new VueRouter({
  routes: [
    { path: '/register', component: RegistrationApp },
  ]
});

new Vue({
  store,
  router,
  el: "#app",
  data: {
    currentView: 'registration-app'
  },
  components: {
    'registration-app': RegistrationApp
  }
});