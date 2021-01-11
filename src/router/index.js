import Vue from 'vue'
import Router from 'vue-router'
import First from "../components/First";
import Show_user from "../components/Show_user";
import Update from "../components/Update";
import Ad from "../components/Ad";

Vue.use(Router)

export default new Router({
  routes: [
    {path: "/user", component:First},
    {path: "/add1", component:Ad},
    {path: "/usershow", component: Show_user},
    {path: "/update", component: Update},
    {path: "/", redirect: "/user"},
    {path: "/*", redirect: "/user"},

  ]
})
