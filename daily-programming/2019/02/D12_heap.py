"""
Heap implementation using pure python 
Author : Donatello Gong
Github : rrbb014
E-mail : gutssoul1@gmail.com
Date : 2019-02-12
"""
class Node:
    def __init__(self):
        self._storage = None
        self._left = None
        self._right = None

    def get(self):
        return self._storage

    def set(self, data):
        self._storage = data
        print("Store ", data)
    
    
    
class Heap:
    """
    Heap is one of kind of tree data structure.
    It is used to implement priority queue.
    priority queue is free to add elements and when extract elements,
    It should return from minimal value.
    In heap, each nodes have data. 
    """
    
    def __init__(self):
        self.root = Node()
    
    def view(self):
        pass
    
    