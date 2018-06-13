<template>  
<div>  
<!---<app-assetscore></app-assetscore>
<app-ninjas v-bind:ninjas="ninjas"></app-ninjas>
<app-survey></app-survey>-->
<news></news>
</div>  
</template>  
<script>

// Imports
import Ninjas from './Ninjas.vue';
import Surveys from './Survey.vue';
import News from './News.vue';
import AssetScore from './AssetScore.vue';
export default {
    components: {
        'app-ninjas': Ninjas,
        'app-survey': Surveys,
        'news' : News,
        'app-assetscore' : AssetScore
    },
  data() {
    return {
    ninjas: [
              {name: 'Ryu', speciality: 'Vue Components', show: false},
              {name: 'Crystal', speciality: 'HTML Wizardry', show: false},
              {name: 'Hitoshi', speciality: 'Click Events', show: false},
              {name: 'Tango', speciality: 'Conditionals', show: false},
              {name: 'Kami', speciality: 'Webpack', show: false},
              {name: 'Yoshi', speciality: 'Data Diggin', show: false}
          ]
    }
  }
}
</script>
