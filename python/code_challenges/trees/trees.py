class Node:
    """
    Instantiate Node class
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """
    Create a Binary Tree class; Define a method for each of the depth first traversals: pre-order, in-order, post-order
    """

    def __init__(self, node=None, max_num=0):
        self.root = node
        self.max_num = max_num

    def pre_order(self):
        # root >> left >> right
        collection = []

        def traverse(root):
            if root != None:
                collection.append(root.value)
                traverse(root.left)
                traverse(root.right)
        return collection

    def in_order(self):
        # left >> root >> right
        collection = []

        def traverse(root):
            if root != None:
                traverse(root.left)
                collection.append(root.value)
                traverse(root.right)
        traverse(self.root)
        return collection
