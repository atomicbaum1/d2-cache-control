"""Bungie client for interacting with the Destiny 2 servers"""
import logging
import sys
from pprint import pprint
from openapi.oauth_client import OpenApiClientSession
from destiny.bungie_api_gen import UserEndpoint, Destiny2Endpoint
from openapi.web_api import download_file
import os.path
import zipfile
import sqlite3

DESTINY_DATABASE_DOWNLOAD_PATH = '/tmp/d2.db.zip'
DESTINY_DATABASE_PATH = '/tmp/'
DESTINY_DATABASE_VERSION_PATH = '/tmp/d2.db.vsn'
DESTINY_DATABASE_MANIFEST_PATH = 'http://www.bungie.net'
DESTINY_CURRENT_DB = f'{DESTINY_DATABASE_PATH}/world_sql_content_8ce5b3356e8749ddcb7f81c0ac8875c6.content'


class BungieClientSession:
    """A Bungie client session."""

    def __init__(self, open_api_session):
        """Initialize the Bungie Client Session.  Only run the discover() function after the user has logged in.
        Args:
            open_api_session - An authenticated OpenApiClientSession
        """
        self.session = open_api_session
        self.user_endpoint = UserEndpoint(open_api_session)
        self.destiny2_endpoint = Destiny2Endpoint(open_api_session)

        self.discovered = False  # True when the discovery was successful
        self.bungie_net_user = None  # bungieNetUser data
        # TODO: Handle multiple membership types and multiple memberships of the same game
        self.destiny_membership_display_name = None
        self.destiny_membership_icon_path = None
        self.destiny_membership_id = None
        self.destiny_membership_type = None
        self.destiny2_manifest_version = None
        self.destiny2_database_location = None

    def _load_database(self, database_name):
        """Load the Destiny 2 database"""
        conn = sqlite3.connect(database_name)
        cur = conn.cursor()

        conn.close()

    def discover(self):
        """Gets all of the basic information for this user."""
        # TODO: In the future this should be a real discovery of the bungie API and not just for one user
        # TODO: for destiny 2
        membership_data = self.user_endpoint.get_membership_data_for_current_user()
        pprint(membership_data)
        self.discovered = True
        self.bungie_net_user = membership_data['Response']['bungieNetUser']

        # TODO: Handle more than one membership
        # This is an array, but for now I'm only going to care about the first membership - most likely only membership
        self.destiny_membership_display_name = membership_data['Response']['destinyMemberships'][0]['displayName']
        self.destiny_membership_icon_path = membership_data['Response']['destinyMemberships'][0]['iconPath']
        self.destiny_membership_id = membership_data['Response']['destinyMemberships'][0]['membershipId']
        self.destiny_membership_type = membership_data['Response']['destinyMemberships'][0]['membershipType']

        # Download the databases
        # TODO: Add support for all databases, not just mobileWorldContentPaths['en']
        manifest = self.destiny2_endpoint.get_destiny_manifest()
        self.destiny2_manifest_version = manifest['Response']['version']
        # Write the version to a file so we can cache downloads
        # TODO: make cache somewhere not in /tmp/?  LEFT OFF HERE. TOO SLEEPY NOW.
        #if os.path.isfile(DESTINY_DATABASE_VERSION_PATH):
        #    with open(DESTINY_DATABASE_VERSION_PATH, 'r') as file:
        #        file.read(self.destiny2_manifest_version)
        #else:  # Download the file
        #    with open(DESTINY_DATABASE_VERSION_PATH, 'w') as file:
        #        file.write(self.destiny2_manifest_version)
        if not os.path.isfile(DESTINY_DATABASE_DOWNLOAD_PATH):
            logging.debug(f'Downloading {DESTINY_DATABASE_DOWNLOAD_PATH}')
            mobile_world_content_paths_en = manifest['Response']['mobileWorldContentPaths']['en']
            download_file(f'{DESTINY_DATABASE_MANIFEST_PATH}{mobile_world_content_paths_en}',
                          DESTINY_DATABASE_DOWNLOAD_PATH)
            logging.debug('Downloaded')

        # Unzip it
        if not os.path.isfile(DESTINY_CURRENT_DB):
            logging.debug(f'Unzipping {DESTINY_DATABASE_DOWNLOAD_PATH}')
            with zipfile.ZipFile(DESTINY_DATABASE_DOWNLOAD_PATH, 'r') as zip_ref:
                zip_ref.extractall(DESTINY_DATABASE_PATH)
            logging.debug('Unzipped')

        # Load the database
        self._load_database(DESTINY_CURRENT_DB)
        logging.debug(f'Database {DESTINY_CURRENT_DB} loaded.')

        logging.debug('Done discovering...')

    def get_destiny2_users(self):
        pass

    def get_destiny2_characters(self):
        pass


if __name__ == '__main__':
    # Some Destiny constants
    DESTINY_BASE_URL = 'https://www.bungie.net'
    DESTINY_SERVER_URL = 'https://www.bungie.net/platform'
    DESTINY_AUTHORIZATION_URL = 'https://www.bungie.net/en/OAuth/Authorize'
    DESTINY_TOKEN_URL = 'https://www.bungie.net/Platform/App/OAuth/token/'
    DESTINY_TOKEN_REFRESH_URL = 'https://www.bungie.net/Platform/App/OAuth/token/'

    # project client ID (Will load from file)
    with open('resources/destiny-oauth-client-id') as x:
        DESTINY_OAUTH_CLIENT_ID = x.read()

    # project X-API-KEY (Will load from file)
    with open('resources/destiny-xapi-key') as x:
        DESTINY_XAPI_KEY = x.read()

    # Setup logging
    logging.basicConfig(# filename='resources/logs/foo.log',
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        level=logging.DEBUG)
    logging.StreamHandler(sys.stdout)

    logging.debug('-------STARTING-------')
    open_api_session = OpenApiClientSession(DESTINY_AUTHORIZATION_URL, DESTINY_TOKEN_URL, DESTINY_TOKEN_REFRESH_URL,
                                            DESTINY_OAUTH_CLIENT_ID, DESTINY_XAPI_KEY)
    auth_url = open_api_session.get_local_authorization_url()
    print(f'Authorization URL is {auth_url}')
    input('Press Enter to continue...')

    destiny_session = BungieClientSession(open_api_session)
    destiny_session.discover()
