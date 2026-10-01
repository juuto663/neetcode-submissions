class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Maps keys to nodes
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def print_list(self):
        curr = self.head

        while curr:
            print(f"{curr.key, curr.val}")
            curr = curr.next

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        # print("Removing")
        # self.print_list()
        return node
    
    def insert(self, node: ListNode):
        last_node = self.tail.prev
        self.tail.prev = node
        last_node.next = node
        node.prev = last_node
        node.next = self.tail

        # print("inserting")
        # self.print_list()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.cache[key].val = value
            node = self.remove(node)
            self.insert(node)
        else:
            ln = ListNode(key, value)
            self.insert(ln)
            self.cache[key] = ln

        if len(self.cache) > self.cap:
            to_evict = self.head.next
            del self.cache[to_evict.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            




