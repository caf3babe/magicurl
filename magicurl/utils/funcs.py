import logging
import re
import hashlib

URL_REGEX = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")


def extract_name_from_url(url:str):
    '''
    Get the name inside the URL
    Paramters-
        1. url(string)- The URl from where name is to be extracted
    Returns:
        1. The name from the URL.
    '''
    return re.findall('(\w+)://([\w\-\.]+)', url)[0][1]

def check_url(url:str):
    '''
    Using regular expression check if the URL is valid or not
    Paramters-
        1. url(string)- The URl to be checked
    '''
    if re.search(re.compile(URL_REGEX), url):
        return True
    else:
        return False

def get_logger():
    logger = logging.getLogger("magicurl")
    return logger

def generate_hash(name: str) -> str:
    '''
    Creates Hash of a given string
    '''
    result = hashlib.md5(bytes(name, "utf-8"))
    return str(result.hexdigest())
