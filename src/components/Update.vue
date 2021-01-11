<template>
<div>
  <el-row :gutter="20">
    <el-col :span="8">
      <div class="grid-content bg-purple">&nbsp;</div>
    </el-col>
    <el-col :span="8">
      <div class="grid-content bg-purple">
        <el-form :model="user_list" status-icon  ref="ruleForm" label-width="100px"
                 class="demo-ruleForm">
          <el-form-item label="ID" prop="id">
            <el-input type="text" v-model="user_list.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="书名" prop="book_name">
            <el-input type="text" v-model="user_list.book_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="添加时间" prop="create_time">
            <el-input  type="date" v-model="user_list.create_time"></el-input>
          </el-form-item>
          <el-form-item label="图片" prop="pic">
            <el-input  type="file" ></el-input>
          </el-form-item>
          <el-form-item label="价格" prop="price">
            <el-input  type="text" v-model="user_list.price"></el-input>
          </el-form-item>
          <el-form-item label="作者" prop="authors" for="(value,key,index) in authors" >
            <el-input  type="text"  v-model="user_list.authors"></el-input>
          </el-form-item>
          <el-form-item label="出版社" prop="publish">
            <el-input  type="text" v-model="user_list.publish"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="add_user('ruleForm')">提交</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-col>

    <el-col :span="8">
      <div class="grid-content bg-purple">&nbsp;</div>
    </el-col>
  </el-row>
</div>
</template>

<script>
export default {
  name: "Update",
    data() {
    return{
      user_list: {
      }
    }

    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      get_emp_by_id() {
        let id = this.$route.query.id;
        this.$axios({
          url: "http://127.0.0.1:8000/app/v2/books/"+id+"/",
          method: 'get',

        }).then(res => {
          console.log(res.data.results)
          this.user_list = res.data.results;
        }).catch(error => {
          console.log(error);
        })
      },
      add_user(){
        this.$axios({
          url:"http://127.0.0.1:8000/app/v2/books/",
          method:'patch',
          data:{
            book_name:this.user.book_name,
            price:this.user.price,
            publish:this.user.publish,
            authors:this.user.authors,
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
    created() {
      this.get_emp_by_id();
    }

}
</script>

<style scoped>

</style>
