import Vue from 'vue'
import Router from 'vue-router'
import Header from './views/Header.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '',
            name: 'home',
            components: {
                default: () => import('./views/List.vue'),
                'header-top': Header,
            },
        }, {
            path: '/detail/:id',
            name: 'detail',
            // props: true,
            props: { default: true },
            components: {
                default: () => import('./views/Detail.vue'),
                'header-top': Header,
            },
        }, {
            path: '/create',
            name: 'create',
            components: {
                default: () => import('./views/CreateUpdate.vue'),
                'header-top': Header,
            },
        }, {

            path: '/update/:id',
            name: 'update',
            // props: true,
            props: { default: true },
            components: {
                default: () => import('./views/CreateUpdate.vue'),
                'header-top': Header,
            },
        }, { path: '*', redirect: { name: 'home' } },
    ],
})
