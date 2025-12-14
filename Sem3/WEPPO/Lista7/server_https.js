const https = require('https');
const fs = require('fs');

const options = {
    pfx: fs.readFileSync('C:\\Users\\kuba\\Documents\\Studia\\Sem3\\Weppo\\Lista7\\server.pfx'),
    passphrase: '123' // Hasło ustawione przy eksporcie do PFX
};

https.createServer(options, (req, res) => {
    res.writeHead(200);
    res.end("Witaj! Polaczenie jest bezpieczne (HTTPS).");
}).listen(3000);

console.log('Serwer HTTPS działa na https://localhost:3000');