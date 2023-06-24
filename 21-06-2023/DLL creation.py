class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("DLL is empty")
        else:
            print()
            temp = self.head
            while temp.next:
                print(temp.data, end='<-->')
                temp = temp.next
            print(temp.data)
            
dll_list1 = DLL()

n1 = Node(10)
dll_list1.head = n1

n2=Node(20)
n1.next = n2
n2.prev = n1

n3=Node(30)
n2.next = n3
n3.prev = n2

dll_list1.display()