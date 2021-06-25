class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, node=None):
        self.head = node

    def insert(self, value):

        node = Node(value)

        node.next = self.head
        self.head = node
        return self

    def includes(self, target):

        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next

        return False

    def __str__(self):

        string = ""

        current = self.head

        while current is not None:
            string += f"{ {current.value} } -> "
            current = current.next

        string += f" None "

        return string

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return self


    def insertAfter(self, target, new_value):
        new_node = Node(new_value)

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return self
            current = current.next

        print("Target not within list")

    def insertBefore(self, target, new_value):
        new_node = Node(new_value)

        if self.head is None:
            return None

        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
            return self

        current = self.head

        while current is not None:
            if current.next.value == target:
                new_node.next = current.next
                current.next = new_node
                return self
            current = current.next

        print("Target not within list")


if __name__ == "__main__":

    pass
