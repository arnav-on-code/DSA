class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next= self.right
        self.right.next=self.left

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        
