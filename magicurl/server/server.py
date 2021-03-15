#!/usr/bin/env python
import base64
from magicurl.utils.funcs import get_logger, check_url, extract_name_from_url, generate_hash
from magicurl.utils.constants import INFO, SHORT_DOMAIN
from magicurl.utils.gladiator import Gladiator
from flask import Flask, request

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

    def _process_url(self):
        '''
        The actual business logic to process url is in this function
        '''
        self.log.info("Started to process the URL with arguments {request.form}")
        if "URL" not in request.form:
            return "ERROR: Body does not contian URL key \n"
        chk =  check_url(request.form["URL"])
        if not chk:
            return "ERROR: URL provided is not valid \n"
        ename = extract_name_from_url(request.form["URL"])
        cryptic_name = generate_hash(ename)

        mem = Gladiator("/tmp")
        if not mem.is_present(cryptic_name):
            mem.insert(cryptic_name)

        return f"Short URL= https://{SHORT_DOMAIN}/{cryptic_name} \n"

    def shorten_url(self):
        """
        Entrypoint of the route to shorten the URL came as payload"
        """
        self.server.add_url_rule("/shorten", view_func=self._process_url,
                methods=["POST"])

    def _add_apis(self):
        '''
        To register all API's this function is called
        '''
        self.basic_info()
        self.shorten_url()
