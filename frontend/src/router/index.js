import Vue from 'vue'
import VueRouter from 'vue-router'
import ProfileVue from "../views/Profile";
import ItemList from "../views/ItemList";
import AddItem from "../views/AddItem";
import ItemDetail from "../views/ItemDetail";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: ItemList
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/profile',
        name: 'profile',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: ProfileVue
    },

    {
        path: '/add-item',
        name: 'add-item',
        component: AddItem
    },
    {
        path: '/item-list',
        name: 'item-list',
        component: ItemList
    },
    {
        path: '/item-list/detail/:id',
        name: 'item-detail',
        component: ItemDetail
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
