class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__ (self):
        self.head=None
        
    def insert_end(self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp = temp.next
        temp.next=ne
        ne.next=None

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head  #temp = first node
            while temp:
                print(temp.data, "-->", end=' ')
                temp = temp.next
                    
obj = SLL()
n = node(10)
obj.head=n
n1 = node(20)
obj.head.next=n1
n2 = node(30)
n1.next = n2
n3 = node(40)
n2.next = n3
obj.display()
