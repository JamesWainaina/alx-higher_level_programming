#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // using the reduce method to count occurrences
  return list.reduce((count, currentElement) => {
    return (currentElement === searchElement) ? count + 1 : count;
  }, 0);
};
