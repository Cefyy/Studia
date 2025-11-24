const fs = require('fs');
const util = require('util');

fs.readFile('z4.txt','utf8',(err,data) => {
    if(err)
    {
        console.error("Blad",err);
        return;
    }
    console.log("Dane",data);
})


//Promise 1

function readFilePromise_1(path,encoding)
{
    return new Promise((resolve,reject) => {
        fs.readFile(path,encoding,(err,data) => {
            if (err) reject(err);
            else resolve(data);
        })
    })
}

//Promise 2
const readFilePromise_2 = util.promisify(fs.readFile);

//Promise3

const fs1 = require('fs').promises;


readFilePromise_1('z4.txt','utf8')
    .then(data => {
        console.log("dane: ",data);
    })
    .catch(err => {
        console.error("Error: ",err)
    })


async function readFileNew()
    {
        try {
            const data = await readFilePromise_1('z4.txt','utf8');
            console.log("data: ",data);
        }
        catch(err){
            console.error("Error: ",error);
        }
    }

readFileNew();