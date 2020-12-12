import Vue from 'vue'
import Vuex from 'vuex'
import api from "../service/api";
import { server } from "../service/constants"; 
// import router from "@/router";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loginState: false,
    navBarDefaultState: true,
    dialogState: false,
    dialogMessage: "",
    loading: false
  },
  getters: {
    getLoginState (state) {
      return state.loginState
    },
    getNavBarState (state) {
      return state.navBarDefaultState
    },
    getDialogState (state) {
      return state.dialogState
    },
    getDialogMessage (state) {
      return state.dialogMessage
    },
    getLoadingDialog (state) {
      return state.loading
    }
  },
  mutations: {
    SET_LOGIN_STATE (state, value) {
      state.loginState = value
    },
    SET_NAV_BARDEFAULT_STATE (state, value) {
      state.navBarDefaultState = value
    },
    SET_DIALOG_STATE (state, value) {
      state.dialogState = value
    },
    SET_DIALOG_MESSAGE (state, value) {
      state.dialogMessage = value
    },
    SET_LOADING_STATE (state, value) {
      state.loading = value
    }
  },
  actions: {
    async login ({ commit, dispatch }, { username, password }) {
      commit("SET_LOADING_STATE", true)
      var result = await api.login({ username, password })
      if (result.data.status == "1") {
        localStorage.setItem(server.USERNAME, result.data.result);
        commit("SET_LOGIN_STATE", true)
        commit("SET_NAV_BARDEFAULT_STATE", false)
        commit("SET_LOADING_STATE", false)
      } else {
        commit("SET_LOGIN_STATE", false)
        commit("SET_NAV_BARDEFAULT_STATE", true)
        commit("SET_LOADING_STATE", false)
        dispatch({ type: 'dialog', state: true, msg: result.data.msg })
      }
    },
    logout ({ commit }) {
      localStorage.removeItem(server.USERNAME);
      commit("SET_LOGIN_STATE", false)
      commit("SET_NAV_BARDEFAULT_STATE", true)
    },
    restoreLogin ({ commit }) {
      var result = localStorage.getItem(server.USERNAME)
      if (result !== null) {
        commit("SET_LOGIN_STATE", true)
        commit("SET_NAV_BARDEFAULT_STATE", false)
      } else {
        commit("SET_LOGIN_STATE", false)
        commit("SET_NAV_BARDEFAULT_STATE", true)
      }
    },
    dialog ({ commit }, { state, msg }) {
      commit("SET_DIALOG_STATE", state)
      commit("SET_DIALOG_MESSAGE", msg)
    },
    async register ({ commit, dispatch }, { ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, pic }) {
      commit("SET_LOADING_STATE", true)
      var result = await api.register({ ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, pic })
      if (result.data.status == "1") {
        commit("SET_LOADING_STATE", false)
      } else {
        commit("SET_LOADING_STATE", false)
        dispatch({ type: 'dialog', state: true, msg: result.data.msg })
      }
    },
    async editprofile ({ commit, dispatch }, { ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, pic }) {
      commit("SET_LOADING_STATE", true)
      var result = await api.editprofile({ ssn, fname, lname, username, password, address, email, phoneNumber, birthDay, pic })
      if (result.data.status == "1") {
        commit("SET_LOADING_STATE", false)
      } else {
        commit("SET_LOADING_STATE", false)
        dispatch({ type: 'dialog', state: true, msg: result.data.msg })
      }
    },
    async reserve ({ commit, dispatch }, { ssn, rid, createDate, tableAmount, detail }) {
      commit("SET_LOADING_STATE", true)
      var result = await api.createReservation({ ssn, rid, createDate, tableAmount, detail })
      if (result.data.status == "1") {
        commit("SET_LOADING_STATE", false)
      } else {
        commit("SET_LOADING_STATE", false)
        dispatch({ type: 'dialog', state: true, msg: result.data.msg })
      }
    },
  },
})
