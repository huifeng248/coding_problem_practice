from collections import OrderedDict

# solution one: double linkedlist, time O(1) space O(n) n is capacity
# the least use is at the end, everytime it's used, it would be move to the head. therefore the end is the least used
# the key chanllenge is to use the dict to store the actual node, which have a prev and next pointer. # use the object.get(key) to get the actual reference address is also another key thing which is easy to missed.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        # not sure why use the cache
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        self.cache[node.key] = node

        head_next = self.head.next
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        head_next.prev = node


    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val
    
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
    
    def remove_node(self, node):
        pre_node = node.prev
        next_node = node.next

        pre_node.next = next_node
        next_node.prev = pre_node
        del self.cache[node.key]
    
    def add_node(self, node):
        self.cache[node.key] = node
        
        next_head = self.head.next
        node.next = next_head
        next_head.prev = node

        node.prev = self.head
        self.head.next = node

    def remove_tail(self):
        prev_tail = self.tail.prev
        
        self.remove_node(prev_tail)

        return prev_tail



    def put(self, key, value):
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value
            self.move_to_head(node)

        else:
            new_node = Node(key, value)
            self.add_node(new_node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.remove_tail()
                # del self.cache[tail.key]
                self.size -= 1
            




# solution two: order dict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity 
        

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
#         if len(self) > self.capacity:
# #             self.popitem(last = False)


# time complexity O(1)
# space complexity O(capacity)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)