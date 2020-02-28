from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if not self.storage.length:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.storage.length < self.capacity:
            if self.storage.length == (self.capacity -1):
                self.current = self.storage.head
                self.storage.add_to_tail(item)
            else:
                self.storage.add_to_tail(item)
                self.current = self.storage.tail


        elif self.storage.length == self.capacity:
            self.storage.tail.next = self.storage.head
            # self.storage.head.prev = self.storage.tail
            self.current.value = item
            self.current = self.current.next
        return

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head

        # while current.next is not self.storage.head:
        # list_buffer_contents.append(current.value)
        # current = current.next
        iteration = self.capacity
        while iteration > 0:
            if current:
                list_buffer_contents.append(current.value)
                current = current.next
                iteration -= 1
            else:
                return list_buffer_contents

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
