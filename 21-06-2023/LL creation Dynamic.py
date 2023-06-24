class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__ (self):
        self.head=None
        self.tail=None
        
    def append(self, data):
        if self.tail is None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail=self.tail.next

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head  #temp = first node
            while temp:
                print(temp.data, "-->", end=' ')
                temp = temp.next
                    
sll_list1 = SLL()
n=int(input("Enter how many elements :"))
for i in range(n):
    data = int(input("Enter data item :"))
    sll_list1.append(data)

sll_list1.display()
