class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, node=None):
        self.head = node

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return self

    def includes(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"{ {current.value} } -> "
            current = current.next
        string += " None "
        return string

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return self

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

    def kth_from_end(self, k):
        length = -1
        temp = self.head
        while temp is not None:
            temp = temp.next
            length += 1
        if length < 2:
            return 'List only has 1 item'
        elif k < 0:
            return 'Choose a positive number'
        elif k >= length:
            return 'choose a smaller number'
        else:
            temp = self.head
            target = length - k
            for i in range(0, target):
                temp = temp.next
            return temp.value
if __name__ == "__main__":
    pass


list1 = LinkedList(1, Node(3, Node(5, Node(7, Node(9)))))
list2 = LinkedList(2, Node(4, Node(6, Node(8, Node(10)))))

def zipLists(list1, list2):
  list1_current = list1.head
  list2_current = list2.head

  while list1_current and list2_current != None:
          list1_next = list1_current.next
          list2_next = list2_current.next

          list1_current.next = list2_current
          list2_current.next = list1_next

          list1_current = list1_next
          list2_current = list2_next

  list2.head = list2_current
