import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axiosAuth from './axios-auth'
import vuetify from './plugins/vuetify'

// Only import what you need!
import { UserPlusIcon, KeyIcon, TerminalIcon,
    LayersIcon, Edit3Icon, SaveIcon, SendIcon, UserIcon, PlusCircleIcon,
} from 'vue-feather-icons' // feather icons

let globalComponents = []
globalComponents = globalComponents.concat([
    UserPlusIcon, KeyIcon, TerminalIcon, LayersIcon,
    Edit3Icon, SaveIcon, SendIcon, UserIcon, PlusCircleIcon]) // feather icons

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
