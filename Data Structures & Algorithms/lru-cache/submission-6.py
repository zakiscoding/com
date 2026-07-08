class Node:
    def __init__(self,key,val):
        self.key =key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap =capacity
        self.cache= {}
        self.right = Node(0,0)
        self.left = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev=node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]