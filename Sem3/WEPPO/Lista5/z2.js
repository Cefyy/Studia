const readline = require('readline');

var rl = readline.createInterface(process.stdin,process.stdout);

rl.question("Input your name: ", (answer) => {
    console.log('Witaj',answer);
    rl.close();
})
