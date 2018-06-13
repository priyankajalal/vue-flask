<template>
<div class ="container">
	<span>Asset Strength</span>
	<table v-for="asset in assets">
		<tr>
			<td>{{asset.symbol}}</td>
			<td>{{asset.score}}</td>
			<td>{{asset.sign}}</td>
		</tr>
	</table>
	
</div>
</template>

<script>

export default {
    
  data() {
    return {
    assets: [
        {
          symbol: "MSFT",
          score: 10,
          sign :"up"
          
        }, {
          symbol: "GOOG",
          score: 9,
          sign :"up"
          
        },
        {
          symbol: "AAPL",
          score: 7,
          sign :"up"
          
        }
      ]
    }
  }
}
	
</script>