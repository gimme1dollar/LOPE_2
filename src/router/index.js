import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/pages/Main'
import MemeDetail from '@/pages/MemeDetail'
import MemeList from '@/pages/MemeList'

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
      component: MemeDetail,
      props: true
    },
    {
      path: '/meme',
      name: 'MemeList',
      component: MemeList
    }
  ]
})
