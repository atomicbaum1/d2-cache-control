# cache-control
A simple inventory tracking system for Destiny 2.
Currently the GUI is a work in progress and it is a multi-step process to login.

Basic OpenAPI code generation of the openapi.json file will generate get code for the OpenAPI Endpoints.

# How to use
1) Get an API key from Bungie and put the API key to `destiny/rescources/destiny-oauth-client-id` and `destiny/rescources/destiny-xapi-key`
2) Generate certificates and put them in openapi/resources/cert.pem and openapi/resources/key.pem.  I used the command `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -nodes -days 365 -subj '/CN=localhost'`
3) Run the server from openapi/oauth_server.py to start the Flask server
4) With the Flask server running, run destiny/bungie_client.py.
5) In the terminal there will be a link to click on, click on it and login to your bungie account
6) Once the tab says "You can now close the tab" close the tab and press "Enter in the terminal".  This will download the Destiny 2 database and print out some information about your account.

# Files to use
* openapi/api_gen.py - generates the API for grabbing OpanAPI data.  This is where destiny/bungie_api_gen.py comes from.
* openapi/oauth_server.py - The Bungie Flask server.  Must be running in order for the client to work.
* destiny/bungie_client.py - The bungie client that will allow you to login to your account.  Once logged in 

# Useful links
https://bungie-net.github.io/multi/schema_Destiny-Definitions-DestinyInventoryBucketDefinition.html#schema_Destiny-Definitions-DestinyInventoryBucketDefinition

https://bungie-net.github.io/multi/schema_Destiny-BucketCategory.html#schema_Destiny-BucketCategory