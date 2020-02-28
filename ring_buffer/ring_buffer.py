from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            self.storage.tail.value = item
            buffer = self.storage.tail
            while self.storage.tail == buffer:
                print(f' value in get {self.storage}')
                temp = self.storage.head.next
                current_value = self.storage.head
                current_value, temp = current_value, temp
                # current_value = temp
            self.storage.remove_from_head()
            self.storage.move_to_front(buffer)
            print(self.storage.head.value)
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
                print(current.value)
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
