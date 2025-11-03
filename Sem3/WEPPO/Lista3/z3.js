function createFs(n) { // tworzy tablicę n funkcji
  var fs = []; // i-ta funkcja z tablicy ma zwrócić i
  for ( var i = 0; i<n; i++ ) {
    fs[i] = function() {
      return i;
    };
  };

  return fs;
}

var myfs = createFs(10);

console.log( myfs[0]() ); // oczekiwane: 0
console.log( myfs[2]() ); // oczekiwane: 2
console.log( myfs[7]() ); // oczekiwane: 7

function createFsLet(n) {
  var fs = [];
  for ( let i = 0; i < n; i++ ) {
    fs[i] = function() { return i; };
  }

  return fs;
}

var myfsLet = createFsLet(10);
console.log( myfsLet[0]() ); // 0
console.log( myfsLet[2]() ); // 2
console.log( myfsLet[7]() ); // 7

//var jest jeden który na koniec ma wartość 10 wiec wszystkie kiedy odwołuje sie 
//to mamy domnkiecie tych funkcji z i=10 

//let tworza kopie wiec kazda z tych funkcji ma swoje domkniecie z i0=0,i1=1 itd.



function createFs_var_IIFE(n) {
  var fs = [];
  for (var i = 0; i < n; i++) {
    (function(j) {
      fs[j] = function() { return j; };
    })(i);
  }
  return fs;
}

var myfsIIFE = createFs_var_IIFE(10);
console.log( myfsIIFE[0]() ); // 0
console.log( myfsIIFE[2]() ); // 2
console.log( myfsIIFE[7]() ); // 7
//wykorzystujemy iife by odizolować var i=0 i zdefiniowac i wykonac funkcje od razu, wykonując kopie
//podczas przerzucania do argumentu
// czyli kazda funkcja nie tworzy domknięcia z i tylko ze swoim j