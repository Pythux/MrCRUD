import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authToken: null,
        username: null,
    },
    mutations: {
        set_username_and_token(state, usernameAndToken) {
            state.authToken = usernameAndToken.token
            state.username = usernameAndToken.username
        },
    },
    actions: {
        login({ commit }, usernameAndToken) {
            localStorage.setItem('usernameAndToken', JSON.stringify(usernameAndToken))
            commit('set_username_and_token', usernameAndToken)
        },
        logout({ commit }) {
            localStorage.removeItem('usernameAndToken')
            commit('set_username_and_token', { username: null, token: null })
        },
        stored_login({ dispatch }) {
            let usernameAndToken = JSON.parse(localStorage.getItem('usernameAndToken'))
            if (usernameAndToken) {
                dispatch('login', usernameAndToken)
            }
        },
    },
})
