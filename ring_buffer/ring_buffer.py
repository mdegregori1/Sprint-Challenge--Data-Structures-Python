from doubly_linked_list import DoublyLinkedList

#  When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element
# first thought, LRU 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if less than capacity
        # check if it exists
        # add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # if you add and it's the only thing in storage, set it as head
            if self.storage.length == 1:
                self.current = self.storage.head
        else:
        # set current value to value of item (Replace)
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
          

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # start at head
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
