"""A depiction of a linked list data structure"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list():
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_node_at(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert_node_at(self, position, new_node):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter < position:
            if counter == position - 1:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            counter += 1
        return None

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        if self.head:
            deleted_node = self.head
            temp_list = deleted_node.next
            self.head = temp_list
            return deleted_node
        else:
            return None
