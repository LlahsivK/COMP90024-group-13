**Most tweeted words in a location, for each sentiment
**
**Map**
```
function (doc) {
  emit([doc.location, doc.overall_sentiment], doc.most_common);
}
```

**Reduce**
```
function (keys, values, rereduce) {
  var merged = [];
  merged = [].concat.apply([], values);  
  merged.sort(function(a,b){return b[1] > a[1];});
  var ten = [];
  for (let i =0; i<10;i++){
    ten.push(merged[i]);
  }
  return ten;
}
```
