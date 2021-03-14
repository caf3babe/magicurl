#!/usr/bin/env python
from magicurl.utils.funcs import get_logger
from magicurl.utils.constants import INFO
from flask import Flask

class Server:
    """
    The Class contains all the API's which masgicurl hosts
    """
    def __init__(self, ip, port):
        '''
        The parameterised contructor for Server class
            Parameters:-
                1. ip(string)- The ip on which the server will start.
                2. port(string)- The port on which the server will bind.
            Returns:
                None
        '''
        self.ip = ip
        self.port = port
        self.log = get_logger()
        self.server = Flask("magicurl")
    
    def start_serving(self):
        '''
        This functions starts the server, A blocking call
        '''
        self._add_apis()
        self.server.run(host=self.ip, port=self.port)

    def basic_info(self):
        """
        Adds the endpoint for default route
        """
        self.server.add_url_rule("/", view_func=self._get_info,
                methods=["GET"])

    def _get_info(self):
        return INFO

    def _add_apis(self):
        self.basic_info()
