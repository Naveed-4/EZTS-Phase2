class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp.next:
                print(temp.data, end="->")
                temp = temp.next
            print(temp.data)

# Create nodes
obj = LinkedList()

n1 = Node(10)
obj.head = n1

n2 = Node(20)
n1.next = n2

n3 = Node(30)
n2.next = n3

n4 = Node(40)
n3.next = n4

n5 = Node(50)
n4.next = n5

obj.display()