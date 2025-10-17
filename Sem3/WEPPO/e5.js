//fibonacci iteracyjnie i rekurencyjnie
// zmierzyc czas obu wersji
// wypisze w postaci tabeli na konsole od 10 do maksymalnego którego sensownie działa
// pomiary zrobic w node.js i jednej z przegladarek
// metody console.time i console.timeEnd

function FibIt(n)
{
    let prev = 1;
    let curr=1;
    let next;
    for(let i=3;i<=n;i++)
    {
        next = prev+curr;
        prev=curr;
        curr=next;
    }
    return curr;
}
function FibRec(n)
{
    if(n==1 || n==2)
    {
        return 1;
    }
    return FibRec(n-1)+FibRec(n-2)
}

console.log("\nPorównanie czasu wykonania Fibonacci (iteracyjnie vs rekurencyjnie):");
console.log("=".repeat(70));

for(let i = 10; i <= 45; i++)
{
    console.log(`\nDla n = ${i}:`);
    
    // Pomiar iteracyjny
    console.time(`  Iteracyjnie FibIt(${i})`);
    const resultIt = FibIt(i);
    console.timeEnd(`  Iteracyjnie FibIt(${i})`);
    
    // Pomiar rekurencyjny
    console.time(`  Rekurencyjnie FibRec(${i})`);
    const resultRec = FibRec(i);
    console.timeEnd(`  Rekurencyjnie FibRec(${i})`);
    
    console.log(`  Wynik: ${resultIt}`);
    console.log("Czy obie funkcje zwracają ten sam wynik: " + (resultIt === resultRec));
    
}