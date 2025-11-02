//dopisac czasy
function fib_mem(n, mem) {
  mem[0] = 0;
  mem[1] = 1;
  if (n in mem) return mem[n];
  else return (mem[n] = fib_mem(n - 2, mem) + fib_mem(n - 1, mem));
}
function FibRec(n) {
  if (n == 1 || n == 2) {
    return 1;
  }
  return FibRec(n - 1) + FibRec(n - 2);
}
function memoize(fn) {
  var cache = {};
  return function (n) {
    if (n in cache) {
      return cache[n];
    } else {
      var result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}
var memofib2 = memoize(FibRec);
memofib2(41)
console.log(fib_mem(41, []));
console.log(memofib2(41));
console.log(FibRec(41))