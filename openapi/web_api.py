"""Common Web related constants and utility functions."""
import logging
import os
import errno
import requests


def download_file(url_path, write_path):
    """Downloads a file
    Args:
        url_path - Path to the file to download
        write_path - Path and name to the file to write
    """
    response = requests.get(url_path)
    if not os.path.exists(os.path.dirname(write_path)):
        try:
            os.makedirs(os.path.dirname(write_path))
        except OSError as exec_err:
            if exec_err.rerrno != errno.EEXIST:
                raise

    with open(write_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    logging.debug('Downloaded {url_path} to {write_path}.'.format(url_path=url_path, write_path=write_path))
