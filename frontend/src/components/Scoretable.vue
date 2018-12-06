<template>
  <div id="container" class="hello">
    <h2>{{tableTitle}}</h2>
    <label class="label">最近7天天气情况</label>
    <!--Alert-->
    <div class="callout alert" data-closable v-if="warningFlag">
      <h5>未选择城市或网络错误!</h5>
      <p>请在下方点选需要查询的城市名称，并重试。</p>
      <button @click="resetWarningFlag" class="close-button" aria-label="Dismiss alert" type="button">
        <span>&times;</span>
      </button>
    </div>

    <hr class="hr"/> 
    <div class="grid-x grid-padding-x">
    <fieldset class="large-5 cell">
      <legend>选择城市</legend>
      <input type="radio" name="pokemon" v-model="inputedCity" value="成都" id="pokemonRed" required><label for="pokemonRed">成都</label>
      <input type="radio" name="pokemon" v-model="inputedCity" value="上海" id="pokemonBlue"><label for="pokemonBlue">上海</label>
      <button id="submit" @click="loadData" class="primary button">获取天气</button>
    </fieldset>
    </div>
    <!--近期天气情况表-->
    <table id="table" class="table unstriped">
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
        <tr v-for="(data, index) in tableData" :key="index">
          <td>{{ data.date }}</td>
          <td>{{ data.week }}</td>
          <td>{{ data.weather }}</td>
          <td>{{ data.temperature }}</td>
          <td>{{ data.wind }}</td>
        </tr>
      </tbody>
    </table>

    <!--图表-->
    <div id="chart" v-show="cityChoosed">
      <canvas id="myChart"></canvas>
    </div>

    <!--着装建议表-->
    <div id="clothing" v-show="cityChoosed">
      <h3>今日天气</h3>
      <label class="label" for="clothing">{{ todayData.date_y }}</label>
      <table id="clothing-table" class="table unstriped">
        <thead>
          <th>天气情况</th>
          <th>贴士</th>
        </thead>
        <tbody>
          <tr>
            <td>紫外线强度</td>
            <td>{{ todayData.uv_index }}</td>
          <tr>
          <tr>
            <td>室外温度</td>
            <td>{{ todayData.temperature }}</td>
          </tr>
          <tr>
            <td>旅行</td>
            <td>{{ todayData.travel_index }}</td>
          </tr>
          <tr>
            <td>着装建议</td>
            <td>{{ todayData.dressing_advice }}</td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script>
  import Chart from 'chart.js';
  export default {
    data() {
      return {
        status: '',
        tableTitle: '',
        inputedCity: '',
        tableData: '',
        todayData: '',
        HT: '',
        LT: '',
        cityChoosed: false,
        warningFlag: false
      }
    },

    created: function () {
      this.tableTitle = "城市天气数据查询";
    },
  
    methods: {
      loadData: function () {
        var table = this;
        this.$ajax.get('http://localhost:5000/v1/' + this.inputedCity)
          .then((response) => {
            this.status = "OK"
            this.cityChoosed = true
            this.tableTitle = this.inputedCity
            this.tableData = response.data.table.result.future
            this.todayData = response.data.table.result.today
            console.log(this.todayData);
            this.HT = response.data.HT
            this.LT = response.data.LT
            if (this.inputedCity === '') {
              console.log("excuted.");
          } else {
            this.loadChart();
          }
          })
          .catch((error) => {
            this.warningFlag = true;
            this.status = "Error occured." + error;
            console.log(this.status);
          });

        },

      warning: function () {
        this.warningFlag = true;
      },

      resetWarningFlag: function () {
        this.warningFlag = false;
      },
  
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
                    data: this.LT,
                  },
                  {
                    label: "最高气温",
                    backgroundColor: 'rgba(220, 20, 60, 0.75)',
                    borderColor: 'rgba(220, 20, 60, 0.75)',
                    data: this.HT,
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
    min-height: 86vh;
    font-family: sans-serif;
  }

  h2 {
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  thead tr {
    background:tan;
  }


  tbody tr:hover {
    color:steelblue;
  }

  #chart {
    width: 50%;
    height: 50%;
    display: inline-block;
  }

  #clothing {
    margin: 0% 5%;
    position: absolute;
    display: inline-block;
  }

  #clothing-table {
    margin: 2%;
  }

</style>
