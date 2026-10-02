import collections
class Node:
    def __init__(self, key:int = 0, value: int = 0):
        self.key, self.value = key, value 
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.defaultdict(Node)
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node: Node): 
        last_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = last_node
        last_node.next = node       

    # def print_list(self):
    #     curr = self.head
    #     print("The list")
    #     while curr:
    #         print(curr.value)
    #         curr = curr.next
    
    def remove(self, node: Node):
        if not node.next and not node.prev:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        # self.print_list()
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache[key]
        node.key = key
        node.value = value
        self.remove(node)
        self.insert(node)
        if len(self.cache) > self.cap:
            key = self.head.next.key
            self.remove(self.head.next)
            del self.cache[key]
        # self.print_list()
