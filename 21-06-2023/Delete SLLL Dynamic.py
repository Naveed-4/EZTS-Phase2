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
        
    #Delete at begining
    def delete_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    #Delete at End
    def delete_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev= prev.next
        prev.next = None #Last 2nd node
        
    #Delete at a pos
    def delete_at_pos(self, pos):
        temp = self.head.next
        prev = self.head
        
        for i in range(1, pos):
            temp = temp.next
            prev = prev.next
        prev.next=temp.next
        temp.next=None
        
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

while(1):
    x=int(input("\nAvailable operations\n\t1. Delete at Begin \n\t2. Delete at End\n\t3. Delete at a index pos\n\t0. Exit\n\t\tChoice :"))
    match x:
        case 1:
            sll_list1.delete_at_beg()
            sll_list1.display()
        case 2:
            sll_list1.delete_at_end()
            sll_list1.display()
        case 3:
            sll_list1.display()
            data = int(input("Enter index pos to delete :"))
            sll_list1.delete_at_pos(data)
            sll_list1.display()
        case 0:
            break
        case _:
            print("Invalid option . Try Again")
            
    
