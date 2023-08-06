console.log("I print first")
const waitTimeMs = 10000

const callback = ()=>{
    console.log("I print second")
}

setTimeout(
    callback,
    waitTimeMs
)
console.log("I print third")