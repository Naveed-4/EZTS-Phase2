# STACK #Follows LIFO concept
# Stack implementation:- 1. Using arrays 2. LL 3. In-built modules
# Insertion and Deletion nhappens from the same end (TOP)

stack = []

def push():
    stack.append(int(input("Enter element to push :")))
    #display()

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print("Popped element is :",stack.pop())
        #display()
        
def display():
    if not stack:
        print("Stack is empty")
    else:
        print(stack)
    
def peek():
    print("Peek/Top of stack is :", stack[len(stack)-1])
    

while True:
    ch = input("\nAvailable Operations:-\n1. Push\n2. Pop\n3. Display\n4. Peek\n0. Exit\n\tChoice :")
    match ch:
        case '1':
            push()
        case '2':
            pop()
        case '3':
            display()
        case '4':
            peek()
        case '0':
            break
        case _:
            print("Invalid option try again.")
    