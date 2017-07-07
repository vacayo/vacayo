import Vue from 'vue/dist/vue.js'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-default/index.css'
import RegistrationApp from './components/registration/app.vue'

Vue.use(ElementUI, { locale });
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    address: '',
    bedrooms: 1,
    bathrooms: 1,
    home_type: '',
    home_size: '',
    last_rent: '',
    date_available: ''
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
    setDateAvailable (state, date_available) {
      state.date_available = date_available
    }
  }
});

new Vue({
  el: "#app",
  store,
  data: {
    currentView: 'registration-app'
  },
  components: {
    'registration-app': RegistrationApp
  }
});