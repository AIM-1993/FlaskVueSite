<template>
  <div id="container" class="hello">
    <h2>{{status}}</h2>
    <label class="label">数据来源：聚合数据API</label>
    <hr class="hr"/>
    <table id="table" class="table hover unstriped">
      <thead>
        <tr>
          <th>日期</th>
          <th>星期</th>
          <th>天气情况</th>
          <th>气温</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in table_data" :key="index">
          <td>{{data.date}}</td>
          <td>{{ data.week }}</td>
          <td>{{ data.weather }}</td>
          <td>{{ data.temperature }}</td>
        </tr>
      </tbody>
    </table>
    <button @click="loadChengDuData" class="primary button">获取成都天气</button>
    <button @click="loadShanghaiData" class="primary button">获取上海天气</button>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        status: '请选择要获取的城市',
        city: '',
        table_data: '',
      }
    },

    created: function () {
    },

    methods: {
      loadChengDuData: function () {
        this.status = "loading...";
        var table = this;
        this.$ajax.get('http://localhost:5000/v1/chengdu-weather')
          .then((response) => {
            this.status = "成都"
            this.table_data = response.data.table.result.future
            console.log(response.data.table.result);
          })
          .catch((error) => {
            this.status = "Error occured." + error;
          })
      },
      loadShanghaiData: function () {
        this.status = "loading...";
        var table = this;
        this.$ajax.get('http:///localhost:5000/v1/shanghai-weather')
        .then((response) => {
          this.status = "上海"
          this.table_data = response.data.table.result.future
          console.log('Shanghai');
        })
        .catch((error) => {
          this.status = "Error occured." + error;
        })
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    position: relative;
    line-height: 20px;
    padding: 1.2%;
    margin: 20px 15%;
    background: #1111;
    min-height: 84vh;
  }

  h2 {
    text-align: center;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  table th {
    text-align: center;
  }

  table tr {
    text-align: center;
  }


  tr:hover {
    background:seashell;
    color:steelblue;
  }

  #chart {
    width: 20%;
    height: 20%;
  }

</style>
