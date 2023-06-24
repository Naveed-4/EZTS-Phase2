#InOrder using Stack 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    #set current to root of binary tree
    current = root
    stack = []
    done = 0
    while True:
        #Reach the left most Node of the current
        if current is not None:
            #Place point to a tree node on the stack
            #before traversing the node's left subtree
            stack.append(current)
            current = current.left
# Backtrack from empty subtree & visit Node
# at top of the stack
# however, if the stack is empty you are done
        elif(stack):
            current = stack.pop()
            print(current.data, end = ' ')
# We have visited this node and its left
# Subtree . How, Its right subtrees's turn
            current = current.right
        else:
            break
    print()

#INPUT
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)