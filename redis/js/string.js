const client = require('./clinet')

async function init(){
    console.log("called ")
    const res = await client.get("users:1")
    console.log(res)
    console.log("done")
}


init();