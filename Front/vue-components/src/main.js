import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

import Axios from 'axios'

// Only import what you need!
import { UserPlusIcon, KeyIcon, TerminalIcon } from 'vue-feather-icons'

let globalComponents = []
globalComponents = globalComponents.concat([UserPlusIcon, KeyIcon, TerminalIcon]) // feather icons

globalComponents.forEach(component => {
    Vue.component(component.name, component)
})

const axiosService = Axios.create(
    {
        baseURL: 'http://localhost:8000/api',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    }
)

axiosService.interceptors.request.use(
    config => {
        if (store.state.authToken) {
            config.headers['Authorization'] = `Bearer ${store.state.authToken}`
        }
        return config
    }, error => {
        Promise.reject(error)
    }
)

Vue.prototype.$http = axiosService

Vue.config.productionTip = false

new Vue({
    router,
    store,
    vuetify,
    render: function (h) { return h(App) },
}).$mount('#app')
