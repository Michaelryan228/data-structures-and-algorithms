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


    def insert_after(self, target, new_value):
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

    def insert_before(self, target, new_value):
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

def linked_list_zip(linklist1, linklist2):
    if linklist1.head is None and linklist2.head is None:
        return None
    if linklist1.head is None:
          return linklist2
    if linklist2.head is None:
            return linklist1

    l1cur = linklist1.head
    l1next = l1cur.next
    l2cur = linklist2.head
    l2next = l2cur.next
    while l1next and l2next:
        l1cur.next = l2cur
        l2cur.next = l1next
        l1cur = l1next
        l2cur = l2next
        l1next = l1next.next
        l2next = l2next.next
    if l1next is None and l2next is None:
        l1cur.next = l2cur
        return(linklist1)
    if l1next is not None:
        l1cur.next = l2cur
        l2cur.next = l1next
        return(linklist1)
    if l2next is not None:
        l2cur.next = l2cur
        return(linklist1)


if __name__ == "__main__":

    pass
