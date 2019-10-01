import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/login',
            name: 'login',
            components: { default: () => import('./views/Login.vue') },
            props: { default: { action: 'login' } },
        },
        {
            path: '/sign-in',
            name: 'sign-in',
            components: { default: () => import('./views/Login.vue') },
            props: { default: { action: 'sign-in' } },
        },
    ],
})
