<template>
  <!-- Nav -->
  <div id="nav">
    <ul id="navbar" class="menu align-right">
      <li v-for="(item, index) in navbar_items" v-html="item.message" :key="index"></li>
    </ul>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        navbar_items: [
          {
            message: '<a href="#">Home</a>'
          },
          {
            message: '<a href="#">Features</a>'
          },
          {
            message: '<a href="#">Pricing</a>'
          }
        ]
      }
    }
  }

</script>


<style scoped>
  #nav {
    background: #050404;
    padding: 12px;
  }
</style>
