<template>
  <div id="app">
    <Navbar/>
    <Scoretable/>
    <Footer/>

  </div>
</template>

<script>
import Navbar from './components/Navbar';
import Scoretable from './components/Scoretable';
import Footer from './components/Footer';


export default {
  name: 'App',
  components: {
    Navbar,
    Scoretable,
    Footer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir'
}
</style>
