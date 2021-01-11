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
            width="120">
          </el-table-column>
          <el-table-column
            prop="get_pic"
            label="图片"
            width="250">
          </el-table-column>

          <el-table-column
            prop="create_time"
            label="添加时间"
            width="270">
          </el-table-column>

        </el-table>



      </el-main>
    </el-container>

  </div>
</template>

<script>
export default {
  name: "Show_user",
  data(){
    return{
book_list:[]
    }
  },
  created() {
    let id=this.$route.query.id;
    this.$axios({
      url: "http://127.0.0.1:8000/app/v2/books/"+id+"/",
      method: "get",

    }).then(response=>{
      // 请求成功后可以走到这个回调函数
      console.log(response.data.results)
      this.book_list = [response.data.results];
    }).catch(error=>{
      // 失败了走这个回调函数
      console.log(error, "1111");
    })


  },
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
