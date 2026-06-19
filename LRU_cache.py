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
    
    def remove(self, node):
        prev= node.prev
        nxt = node.next

        prev.next=nxt
        nxt.prev=prev

    def insert(self,node):
        prev= self.right.prev

        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node


    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        
