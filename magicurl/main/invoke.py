#!/usr/bin/env python
from magicurl.utils.logger import get_logger
from magicurl.utils.constants import PORT, IP
from flask import Flask

LOG = get_logger()

def start_server():
    """
    The Entrypoint of magicurl utility
    """

    LOG.info("Starting magicurl server at port {PORT} and IP address- {IP}")
    server = Flask(___name__)
    server.run()

