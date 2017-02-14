# -*- coding: utf-8 -*-
"""
    Micropub-Config
    ===============
    This class queries a [Micropub](https://www.w3.org/TR/micropub/) endpoint
    for common [configuration parameters](https://www.w3.org/TR/micropub/#querying).
"""

import requests

class MicropubConfig:
    """MicropubConfig provides support for querying Micropub endpoint
    configuration such as media endpoint, syndicate-to values.
    """

    def __init__(self, endpoint, access_token):
        """Initialize this config object
        
        Args:
          endpoint (string): URL of the micropub endpoint.
          access_token (string): Access token to pass to the micropub endpoint
            when making requests.
        """
        self.endpoint = endpoint
        self.access_token = access_token
        self.query_config()

    def query_config(self):
        params= { 'q': 'config' }
        headers = { 'Authorization': "Bearer %s" % self.access_token }
        resp = requests.get( self.endpoint, headers=headers, params=params )
        try:
            self.mp_config = resp.json()
        except ValueError:
            self.mp_config = {}
