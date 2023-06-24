class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        if self.tail is None:
            self.head=Node(data)
            self.tail = self.head
        else:
            self.tail.next=Node(data)
            self.tail = self.tail.next
            
    def search(self, key):
        temp = self.head
        while temp:
            if(temp.data == key):
                print("Element found")
                return
            temp=temp.next
        print("Element not found")
        
    def display(self):
        if self.head is None:
            print("LL is empty")
        else:
            print()
            temp = self.head
            while temp.next:
                print(temp.data, end='->')
                temp = temp.next
            print(temp.data)


sll_list1 = SLL()
n = int(input("Enter no.of ele :"))
for i in range (n):
    data = int(input("Enter data value :"))
    sll_list1.append(data)
    
sll_list1.display()

key = int(input("Enter data value to search for :"))
sll_list1.search(key)

