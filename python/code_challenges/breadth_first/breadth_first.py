from queues.queues import Queue


def breadth_first(tree):

    if tree.root is None:
        return []

    queueu = Queue()
    queueu.enqueue(tree.root)
    result_list = []

    while not queueu.isEmpty():

        front = queueu.dequeue()

        if front.left:
            queueu.enqueue(front.left)

        if front.right:
            queueu.enqueue(front.right)

        result_list.append(front.value)

    return result_list
