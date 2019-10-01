import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authToken: null,
    },
    mutations: {
        set_authToken (state, newToken) { state.authToken = newToken },
    },
    actions: {
    },
})
