"""
Hash-Table implementation using pure python 
Author : Donatello Gong
Github : rrbb014
E-mail : gutssoul1@gmail.com
"""

import sys

class HashTable:
    """
    Hash-Table is one of data structure.
    It's useful to get same value many time.
    Asymtotically, if search one key's value is O(1).
    Thanks to hashing and array, directly access index of hashed key value.
    However, cons of hash-table is hash collision.
    Because hash function cannot make unique number from input value,
    it is more important to handle hashing value is same but not same input.
    """

    def __init__(self, bucket_size: int=pow(2, 10), hash_function=hash):
        if bucket_size > pow(2, 10):
            raise ValueError("Sorry, unfortunately too high bucket_size in this script. Please re-calibrate bucket_size <= pow(2, 10). ")

        self._bucket_size=bucket_size
        self._store_keys= [None] * self._bucket_size # storage for keys
        self._store_values = [None] * self._bucket_size # storage for values

        self._hash = hash_function  # python built-in hash function
    
    def __getitem__(self, key):
        hash_value = self._hash(key)
        key_index = hash_value % self._bucket_size
        val = self._store_keys[key_index] 
        
        if val is None:
            raise Exception('No key ', key)
        else:
            if not isinstance(val, list):
                return val
            else:
                for i in val:
                    if i == key:
                        return i
    
    def __setitem__(self, key, value):
        hash_value = self._hash(key)
        key_index = hash_value % self._bucket_size

        # if hash-collision occured
        if self._store_keys[key_index] is None:
            self._store_keys[key_index] = key
            self._store_values[key_index] = value
        else:
            if isinstance(self._store_keys[key_index], list):
                print("hash-collision with ", str(key), " and ", " ".join([i for i in self._store_keys[key_index]]))
                self._store_keys[key_index].append(key)
                self._store_values[key_index].append(value)

            else:    
                print("hash-collision with {} , {}".format(key, self._store_keys[key_index]))
                t = []
                t.append(self._store_keys[key_index])
                t.append(key)
                self._store_keys[key_index] = t

                v = []
                v.append(self._store_values[key_index])
                v.append(value)
                self._store_values[key_index] = v
    
    def keys(self):
        res = ""
        only_val = []
        list_val = []
        for idx in range(len(self._store_keys)):
            if self._store_keys[idx] is None:
                continue

            if not isinstance(self._store_keys[idx], list):
                only_val.append(idx)
            else:
                list_val.append(idx)

        for i in only_val:
            res += str(self._store_keys[i]) + ",\n"
        
        for j in list_val:
            for k in self._store_keys[j]:
                res += k + ",\n"

        return res
    
    def values(self):
        res = ""
        only_val = []
        list_val = []

        for idx in range(len(self._store_values)):
            if self._store_values[idx] is None:
                continue

            if not isinstance(self._store_values[idx], list):
                only_val.append(idx)
            else:
                list_val.append(idx)

        for i in only_val:
            res += str(self._store_values[i]) + ",\n"
        
        for j in list_val:
            for k in self._store_values[j]:
                res += k + ",\n"

        return res

if __name__ == "__main__":
    ht = HashTable()
    ht['asd'] = 'hi hashtable'
    print(ht.keys())
    print(ht.values())