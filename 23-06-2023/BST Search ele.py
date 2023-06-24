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

# Perform Inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Search for a value using Inorder traversal
def find(root, x):
    if root is None:
        return False

    if root.key == x:
        return True

    if x < root.key:
        return find(root.left, x)
    else:
        return find(root.right, x)

# 10, 5, 15, 2, 7, 12, 17

l = [10, 5, 15, 2, 7, 12, 17]

root = None
r = Node(10)
for i in l:
    r = insert(r, i)

inorder(r)

x = int(input("\nEnter a value to search: "))
if find(r, x):
    print("Found")
else:
    print("Not Found")
