<template>
<div class="container" id="app-jokes">
   <h2>Click the button to get Random jokes</h2>
        <button id="btn" class="" v-on:click="getJokes">Get Jokes</button>
            <table v-for="joke in jokes">
              <tr>
              <td>{{ joke.symbol }}</td>
              <td>{{ joke.exchange }}</td>
               <td>{{ joke.companyname }}</td>
              </tr>
            </table>
  </div>
</template>
<script >
  
import axios from 'axios';
  
export default {
  data () {
    return {
      jokes: [],
      loading: false
    }
  }, 
  methods: {
    getJokes: function () {
      this.loading = true;
      axios.get("http://localhost:5000/symbol/msft,goog,aapl")
      .then((response)  =>  {
        this.loading = false;
        this.jokes = response.data;
      }, (error)  =>  {
        this.loading = false;
      })
    }
  },
}
</script>
