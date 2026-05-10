import { createRouter, createWebHistory } from 'vue-router'
import OSMonitor from '../components/OSMonitor.vue'

const routes = [
  { path: '/', component: OSMonitor },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
