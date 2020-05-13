import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/pages/Main'
import Meme from '@/pages/Meme'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/meme/:id',
      name: 'Meme',
      component: Meme,
      props: true
    }
  ]
})
