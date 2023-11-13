#!/usr/bin/node

// prints second biggest interger in a list.
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);// this is the algorithm sorts in ascending order.
    // a-b is a - is a comparison operator means.
  console.log(args[args.length - 2]);// prints second to last argument.
}
