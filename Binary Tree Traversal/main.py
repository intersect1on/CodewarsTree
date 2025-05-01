class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node):
    if not node:
        return []

    return [node.data] + pre_order(node.left) + pre_order(node.right)

def in_order(node):
    if not node:
        return []

    return in_order(node.left) + [node.data] + in_order(node.right)

def post_order(node):
    if not node:
        return []

    return post_order(node.left) + post_order(node.right) + [node.data]
