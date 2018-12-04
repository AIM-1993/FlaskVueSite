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
            message: '<a href="#">Dashboard</a>'
          },
          {
            message: '<a href="#">About</a>'
          }
        ]
      }
    }
  }

</script>

<style>
  #nav {
    background: #0d0d0d;
    padding: 12px;
    
  }

  #nav a {
    color:azure;
  }

  #nav a:hover {
	  color: aqua;
  }
</style>
