// Memoizacja - iteracyjna wersja
function fib_mem(n, mem) {
  mem[0] = 0;
  mem[1] = 1;
  if (n in mem) return mem[n];
  else return (mem[n] = fib_mem(n - 2, mem) + fib_mem(n - 1, mem));
}

// Rekurencja - wersja naiwna (bardzo wolna)
function FibRec(n) {
  if (n == 1 || n == 2) {
    return 1;
  }
  return FibRec(n - 1) + FibRec(n - 2);
}

// Funkcja memoizująca - dekorator
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

// Tworzenie memoizowanej wersji rekurencji
var memofib2 = memoize(FibRec);

var memofib41 = memoize(FibRec);
memofib41(41);

console.time("fib_mem(41)");
fib_mem(41, []);
console.timeEnd("fib_mem(41)");

console.time("memofib(41) cached");
memofib41(41);
console.timeEnd("memofib(41) cached");

console.time("FibRec(41)");
FibRec(41);
console.timeEnd("FibRec(41)");

console.log();

console.time("fib_mem(40)");
fib_mem(40, []);
console.timeEnd("fib_mem(40)");

console.time("FibRec(40)");
FibRec(40);
console.timeEnd("FibRec(40)");

var memofib40 = memoize(FibRec);
console.time("memofib(40)");
memofib40(40);
console.timeEnd("memofib(40)");

