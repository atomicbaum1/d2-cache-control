"""Web API for connecting to and getting data from OpenAPI servers."""

import logging
import requests
import json

LOCAL_OAUTH_SERVER_URL = 'https://localhost:5000'


class OpenApiClientSession:
    """Opan API client"""

    def __init__(self, authorization_url, token_url, token_refresh_url, client_id, xapi_key,
                 local_server_address=LOCAL_OAUTH_SERVER_URL):
        """Initialize the OpenAPI server with the correct endpoints
        Args:
            authorization_url - The OAuth authorization URL
            token_url - The OAuth token URL
            token_refresh_url - The OAuth refresh token URL
            client_id - OAuth Client application ID
            xapi_key - X-API-KEY
            local_server_address - Address of the local OAUTH server
        """

        # Grab the client info needed
        self.local_server_address = local_server_address
        self.authorization_url = authorization_url
        self.token_url = token_url
        self.token_refresh_url = token_refresh_url
        self.client_id = client_id
        self.xapi_key = xapi_key

    def get_local_authorization_url(self):
        """Get the URL to the session authorization URL
        This return the URL for the server authorization page.
        After the user is logged in you can start requesting data.
        Returns:
            string containing the URL link of the authorization page
        """

        open_url = ('{local_server_address}/authorize?'
                    'authorization_url={authorization_url}&'
                    'token_url={token_url}&'
                    'token_refresh_url={token_refresh_url}&'
                    'client_id={client_id}&'
                    'xapi_key={xapi_key}&').format(local_server_address=self.local_server_address,
                                                   authorization_url=self.authorization_url,
                                                   token_url=self.token_url,
                                                   token_refresh_url=self.token_refresh_url,
                                                   client_id=self.client_id,
                                                   xapi_key=self.xapi_key)
        logging.debug('Open URL is:{open_url}'.format(open_url=open_url))
        return open_url

    def shutdown(self):
        """Shuts down the flask server"""
        # TODO: Build a certificate chain so we can verify our localhost and remove the verify=False workaround.
        requests.get('{local_server_address}/shutdown'.format(local_server_address=self.local_server_address),
                     verify=False)

    def get_any(self, url_get):
        """Get any request back as a dictionary
        A connection must already be established in order to request data.
        Be sure to call initialize() and authenticate_user() first - and that the user is really authenticated
        before attempting to run this command.
        Ex.
            session.get_any('{url}/{path}'.format{URL, '/Api/{Param}/'))
        You must provide URL params in your GET request in the "url_get" parameter.
        Returns:
            Dictionary of raw data
        """

        params = {'url_get': url_get}
        logging.debug('URL is: {url_get}'.format(url_get=url_get))

        req = requests.get('{local_server_address}/any'.format(local_server_address=self.local_server_address),
                           verify=False, params=params)
        print(req.text)
        return json.loads(req.text)
