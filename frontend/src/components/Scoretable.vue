<template>
  <div id="container" class="hello">
    <h2>{{status}}</h2>
    <label class="label">数据来源：聚合数据API</label>
    <hr class="hr"/>
    <table id="table" class="table hover unstriped">
      <thead>
        <tr>
          <th>Id</th>
          <th>日期</th>
          <th>空气质量</th>
          <th>AQI指数</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in table_data" :key="index">
          <td>{{index}}</td>
          <td>{{ data.date }}</td>
          <td>{{ data.quality }}</td>
          <td>{{ data.AQI }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        status: 'Connect Success',
        city: '',
        table_data: '',
      }
    },
    created: function () {
      this.loadData();
    },
    methods: {
      loadData: function () {
        this.status = "loading...";
        var table = this;
        this.$ajax.get('http://localhost:5000/')
          .then((response) => {
            this.status = response.data.table.result[0].citynow.city + "近两周空气质量状况表";
            this.table_data = response.data.table.result[0].lastTwoWeeks;
            console.log(response.data.table.result[0].lastTwoWeeks);
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


  #container table tr:hover {
    background:seashell;
  }


</style>
