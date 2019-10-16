import Vue from 'vue'
import Vuex from 'vuex'
import http from './axios-auth'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authToken: null,
        authUserPath: null,
        users: {},
        ongoingRequest: [],
    },
    mutations: {
        set_userpath_and_token(state, userpathAndToken) {
            state.authToken = userpathAndToken.token
            state.authUserPath = userpathAndToken.userPath
        },
        'add-user': (state, user) => {
            // state.users[user.url] = user
            state.users = Object.assign({}, state.users, { [user.url]: user })
        },
    },
    actions: {
        login({ commit, dispatch }, userpathAndToken) {
            localStorage.setItem('userpathAndToken', JSON.stringify(userpathAndToken))
            commit('set_userpath_and_token', userpathAndToken)
            dispatch('check-user', userpathAndToken.userPath)
        },
        logout({ commit }) {
            localStorage.removeItem('userpathAndToken')
            commit('set_userpath_and_token', { UserPath: null, token: null })
        },
        stored_login({ dispatch }) {
            let userpathAndToken = JSON.parse(localStorage.getItem('userpathAndToken'))
            if (userpathAndToken) {
                dispatch('login', userpathAndToken)
            }
        },
        'check-user': ({ commit, state }, userPath) => {
            if (!state.users[userPath] && state.ongoingRequest.indexOf(userPath) === -1) {
                state.ongoingRequest.push(userPath)
                http.get(userPath).then(response => {
                    let user = response.data
                    user = http.toRelative(user, ['url', 'post_set'])
                    http.get(`/user_lottie/${user.id}`)
                        .then(response => { user.lottie = JSON.parse(response.data.lottie_json) })
                        .catch(() => {})
                        .finally(() => {
                            state.ongoingRequest.splice(state.ongoingRequest.indexOf(userPath), 1)
                            commit('add-user', user)
                        })
                })
            }
        },
    },
})
