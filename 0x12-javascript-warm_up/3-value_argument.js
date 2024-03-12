#!/usr/bin/node
// a script that prints the first argument passed to it//
const firstArgument = process.argv;
if (firstArgument[2] === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgument[2]);
}
