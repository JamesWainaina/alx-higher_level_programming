#!/usr/bin/node
// prints the message according to the argument passed.
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
