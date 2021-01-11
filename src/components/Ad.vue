<template>
  <div>
    <h3>添加用户</h3>
    <hr>
    <el-form :data="user" status-icon  ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="书名" prop="book_name">
        <el-input type="text" v-model="user.book_name" ></el-input>
      </el-form-item>
      <el-form-item label="添加时间" prop="create_time">
        <el-input type="date" v-model="user.create_time"></el-input>
      </el-form-item>
      <el-form-item label="图片" prop="pic">
        <el-input type="file" v-model="user.pic"></el-input>
      </el-form-item>
      <el-form-item label="价格" prop="price">
        <el-input type="text" v-model="user.price"></el-input>
      </el-form-item>
      <el-form-item label="作者" prop="authors">
        <el-input v-model="user.authors"></el-input>
      </el-form-item>
      <el-form-item label="出版社" prop="publish">
        <el-input v-model="user.publish"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="add_user">提交</el-button>

      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
  name: "AddUser",
  data() {
    return {
     user: {
       book_name: '',
       price: '',
       publish: '',
       authors: '',
       pic: '',
       create_time:''
      }
    }
  },
  methods:{
    add_user(){
      this.$axios({
        url:"http://127.0.0.1:8000/app/v2/books/",
        method:'post',
        data:{
          book_name:this.user.book_name,
          price:this.user.price,
          publish:this.user.publish,
          authors:[this.user.authors],
          pic:this.user.pic,
          create_time:this.user.create_time,

        }
      }).then(res=>{
        if (res.data){
          this.$router.go(-1)
        }
      })
    }
  },
}
</script>

<style scoped>
h3{
  color: blue;
}

</style>
