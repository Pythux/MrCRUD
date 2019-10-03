import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axiosAuth from './axios-auth'
import vuetify from './plugins/vuetify'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

// Only import what you need!
import { UserPlusIcon, KeyIcon, TerminalIcon, LayersIcon } from 'vue-feather-icons'

let globalComponents = []
globalComponents = globalComponents.concat(
    [UserPlusIcon, KeyIcon, TerminalIcon, LayersIcon]) // feather icons

globalComponents.forEach(component => {
    Vue.component(component.name, component)
})

Vue.prototype.$http = axiosAuth

// Vue.directive('name', Directive) // v-name

new Vue({
    router,
    store,
    vuetify,
    render: function(h) { return h(App) },
}).$mount('#app')

Vue.config.productionTip = false
