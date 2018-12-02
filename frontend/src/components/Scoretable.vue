<template>
  <div id="container" class="hello">
    <h2>{{status}}</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Birth</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in table_data" :key="index">
          <td>{{ data.name }}</td>
          <td>{{ data.birth }}</td>
          <td>{{ data.score }}</td>
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
        table_data: ''
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
            this.status = response.data.result;
            this.table_data = response.data.data;
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
    min-height: 81vh;
  }

</style>
