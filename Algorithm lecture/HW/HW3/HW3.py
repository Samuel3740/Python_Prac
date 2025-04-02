class Node(object):
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def delete_node(node):
    if node.left is None and node.right is None:
        return None
    elif node.left is not None and node.right is None:
        return node.left
    elif node.right is not None and node.left is None:
        return node.right
    else:
        s = node.right
        parent = None
        while s.left is not None:
            parent = s
            s = s.left
        node.key = s.key
        if s == node.right:
            node.right = s.right
        else:
            parent.left = s.right
        return node

def delete(root, node):
    if node == root:
        return delete_node(node)
    elif node == node.parent.left:
        node.parent.left = delete_node(node)
        if node.parent.left:
            node.parent.left.parent = node.parent
    else:
        node.parent.right = delete_node(node)
        if node.parent.right:
            node.parent.right.parent = node.parent
    return root