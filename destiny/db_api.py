"""Database API for reading the Destiny 2 databases gathered from the manifest."""

import sqlite3
import zipfile
from os import rename, path
import json

DATABASE_DIRECTORY = '/tmp/'
DATABASE_ZIP_NAME = 'd2.db.zip'
DATABASE_NAME = 'dt_db.sqlite'
DATABASE_ZIP_DIR_PATH = DATABASE_DIRECTORY + DATABASE_ZIP_NAME
DATABASE_DIR_PATH = DATABASE_DIRECTORY + DATABASE_NAME

# TODO: check local DB version history
def database_exists(directory=DATABASE_DIRECTORY, zip_name=DATABASE_ZIP_NAME, name=DATABASE_NAME):
    """Extracts the destiny database zip file and renames the contents.

    Args:
        directory:
            Directory where the database zip file is located and where the extracted database reside.
        zip_name:
            Name of the destiny database zip file
        name:
            Name of the extracted database

    Returns:
        True if everything exists and false otherwise
    """
    return path.exists(directory + zip_name) and path.exists(directory + name)

def extract_database(directory=DATABASE_DIRECTORY, zip_name=DATABASE_ZIP_NAME, name=DATABASE_NAME):
    """Extracts the destiny database zip file and renames the contents.

    Args:
        directory:
            Directory where the database zip file is located and where the extracted database will reside.
        zip_name:
            Name of the destiny database zip file to unzip
        name:
            Name of the database after it is extracted.  This is usually a rename.
    """
    zf = zipfile.ZipFile(directory + zip_name, 'r')
    extracted_name = zf.infolist()[0].filename  # Assuming a lot here. ZipInfo list with one file (database)
    zf.extractall(directory)
    zf.close()
    rename(directory + extracted_name, directory + name)


class EquipmentItem:
    """Important equipment information"""
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path


# TODO: Don't be lazy and grab all of the item hashes at once in one select
def get_equipment_item(connection, item_hash):
    """Open the Destiny 2 sqlite database and extract interesting weapon data.

    Args:
        connection:
            Database connection

        item_hash:
            Item hash to get

    Returns:
        A dictionary where the key is the weapon hash and the value is a dictionary of name value weapon attributes.
    """
    cur = connection.cursor()
    cur.execute('SELECT json FROM DestinyInventoryItemDefinition where json LIKE \'%{item_hash}%\';'.format(
        item_hash=item_hash))

    # Should be the one and only entry
    entry = cur.fetchall()[0][0]
    item_dict = json.loads(entry)
    return EquipmentItem(item_dict['displayProperties']['name'], item_dict['displayProperties']['icon'])


def demo():
    """db_api demo"""
    if not database_exists():
        extract_database()

    connection = sqlite3.connect(DATABASE_DIR_PATH)
    sample = [(273396910, 2), (3312073054, 3), (3860697509, 2), (3778520449, 2), (48361213, 2), (731147178, 2),
              (2535939781, 2), (3778520451, 2), (2296691422, 2), (287042892, 2), (1277015089, 2), (2502422774, 2),
              (1513927137, 2), (1024867629, 2)]

    def print_item(item):
        print('Item name: {name} - {path}'.format(name=item.name, path=item.icon_path))

    [print_item(get_equipment_item(connection, item[0])) for item in sample]


if __name__ == '__main__':
    demo()
