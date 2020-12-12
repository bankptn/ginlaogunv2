<template>
  <v-app>
    <navbarLogin v-if="$store.getters.getLoginState"/>
    <navbar v-if="$store.getters.getNavBarState"/>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

import navbarLogin from './components/core/navbar-signin.vue';
import navbar from './components/core/navbar';

export default {
  name: 'App',
  components: {
    navbarLogin,
    navbar
  },
  mounted () {
    this.$store.dispatch({ type: "restoreLogin" });
  }
};
</script>
