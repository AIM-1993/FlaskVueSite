<template>
  <div id="container" class="hello">
    <h2>{{tableTitle}}</h2>
    <label class="label">最近7天天气情况</label>
    <!--Alert-->
    <div class="callout alert" data-closable v-if="warningFlag">
      <h5>未选择城市!</h5>
      <p>请在下方点选需要查询的城市名称。</p>
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
        <tr v-for="(data, index) in table_data" :key="index">
          <td>{{data.date}}</td>
          <td>{{ data.week }}</td>
          <td>{{ data.weather }}</td>
          <td>{{ data.temperature }}</td>
          <td>{{ data.wind }}</td>
        </tr>
      </tbody>
    </table>

    <div id="chart" v-show="cityChoosed">
      <canvas id="myChart"></canvas>
    </div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        status: '',
        tableTitle: '',
        inputedCity: '',
        table_data: '',
        cityChoosed: false,
        warningFlag: false
      }
    },

    created: function () {
      this.tableTitle = "城市天气数据查询";
    },

    methods: {
      loadData: function () {
        console.log(this.status);
        var table = this;
        this.$ajax.get('http://localhost:5000/v1/' + this.inputedCity)
          .then((response) => {
            this.status = "OK";
            this.cityChoosed = true;
            this.tableTitle = this.inputedCity;
            this.table_data = response.data.table.result.future;
            console.log(response.data.table.result);
          })
          .catch((error) => {
            this.status = "Error occured." + error;
            console.log(this.status);
          });
          if (this.inputedCity === '') {
            this.warning();
          } else {
          this.loadChart();
          }
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
  }

</style>
