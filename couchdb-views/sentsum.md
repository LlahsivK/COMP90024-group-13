**Number of postive, negatice, neutral tweets in each location**

**Map**
```
function (doc) {
  if (doc.overall_sentiment === 'positive'){
    emit(doc.location, {positive: 1, negative: 0, neutral: 0});
  }
  if (doc.overall_sentiment === 'negative'){
    emit(doc.location, {positive: 0, negative: 1, neutral: 0});
  }
  if (doc.overall_sentiment === 'neutral'){
    emit(doc.location, {positive: 0, negative: 0, neutral: 1});
  }  
}
```

**Reduce**
```
_sum
```
