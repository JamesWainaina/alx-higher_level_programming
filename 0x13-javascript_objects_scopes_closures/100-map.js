#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);

const mappedList = list.map(function (element, idx) {
  return element * idx;
  // the element and idx are identifiers for the provided array
});
console.log(mappedList);
