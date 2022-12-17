import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DinoMenuView from '../views/DinoMenuView.vue'
import JeepMenuVue from '../views/JeepMenuVue.vue'
import RecintoMenuView from '../views/RecintoMenuView.vue'
import NewJeep from '../views/NewJeep.vue'
import QuitJeepRuta from '../views/QuitJeepRuta.vue'
import NewDino from '../views/NewDino.vue'
import AddJeepRuta from '../views/AddJeepRuta.vue'
import DeleteJeep from '../views/DeleteJeep.vue'
import ModifyJeep from '../views/ModifyJeep.vue'


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
    component: JeepMenuVue
  },
  {
    path: '/recintomenu',
    name: 'recintomenu',
    component: RecintoMenuView
  },
  {
    path: '/newjeep',
    name: 'newjeep',
    component: NewJeep
  },
  {
    path: '/quitJeepRuta',
    name: 'quitJeepRuta',
    component: QuitJeepRuta
  },
  {
    path: '/newdino',
    name: 'newdino',
    component: NewDino
  },
  {
    path: '/addJeepRuta',
    name: 'addJeepRuta',
    component: AddJeepRuta
  },
  {
    path: '/deleteJeep',
    name: 'deleteJeep',
    component: DeleteJeep
  },
  {
    path: '/modifyJeep',
    name: 'modifyJeep',
    component: ModifyJeep
  },



]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
