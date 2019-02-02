"""OAuth2 local Flask server for interfacing with the OpenAPI server
The API to this server is in the form of GET requests for connecting to and getting data from OpenAPI servers.
"""

import sys
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect
from flask.json import jsonify
from os import urandom
import logging

# Flask application
app = Flask(__name__)
local_session = {}  # We only want one session across all local traffic.  OAuthClient<->LocalOAuthServer<->OAuthServer


@app.route('/authorize')
def authorize():
    """OAuth2 Authorization Path. (Step 1 in the OAuth process)
    The browser needs to navigate to this link first in order to authorize the user.
    Returns:
        A redirect to the authorization URL (The Oauth2 Server)
    """
    logging.debug('=====Calling {path}==='.format(path='/authorize'))

    # Extract the URL params
    local_session['authorization_url'] = request.args.get('authorization_url')
    local_session['token_url'] = request.args.get('token_url')
    local_session['token_refresh_url'] = request.args.get('token_refresh_url')
    local_session['client_id'] = request.args.get('client_id')
    local_session['xapi_key'] = request.args.get('xapi_key')

    logging.debug(('URL params:\n'
                   'authorization_url:{authorization_url}\n'
                   'token_url:{token_url}\n'
                   'token_refresh_url:{token_refresh_url}\n'
                   'client_id:{client_id}\n'
                   'xapi_key:{xapi_key}\n'
                   ).format(authorization_url=local_session['authorization_url'],
                            token_url=local_session['token_url'],
                            token_refresh_url=local_session['token_refresh_url'],
                            client_id=local_session['client_id'],
                            xapi_key=local_session['xapi_key']))

    # Setup our authorization session
    oauth_session = OAuth2Session(local_session['client_id'])
    authorization_url, state = oauth_session.authorization_url(local_session['authorization_url'])

    # State is used to prevent Cross Site Request Forgery (CSRF)
    local_session['oauth_state'] = state
    logging.debug('CSRF oauth_state is {state}'.format(state=state))
    # Redirect the user to the authorization URL (This is step 2 for the user to login with their web browser)
    return redirect(authorization_url)


@app.route('/callback', methods=["GET"])
def callback():
    """Get an access token (OAuth Step 3)
    This is the callback URL that we provided to the OAuth servers.
    You cannot change this unless you also update the Redirect URL on the application page.
    Returns:
        Redirect to the close page
    """
    logging.debug('=====Calling {path}==='.format(path='/callback'))
    logging.debug('CSRF oauth_state is NOW {state}'.format(state=local_session['oauth_state']))
    # Get the session and grab a token
    logging.debug('Request url is {url}'.format(url=request.url))
    oauth_session = OAuth2Session(local_session['client_id'], state=local_session['oauth_state'])
    token = oauth_session.fetch_token(local_session['token_url'],
                                      client_secret='',  # No client secret for public
                                      authorization_response=request.url)

    # Store the token
    local_session['oauth_token'] = token
    local_session['logged_in'] = True

    # Inform the user it is now OK to close the tab
    return redirect('/close')


@app.route('/status', methods=["GET"])
def status():
    """Status JSON string of all of the web server globals.
    Currently supports the following:
        logged_in : Truth value.  True when the user is logged in.
    Returns:
        Json string containing a dictionary of supported server globals.
    """
    logging.debug('=====Calling {path}==='.format(path='/status'))

    # TODO: Return status data based on timestamp of oauth_token and refreshes

    data = {'logged_in': local_session['logged_in']}
    logging.debug('Data is {data}'.format(data=data))

    return jsonify(data)


@app.route('/close')
def close():
    """Inform the user that it is OK to close the tab
    Returns:
        Information the user can use to take the next step.
    """
    logging.debug('=====Calling {path}==='.format(path='/close'))

    return "You can now close the tab."


@app.route('/any', methods=["GET"])
def any_request():
    """Get any attribute using the current connection.
    A connection must already be established in order to request data.
    You must provide the following URL params in your GET request:
        "url" - The URL to send the information to
        "request_type" - The request type.  Either "get" or "post" supported
        "oauth_client_id" - The OAuth client ID
        "xapi_key" - The X-API key
    Returns:
        JSON string of the response data.
    """
    logging.debug('=====Calling {path}==='.format(path='/any'))

    url_get = request.args.get('url_get')
    # TODO: Add request types
    # request_type = request.args.get('request_type')

    # Get our session, set the X-API-KEY
    oauth_session = OAuth2Session(local_session['client_id'], token=local_session['oauth_token'])
    oauth_session.headers['X-API-KEY'] = local_session['xapi_key']
    response = oauth_session.get(url_get)
    logging.debug('Response is: {response}'.format(response=response))

    return jsonify(response.json())


@app.route('/shutdown', methods=['GET'])
def shutdown():
    """Shutdown the server"""
    logging.debug('=====Calling {path}==='.format(path='/shutdown'))
    request.environ.get('werkzeug.server.shutdown')()
    return '{}'


def start_flask_server_process():
    """Setup and run the Flask server."""
    # Setup logging
    logging.basicConfig(# filename='resources/logs/foo.log',
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        level=logging.DEBUG)
    logging.StreamHandler(sys.stdout)
    logging.debug('Starting the Flask server.')

    # Flask server setup
    app.secret_key = urandom(24)
    app.use_reloader = True
    app.run(debug=True, ssl_context=('resources/cert.pem', 'resources/key.pem'))


if __name__ == '__main__':
    # Start the Flask server
    start_flask_server_process()
