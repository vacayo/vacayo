import Vue from 'vue/dist/vue'
import VueRouter from 'vue-router'
import styles from '../../scss/styles.scss'
import routes from './routes'

Vue.use(VueRouter);

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