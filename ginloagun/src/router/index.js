import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '../views/signup.vue'
import edit from '../views/edit-profile.vue'
import home from '../views/Home.vue'
import CusHome from '../views/cus-home.vue'
import profile from '../views/profile.vue'
import login from '../views/login.vue'
import refeel from '../views/refeel.vue'
import reserve from '../views/reserve.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/edit',
    name: 'edit',
    component: edit,
    meta: {
      isSecured: true
    }
  },
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/cus-home',
    name: 'CusHome',
    component: CusHome
  },
  {
    path: '/profile',
    name: 'profile',
    component: profile,
    meta: {
      isSecured: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/refeel',
    name: 'refeel',
    component: refeel,
    meta: {
      isSecured: true
    }
  },
  {
    path: '/reserve',
    name: 'reserve',
    component: reserve,
    meta: {
      isSecured: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.isSecured)) {
    var userid = localStorage.getItem("USERNAME")
    if (userid !== null) {
      next() 
    } else {
      next("/");
    }
  } else {
    next();
  }
});

export default router
