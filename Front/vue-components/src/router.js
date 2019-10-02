import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            components: { default: () => import('./views/Home.vue'), header: () => import('./views/Header.vue') },
        },
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

router.beforeEach((to, from, next) => {
    if (localStorage.getItem('usernameAndToken')) {
        store.dispatch('stored_login')
    }
    let isAuth = store.state.authToken
    let goAuth = to.name === 'login' || to.name === 'sign-in'
    if (isAuth && goAuth) {
        next({ name: 'home' })
        return
    }
    if (!isAuth && !goAuth) {
        next({ name: 'login', params: { action: 'login' } })
        return
    }
    next()
})

export default router
