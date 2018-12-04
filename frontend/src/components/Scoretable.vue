<template>
  <div id="container" class="hello">
    <h2>{{city}}</h2>
    <label class="label">最近7天天气情况</label>
    <hr class="hr"/>
    <label for="">目前能够查询的城市仅有：</label>
    <ul>
      <li>成都</li>
      <li>上海</li>
    </ul>
    <table id="table" class="table hover unstriped">
      <thead>
        <tr>
          <th>日期</th>
          <th>星期</th>
          <th>天气情况</th>
          <th>气温</th>
          <th>风力</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in table_data" :key="index">
          <td>{{data.date}}</td>
          <td>{{ data.week }}</td>
          <td>{{ data.weather }}</td>
          <td>{{ data.temperature }}</td>
          <td>{{ data.wind }}</td>
        </tr>
      </tbody>
    </table>
    <div width="20%" height="20%">
      <canvas id="myChart"></canvas>
    </div>
    <input class="input form-control medium-6 cell" v-model="input_city" type="text" placeholder="请输入想要查询的城市名"/>
    <button @click="loadData" class="primary button">获取天气</button>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        status: '',
        city: '',
        input_city: '',
        table_data: '',
      }
    },

    created: function () {
      this.city = "天气查询";
    },

    methods: {
      loadData: function () {
        this.status = "数据获取成功!";
        console.log(this.status);
        var table = this;
        this.$ajax.get('http://localhost:5000/v1/' + this.input_city)
          .then((response) => {
            this.status = this.city;
            this.table_data = response.data.table.result.future;
            console.log(response.data.table.result);
          })
          .catch((error) => {
            this.status = "Error occured." + error;
            console.log(this.status);
          });

        if ((this.input_city === '') || (this.input_city in ['成都', '上海'] === false)) {
          alert("请输入正确内容！");
        } else {
            this.loadChart();
        }

      },

    // loadShanghaiData: function () {
    //   this.status = "loading...";
    //   var table = this;
    //   this.$ajax.get('http:///localhost:5000/v1/shanghai-weather')
    //   .then((response) => {
    //     this.status = this.city;
    //     this.table_data = response.data.table.result.future;
    //     console.log('Shanghai');
    //   })
    //   .catch((error) => {
    //     this.status = "Error occured." + error;
    //   })
    // },

    loadChart: function () {
      var ctx = document.getElementById('myChart').getContext('2d');
      var chart = new Chart(ctx, {
          // The type of chart we want to create
          type: 'line',

          // The data for our dataset
          data: {
              title: "温度走势图",
              labels: ["星期二", "星期三", "星期四", "星期五", "星期六", "星期天", "星期一"],
              datasets: [
                {
                  label: "最低气温",
                  backgroundColor: 'rgba(	0, 191, 255, 0.75)',
                  borderColor: 'rgb(0, 191, 255)',
                  data: [8, 7, 4, 3, 3, 7, 3],
                },
                {
                  label: "最高气温",
                  backgroundColor: 'rgba(220, 20, 60, 0.75)',
                  borderColor: 'rgba(220, 20, 60, 0.75)',
                  data: [12, 11, 10, 8, 6, 11, 8],
                },
              ]
          },

          // Configuration options go here
          options: {}
        });
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
    font-family: sans-serif;
  }

  h2 {
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  table th {
    text-align: center;
  }

  table tr {
    text-align: center;
  }


  tr:hover {
    background:tan;
    color:steelblue;
  }

  #chart {
    width: 20%;
    height: 20%;
  }

</style>
