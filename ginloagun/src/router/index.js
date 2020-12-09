import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/login.vue'
import profile from '../views/profile.vue'
import signup from '../views/signup.vue'
import editprofile from '../views/edit-profile.vue'
import cushome from '../views/cus-home.vue'
import reserve from '../views/reserve.vue'
import zyn from '../views/zyn.vue'
import refeel from '../views/refeel.vue'
import cminor from '../views/cminor.vue'
import toget from '../views/toget.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/profile',
    name: 'profile',
    component: profile
  },
  {
    path: '/signup',
    name: 'signup',
    component: signup
  },
  {
    path: '/edit-profile',
    name: 'edit-profil',
    component: editprofile
  },
  {
    path: '/cus-home',
    name: 'cus-homr',
    component: cushome
  },
  {
    path: '/reserve/refeel',
    name: 'reserve',
    component: reserve
  },
  {
    path: '/zyn/',
    name: 'zyn',
    component: zyn
  },
  {
    path: '/refeel/',
    name: 'refeel',
    component: refeel
  },
  {
    path: '/cminor/',
    name: 'cminor',
    component: cminor
  },
  {
    path: '/toget/',
    name: 'toget',
    component: toget
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
