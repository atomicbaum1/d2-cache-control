# OpenAPI resources
Add your cert.pem and key.pem generated from this command here
` openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -nodes -days 365 -subj '/CN=localhost'`