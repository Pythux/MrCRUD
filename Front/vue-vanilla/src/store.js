import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        toasts: [],
        toast_id_count: 0,
    },
    mutations: {
        toast (state, toast) {
            state.toasts.push(toast)
        },
        delete_toast ({ toasts }, id) {
            let index = toasts.findIndex(toast => toast.id === id)
            if (index !== -1) {
                toasts.splice(index, 1)
            }
        },
    },
    actions: {
        toast ({ commit, state }, toast) {
            toast.id = state.toast_id_count++
            commit('toast', toast)
            setTimeout(() => {
                commit('delete_toast', toast.id)
            }, 6000)
        },
    },
})
