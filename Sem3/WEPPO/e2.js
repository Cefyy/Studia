//LICZBY OD 1 DO 1E5, KTORE SA PODZIELNE PRZEZ KAZDA ZE SWOICH CYFR ORAZ ICH SUME
function CzyPodzielna(number)
{
    let sum = 0;
    let OriginalNumber = number;
    let temp = number;
    
    while(temp > 0)
    {
        let Digit = temp % 10;
        
        
        if(Digit === 0)
            return false;
            

        if(OriginalNumber % Digit !== 0)
            return false;
            
        sum += Digit;
        temp = Math.floor(temp / 10);
    }
    
    return (OriginalNumber % sum === 0);
}

console.log("Liczby od 1 do 100000 podzielne przez każdą swoją cyfrę i sumę cyfr:\n");
for(let i = 1; i < 1e5; i++)
{
    if(CzyPodzielna(i))
    {
        console.log(i);
    }
}