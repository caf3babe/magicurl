#!/usr/bin/env python
from magicurl.utils.funcs import get_logger
from magicurl.utils.constants import PORT, IP, INFO
from magicurl.server.server import Server

LOG = get_logger()
def start_server():
    """
    The Entrypoint of magicurl utility
    """

    LOG.info("Starting magicurl server at port {PORT} and IP address- {IP}")
    server = Server(ip=IP, port=PORT)
    server.start_serving()
