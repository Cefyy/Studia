const https = require('https');

function fetchBasic(url, callback) {
    https.get(url, (res) => {
        let data = '';
        
        res.on('data', (chunk) => {
            data += chunk;
        });
        
        res.on('end', () => {
            callback(null, data);
        });
        
    }).on('error', (err) => {
        callback(err, null);
    });
}

function fetchPromise(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            let data = '';
            
            res.on('data', (chunk) => {
                data += chunk;
            });

            res.on('end', () => {
                resolve(data);
            });
            
        }).on('error', (err) => {
            reject(err);
        });
    });
}

// Demonstracja użycia
// Większy zasób z wieloma chunkami
const testUrl = 'https://en.wikipedia.org/wiki/Node.js';

fetchBasic(testUrl, (err, data) => {
    if (err) {
        console.error(err.message);
        return;
    }
    console.log(data);
});

fetchPromise(testUrl)
    .then(data => {
        console.log(data);
    })
    .catch(err => {
        console.error(err.message);
    });
