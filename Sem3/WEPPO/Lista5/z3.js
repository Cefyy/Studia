const readline = require('readline');

var rl = readline.createInterface(process.stdin,process.stdout);

let number = Math.floor(Math.random()*101); 

rl.setPrompt("Guess the number (0,100): ");
rl.prompt();
rl.on('line',function(line) {
    if (Number(line) == number)
        { 
            
            console.log("Congratulations!");
            rl.close();
        }
    if(Number(line) > number)
        console.log("Guessed number is too big")
    if(Number(line) < number)
        console.log("Guessed number is too small");
    rl.prompt();
}).on('close',function()
{
    process.exit(0);
})