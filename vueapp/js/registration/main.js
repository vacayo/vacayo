import Vue from 'vue/dist/vue.js'
import Vuex from 'vuex'
import VueMask from 'v-mask'
import VueSticky from 'vue-sticky'
import VueMultianalytics from 'vue-multianalytics'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-default/index.css'
import '../scss/styles.scss'
import App from './App'
import router from './router'

Vue.use(ElementUI, { locale });
Vue.use(Vuex);
Vue.use(VueMask);

Vue.use(VueMultianalytics, {
  modules: {
    mixpanel: {
      token: '756ff338a534b6f3a4f49682546327cc'
    }
  }
});

Vue.directive('sticky', VueSticky);

const store = new Vuex.Store({
  strict: true,
  state: {
    property: {
      address: null,
      bedrooms: 1,
      bathrooms: 1,
      home_type: null,
      home_size: null,
      last_rent: null,
      has_rented: false,
      available_date: null,
      rent_estimate: null,
      rent_estimate_low: null,
      rent_estimate_high: null,
    },
    owner: {
      first_name: '',
      last_name: '',
      phone: '',
      email: '',
    },
  },
  mutations: {
    updateProperty: function (state, property) {
      Object.assign(state.property, property);
    },
    updateOwner: function (state, owner) {
      Object.assign(state.owner, owner);
    },
  }
});

new Vue({
  store,
  router,
  el: "#app",
  template: '<App/>',
  components: { App }
});