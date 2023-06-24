class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__ (self):
        self.head=None

    def insert_at_pos(self, pos, data):
        newn = node(data)
        temp=self.head
        for _ in range (pos-1):
            print('hi')
            temp = temp.next
        newn.next=temp.next
        temp.next=newn
        self.display()
    
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head  #temp = first node
            while temp.next:
                print(temp.data, "-->", end=' ')
                temp = temp.next
            print(temp.data)
                    
obj = SLL()
n1 = node(10)
obj.head=n1
n2 = node(20)
obj.head.next=n2  #or n1.next = n2
n3 = node(30)
n2.next = n3
n4 = node(40)
n3.next = n4
obj.display()

obj.insert_at_pos(int(input("Enter pos to add at :")), int(input("Enter data value :")))