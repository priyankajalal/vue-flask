<template>
  <div id="app">
    <app-header  ></app-header>      
    <router-view/>
    <app-footer ></app-footer>
  </div>
</template>

<script>
// Imports
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
    components: {
        'app-header': Header,
        'app-footer': Footer
    }
}
</script>

<style>  
</style> 
