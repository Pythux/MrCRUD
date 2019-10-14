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
            components: { default: () => import('./views/List.vue'), header: () => import('./views/Header.vue') },
        },
        {
            path: '/detail/post/:idPost',
            name: 'detail',
            components: { default: () => import('./views/Detail.vue'), header: () => import('./views/Header.vue') },
            props: { default: (route) => { return { pathPost: `/post/${route.params.idPost}` } } },
        }, {
            path: '/create',
            name: 'create',
            components: { default: () => import('./views/Detail.vue'), header: () => import('./views/Header.vue') },
        }, {
            path: '/config',
            name: 'config',
            components: { default: () => import('./views/Config.vue'), header: () => import('./views/Header.vue') },
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
    let isAuth = store.state.authToken
    if ((!isAuth) && localStorage.getItem('usernameAndToken')) {
        store.dispatch('stored_login')
    }
    isAuth = store.state.authToken
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
