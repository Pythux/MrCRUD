import Vue from 'vue'
import Vuex from 'vuex'
import http from './axios-auth'

Vue.use(Vuex)

export default new Vuex.Store({
    state: () => ({
        authToken: null,
        authUserPath: null,
        users: {},
        ongoingRequest: [],
    }),
    mutations: {
        set_userpath_and_token(state, userpathAndToken) {
            state.authToken = userpathAndToken.token
            state.authUserPath = userpathAndToken.userPath
        },
        'add-user': (state, user) => {
            // state.users[user.url] = user
            state.users = Object.assign({}, state.users, { [user.url]: user })
        },
        'set-user-lottie': (state, { userPath, lottie }) => {
            let user = state.users[userPath]
            user.lottie = lottie
            state.users = Object.assign({}, state.users, { [userPath]: user })
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
        'check-user': ({ commit, state, dispatch }, userPath) => {
            let ongoing = 'check-user, path: ' + userPath
            if (!state.users[userPath] && state.ongoingRequest.indexOf(ongoing) === -1) {
                state.ongoingRequest.push(ongoing)
                http.get(userPath).then(response => {
                    let user = response.data
                    user = http.toRelative(user, ['url', 'post_set'])
                    commit('add-user', user)
                    dispatch('check-user-lottie', userPath)
                }).finally(() => state.ongoingRequest.splice(state.ongoingRequest.indexOf(ongoing), 1))
            }
        },
        'check-user-lottie': ({ commit, state }, userPath) => {
            let ongoing = 'check-user-lottie, path: ' + userPath
            if (state.ongoingRequest.indexOf(ongoing) === -1) {
                state.ongoingRequest.push(ongoing)
                http.get(`/user_lottie/${state.users[userPath].id}`)
                    .then(response => {
                        commit('set-user-lottie', { userPath, lottie: JSON.parse(response.data.lottie_json) })
                    })
                    .catch(() => {})
                    .finally(() => {
                        state.ongoingRequest.splice(state.ongoingRequest.indexOf(ongoing), 1)
                    })
            }
        },
    },
})
