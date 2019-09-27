import Vue from 'vue'
import Axios from 'axios'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

const token = 'eyJpZCI6NSwiaWF0IjoxNTY5MzM2OTU1fQ.RuGZ1K33-t574RU4OX4kuTeR-BdKZTcB8Jvi2Z-0t98'
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
