"""
Hash-Table implementation using pure python 
Author : Donatello Gong
Github : rrbb014
E-mail : gutssoul1@gmail.com
"""

import sys

class HashTable:
    def __init__(self, bucket_size=pow(2, 10)):
        self._bucket_size=bucket_size
        self._store_keys= [None] * self._bucket_size # storage for keys
        self._store_values = [None] * self._bucket_size # storage for values
        self._hash = hash  # python built-in hash function
    
    def __getitem__(self, key):
        hash_value = self._hash(key)
        key_index = hash_value % self._bucket_size
        val = self._store_keys[key_index] 
        
        if val is None:
            raise Exception('No key ', key)
        else:
            return val
    
    def __setitem__(self, key, value):
        hash_value = self._hash(key)
        key_index = hash_value % self._bucket_size

        self._store_keys[key_index] = key
        self._store_values[key_index] = value
    
    def keys(self):
        res = [i for i in self._store_keys if i is not None]
        return res
    
    def values(self):
        res = [i for i in self._store_values if i is not None]
        return res


if __name__ == "__main__":
    a = HashTable()
    # print(a['asd'])
    a['asd'] = 'hi hashtable'
    #print(a['asd'])
    print(a.keys())
    print(a.values())