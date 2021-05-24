**Average sentiment score associated with a location**

**Map**
```
function (doc) {
  emit(doc.location, doc.overall_sentiment);
}
```

**Reduce**
```
function (keys, values, rereduce) {
  return sum(values)/values.length;
}
```
