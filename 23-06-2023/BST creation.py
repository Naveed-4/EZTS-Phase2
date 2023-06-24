class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 88)
r = insert(r, 40)

inorder(r)