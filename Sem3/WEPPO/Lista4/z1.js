function getLastProto(o) {
  var p = o;
  do {
    o = p;
    p = Object.getPrototypeOf(o);
  } while (p);
  return o;
}

var obj1 = {};
var obj2 = new Object();
var arr = [1, 2, 3];
var func = function () {};
var date = new Date();

function MojKonstruktor() {}
var mojObiekt = new MojKonstruktor();

var proto1 = getLastProto(obj1);
var proto2 = getLastProto(obj2);
var proto3 = getLastProto(arr);
var proto4 = getLastProto(func);
var proto5 = getLastProto(date);
var proto6 = getLastProto(mojObiekt);

console.log("obj1 === obj2:", proto1 === proto2);
console.log("obj1 === arr:", proto1 === proto3);
console.log("obj1 === func:", proto1 === proto4);
console.log("obj1 === date:", proto1 === proto5);
console.log("obj1 === mojObiekt:", proto1 === proto6);
console.log("Wszystkie === Object.prototype:", proto1 === Object.prototype);
