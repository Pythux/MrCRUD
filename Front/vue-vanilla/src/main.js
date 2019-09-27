import Vue from 'vue'
import Axios from 'axios'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

const token = 'eyJpZCI6OCwiaWF0IjoxNTY5NTYwMTI3fQ.0FEhoqKbSKlXF_778uGKNK-SJ7VYSOjh4lAwJ0IZNWE'
Vue.prototype.$http = Axios.create(
    {
        baseURL: 'http://localhost:8000/api',
        headers: {
            Authorization: `Bearer ${token}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    }
)

new Vue({
    router,
    render: function (h) { return h(App) },
}).$mount('#app')
