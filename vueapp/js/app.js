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
    },
    owner: {
      first_name: '',
      last_name: '',
      phone: '',
      email: '',
    },
    quote: 'PENDING'
  },
  mutations: {
    updateProperty: function (state, property) {
      Object.assign(state.property, property);
    },
    updateOwner: function (state, owner) {
      Object.assign(state.owner, owner);
    },
    updateQuote (state, quote) {
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