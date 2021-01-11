<template>
<div>
  <el-container>
    <el-header>用户页</el-header>
    <el-main>
      <el-table
        :data="book_list"
        height="250"
        border
        style="width: 100%">
        <el-table-column
          prop="id"
          label="ID"
          width="50">
        </el-table-column>
        <el-table-column
          prop="book_name"
          label="书名"
          width="150">
        </el-table-column>
        <el-table-column
          prop="price"
          label="价格"
          width="80">
        </el-table-column>
        <el-table-column
          prop="get_pic"
          label="图片"
          width="200">
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="添加时间"
          width="220">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="350">
          <template slot-scope="scope">
            <el-button type="success" @click="add1(scope.row.id)" class="el-icon-circle-plus" size="small">增加</el-button>
            <el-button @click="sho(scope.row.id)" type="primary" class="el-icon-reading" size="small">查看</el-button>
            <el-button @click="dell(scope.row.id)" type="danger" class="el-icon-delete" size="small">删除</el-button>
            <el-button type="warning" @click="upda(scope.row.id)" class="el-icon-edit" size="small">修改</el-button>
          </template>
        </el-table-column>
      </el-table>




    </el-main>
  </el-container>

</div>
</template>

<script>
export default {
  name: "First",
  methods:{
    sho(row){
      this.$message ({
        message: '查看成功',
        type: 'success',
        showClose: true,
        duration: 1000,
      });
      this.$router.push({path: "/usershow?id=" + row,
      })
    },
    add1(row){
      this.$message ({
        message: '跳转添加页面',
        type: 'success',
        showClose: true,
        duration: 1000,
      });
      this.$router.push({path: "/add1",
      })
    },
    dell(row){
      this.$axios({
        url: "http://127.0.0.1:8000/app/v2/books/ "+row+"/",
        method: "delete",
        // data:{
        //   id:row
        // }

      }).then(res=>{
        // 请求成功后可以走到这个回调函数
        if(res.data){
          this.$router.go(0)
          alert('删除成功')

        }
      }).catch(error=>{
        // 失败了走这个回调函数
        console.log(error, "1111");
      })



    },
    upda(row){
      this.$message({
        message: '跳转修改页面',
        type: 'success',
        showClose: true,
        duration: 1000,
      });
      this.$router.push({path: "/update?id=" + row,
      })
      },

  },


  created() {
    //查询所有用户
    this.$axios({
      url: "http://127.0.0.1:8000/app/v2/books/",
      method: "get",
    }).then(response=>{
      // 请求成功后可以走到这个回调函数
      console.log(response.data)
      this.book_list = response.data.results;
    }).catch(error=>{
      // 失败了走这个回调函数
      console.log(error, "1111");
    })

  } ,

  data() {
    return {
      book_list: [],
    }
  }

}
</script>

<style scoped>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 30px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
