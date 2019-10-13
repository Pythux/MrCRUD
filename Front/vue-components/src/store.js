import Vue from 'vue'
import Vuex from 'vuex'
import http from './axios-auth'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authToken: null,
        username: null,
        users: {},
    },
    mutations: {
        set_username_and_token(state, usernameAndToken) {
            state.authToken = usernameAndToken.token
            state.username = usernameAndToken.username
        },
        'add-user': (state, user) => {
            // state.users[user.url] = user
            state.users = Object.assign({}, state.users, { [user.url]: user })
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
        'check-user': ({ commit, state }, userPath) => {
            if (!state.users[userPath]) {
                http.get(userPath).then(response => {
                    let user = response.data
                    user = http.toRelative(user, ['url', 'post_set'])
                    if (!(user.url in state.users)) {
                        // commit('add-user', user)
                        http.get(`/user_lottie/${user.id}`)
                            .then(response => { user.lottie = JSON.parse(response.data.lottie_json) })
                            .finally(() => {
                                commit('add-user', user)
                            })
                    }
                })
            }
        },
    },
})
