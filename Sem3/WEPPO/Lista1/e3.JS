//liczby pierwsze od 2 do 1e5 nie musi byc najwydajniej

function czyPierwsza(number)
{
    for(let i=2;i<=Math.sqrt(number);i++)
    {
        if(number%i === 0)
            return false;
    }
    return true;
}

console.log("Wszystkie liczby pierwsze od 2 do 100000: \n")
for(let i = 2;i<=1e5;i++)
{
    if(czyPierwsza(i))
    {
        console.log(i);
    }
}
