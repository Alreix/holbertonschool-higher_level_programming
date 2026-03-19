#!/usr/bin/node

// Node.js program to demonstrate the use of process.argv with if and else

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
