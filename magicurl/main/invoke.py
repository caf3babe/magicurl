#!/usr/bin/env python
from magicurl.utils.logger import get_logger
from magicurl.utils.constants import PORT, IP, INFO
from flask import Flask

LOG = get_logger()
SERVER= None
def start_server():
    """
    The Entrypoint of magicurl utility
    """

    LOG.info("Starting magicurl server at port {PORT} and IP address- {IP}")
    SERVER = Flask("magicurl")
    SERVER.run(host=IP, port=PORT)

@SERVER.route("/")
def print_info():
    return INFO
