class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: 'TreeNode', key: int) -> 'TreeNode':
    if not root:
        return None

    if root.val < key:
        root.right = deleteNode(root.right, key)
    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        right_node = root.right
        right_min = right_node.val

        while right_node.left:
            right_node = right_node.left
            right_min = right_node.val

        root.val = right_min
        root.right = deleteNode(root.right, right_min)

    return root
