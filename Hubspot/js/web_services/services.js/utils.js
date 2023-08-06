const hubspot = require("@hubspot/api-client")
const {CLIENT_ID, CLIENT_SECRET } = process.env;


const hubspotClient = new hubspot.Client();


const getAccessToken = async ()=>{
    const result = await hubspotClient.oauth.defaultApi.createToken(
        
    )
}

