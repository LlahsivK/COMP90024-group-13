<h1><b>Database:</b> topten-location</h1>
<ul>
<h3>•	<b>Design document</b>: locatesent</h3>
<p>
<b>View</b>: locsent

A mapreduce function that finds the top ten most used words in a location, for each sentiment. 

	Eg. {"key":["Ballarat","positive"],"value":[["budget",38],["great",29],["ride",20],["noosa",18],["morrison",17],["back",17],["fire",16],["#actorslife",16],["australia",16],["#ffmvic",15]]}

Top ten most common words tweeted from Ballarat with a positive tweet sentiment.



<h3>•	<b>Design document</b>: location</h3>

<b>View</b>: loctop

A mapreduce function that finds the top ten most used words for a location.

	Eg. {"key":"Ballarat","value":[["budget",38],["great",29],["ride",20],["noosa",18],["morrison",17],["back",17],["fire",16],["#actorslife",16],["australia",16],["#ffmvic",15]]}

Top ten most common words tweeted from Ballarat.



<h3>•	<b>Design document</b>: sentiment</h3>

<b>View</b>: sentsum

A mapreduce function that finds the number of positive, negative and neutral tweets in a location.

	Eg .{"key":"Ballarat","value":{"negative":0,"neutral":0,"positive":4}}
	
Count of positive, negative and neutral tweets from Ballarat.



<h3>•	<b>Design document</b>: unique</h3>

<b>View</b>: sent

A mapreduce function that finds the most common words associated with each sentiment.

	Eg. {"key":"positive","value":[["bay",189],["denise",189],["robinson",189],["photo",186],["cowall",182],["daily",182],["#turningplasterintowow",179],["#distinctlydifferent",171],["#cartoon",163],["#marketing",162]]}

The top ten most frequently used words associated with positive sentiment.
</ul>



<h1><b>Database</b>: final-sentiment</h1>
<ul>
<h3>•	<b>Design document</b>: sentiment</h3>

<b>View</b>: average

A mapreduce function that gives the average sentiment value for a location.

	Eg. {"key":"Ballarat","value":34.53457499999999}, {"key":"Barwon - West","value":37.06759999999999}

Average sentiment values for Ballarat and Barwon-West.
</ul>
</p>

	

