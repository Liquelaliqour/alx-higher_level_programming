#!/usr/bin/node
// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Export the Square class
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Pass size as both width and height to the Rectangle constructor
  }
}
