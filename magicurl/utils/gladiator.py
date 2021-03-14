#!/usr/bin/env python
import os
from magicurl.utils.funcs import get_logger

class Gladiator:
    '''
    A Service that gives memory to the magicurl
    '''
    def __init__(self, path:str):
        '''
        The path where to create the memory map for magicurl
            Parameters-
                1. path(string): The absolute path where memory would be created
            Returns:
                None
            In case file already found in path, then Gladiator will read it
        '''
        self.path = path
        self.log = get_logger()
        self._f_name = ".murl-cache.json"
        self._cache = None
        self._setup()

    def _setup(self):
        '''
        A function which initialises everything
        '''
        with open(os.path.join(self.path, self._f_name), "r") as cache_handler:
                self._cache = cache_handler.readlines()

    def _dump_cache(self):
        '''
        To dump the local cache in memory to File
        '''
        with open(os.path.join(self.path, self._f_name), "wa") as cache_file:
            import pdb
            pdb.set_trace()


    def insert(self, key: str, value: str):
        '''
        This function inserts the data in key value format in memory map
            Parameters-
                1. key(string): The Key or index with which to store
                2. value(string): The Value to store against the key
        '''
        self.log.info(f"Adding key {key} with value {value}")

        #Ideally there will be another utility to check of the key is already present
        #Then dont insert, But this is just a double check.
        if key in self._cache.keys():
            self.log.error("Insertion failed as key already present in map")
            return False

        self._cache[key] = value
        self._dump_cache()
        return True
