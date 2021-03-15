#!/usr/bin/env python
import os
import json
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
        try:
            with open(os.path.join(self.path, self._f_name), "r") as cache_handler:
                    self._cache = json.load(cache_handler)
        except FileNotFoundError as no_file:
            self._cache = {"urls": []}

    def is_present(self, value: str):
        '''
        Check if the value is already present or not in cache
            Parameters:
                1. value(string)- The value to be searched
        '''
        if value in self._cache["urls"]:
            return True
        return False

    def _dump_cache(self):
        '''
        To dump the local cache in memory to File
        '''
        with open(os.path.join(self.path, self._f_name), "w") as cache_file:
            json.dump(self._cache, cache_file)

    def insert(self, value: str):
        '''
        This function inserts the data value in memory map.
            Parameters-
                2. value(string): The Value to store against the key
        '''
        self.log.info(f"Adding value {value}")

        #Ideally there will be another utility to check of the key is already present
        #Then dont insert, But this is just a double check.
        if value in self._cache["urls"]:
            self.log.error("Insertion failed as key already present in map")
            return False

        self._cache["urls"].append(value)
        self._dump_cache()
        return True
