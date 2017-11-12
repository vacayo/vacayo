import Vue from 'vue/dist/vue'
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate';
import { Validator } from 'vee-validate';
//import styles from '../../scss/styles.scss'
import routes from './routes'

Vue.use(VueRouter);
Vue.use(VeeValidate);

const dictionary = {
  en: {
    messages:{
      required: () => 'This field is required.'
    }
  }
};

Validator.updateDictionary(dictionary);

const router = new VueRouter({
  mode: 'hash',
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: routes
});

new Vue({
  el: "#app",
  router,
  template: "<router-view></router-view>"
});