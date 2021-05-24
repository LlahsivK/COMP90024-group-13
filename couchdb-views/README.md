**Database**: topten-location

•	**Design document**: locatesent

**View**: locsent

A mapreduce function that finds the top ten most used words in a location, for each sentiment. 

_Eg. {"key":["Ballarat","positive"],"value":[["budget",38],["great",29],["ride",20],["noosa",18],["morrison",17],["back",17],["fire",16],["#actorslife",16],["australia",16],["#ffmvic",15]]}_ 

Top ten most common words tweeted from Ballarat with a positive tweet sentiment.

•	**Design document**: location

**View**: loctop

A mapreduce function that finds the top ten most used words for a location.
_Eg. {"key":"Ballarat","value":[["budget",38],["great",29],["ride",20],["noosa",18],["morrison",17],["back",17],["fire",16],["#actorslife",16],["australia",16],["#ffmvic",15]]
_
Top ten most common words tweeted from Ballarat.


•	**Design document**: sentiment

**View**: sentsum

A mapreduce function that finds the number of positive, negative and neutral tweets in a location.

_Eg .{"key":"Ballarat","value":{"negative":0,"neutral":0,"positive":4}}
_
Count of positive, negative and neutral tweets from Ballarat.


•	**Design document**: unique

**View**: sent

A mapreduce function that finds the most common words associated with each sentiment.

_Eg. {"key":"positive","value":[["bay",189],["denise",189],["robinson",189],["photo",186],["cowall",182],["daily",182],["#turningplasterintowow",179],["#distinctlydifferent",171],["#cartoon",163],["#marketing",162]]}_

The top ten most frequently used words associated with positive sentiment.


**Database**: final-sentiment

•	**Design document**: sentiment

**View**: average

A mapreduce function that gives the average sentiment value for a location.

_Eg. {"key":"Ballarat","value":34.53457499999999},
{"key":"Barwon - West","value":37.06759999999999}_

Average sentiment values for Ballarat and Barwon-West.


	

