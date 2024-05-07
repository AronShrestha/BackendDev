const http = require("http"); 
const WebSocketServer = require("websocket").server
let connection = null

const httpserver =  http.createServer( (req, res)=>{
    console.log("Received a request");
    // res.write("Hello ");
    // res.end();
}) // creating server

const websocket = new WebSocketServer({
    "httpServer": httpserver  // this is handshake

})

websocket.on("request", request=>{ //this isconnection upgrade
    function mesasgeFromServer(texMsg){
        console.log("message sending from server")
        connection.send(`Heelo ${texMsg}-------->`)
    }
    connection  = request.accept(null, request.origin)
    // console.log(connection)
    connection.on("open",()=>{
        console.log("Opened !!!!!!!!")
    } )
    connection.on("close", ()=>{
        console.log("Closed")
    })
   connection.on("message",(message)=>{
    const texMsg = message.utf8Data;
    console.log(`Received message from the client  ${texMsg}`)
    mesasgeFromServer(texMsg);

   })   
})

httpserver.listen(8000,()=>{
    console.log("Listening at port 8000")
})