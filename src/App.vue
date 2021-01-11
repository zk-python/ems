<template>
  <div id="app">
    <h3>欢迎访问百知教育信息管理系统</h3>
    <hr>
    <router-link to="/user">用户管理</router-link>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
import First from "./components/First";

export default {
  name: 'App',
  comments:{
    First:First,


  },

}
</script>

<style>
h3{
  color: greenyellow;
}
</style>
