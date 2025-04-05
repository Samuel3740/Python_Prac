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
            if s.right:
                s.right.parent = node
        else:
            parent.left = s.right
            if s.right:
                s.right.parent = parent
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

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)



# 트리 구성 예시
if __name__ == '__main__':

    #         17
    #       /    \
    #     6       21
    #    / \     /  \
    #   3   9   18   23

    root = Node(17)
    n6 = Node(6, root)
    n21 = Node(21, root)
    n3 = Node(3, n6)
    n9 = Node(9, n6)
    n18 = Node(18, n21)
    n23 = Node(23, n21)

    root.left = n6
    root.right = n21
    n6.left = n3
    n6.right = n9
    n21.left = n18
    n21.right = n23

    print("삭제 전 트리:")
    inorder(root)
    print()

    # 예시 트리에서 루트 노드(13) 삭제
    print(f"\n노드 {root.key} 삭제")
    root = delete(root, root)

    print("\n삭제 후 트리:")
    inorder(root)
    print()