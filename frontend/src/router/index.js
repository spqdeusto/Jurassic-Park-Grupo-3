import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DinoMenuView from '../views/DinoMenuView.vue'
import JeepMenuView from '../views/JeepMenuView.vue'
import RecintoMenuView from '../views/RecintoMenuView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dinomenu',
    name: 'dinomenu',
    component: DinoMenuView
  },
  {
    path: '/jeepmenu',
    name: 'jeepmenu',
    component: JeepMenuView
  },
  {
    path: '/recintomenu',
    name: 'recintomenu',
    component: RecintoMenuView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
