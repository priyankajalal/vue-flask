import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Survey from '@/components/Survey'
import PageNotFound from '@/components/PageNotFound.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/survey',
      name: 'Survey',
      component: Survey
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
     { 
     	path: "*", 
     component: PageNotFound 
 }
  ],
  mode: 'history'
})
