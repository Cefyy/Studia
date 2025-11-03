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

console.log("=== POMIAR CZASU DLA FIB(41) ===\n");


console.log("1. fib_mem(41) - memoizacja iteracyjna:");
console.time("fib_mem");
var result1 = fib_mem(41, []);
console.timeEnd("fib_mem");
console.log("Wynik:", result1);
console.log();


console.log("2. memofib2(41):");
console.time("memofib2");
memofib2(41);
var result2 = memofib2(41);
console.timeEnd("memofib2");
console.log("Wynik:", result2);
console.log();

console.log("3. FibRec(41):");
console.time("FibRec");
var result3 = FibRec(41);
console.timeEnd("FibRec");
console.log("Wynik:", result3);
console.log();


console.log("=== PORÓWNANIE WYNIKÓW ===");
console.log("Wszystkie wyniki równe?", result1 === result2 && result2 === result3);
console.log();

