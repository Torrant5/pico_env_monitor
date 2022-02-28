<template>
  <div id="app">

    <b-navbar class="p-1" sticky
     style="background: rgba(0, 0, 0, 0.603)">
        <b-navbar-brand href="#" class="ml-5">
          <h1 style="color:aliceblue" class="m-0">Pico Env Monitor</h1>
        </b-navbar-brand>
    </b-navbar>

    <ChartsContainer />

  </div>
</template>

<script>
import ChartsContainer from './components/ChartsContainer.vue'

export default {
  name: 'App',
  components: {
    ChartsContainer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#footer {
  background-color: #888;
}
</style>
