<template>
  <div id="app">
    <Navbar/>
    <Scoretable/>

  </div>
</template>

<script>
import Navbar from './components/Navbar';
import Scoretable from './components/Scoretable';


export default {
  name: 'App',
  components: {
    Navbar,
    Scoretable
  }
}
</script>

<style>
#app {
  font-family: 'Avenir'
}
</style>
