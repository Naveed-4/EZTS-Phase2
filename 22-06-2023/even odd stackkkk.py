#Create Stack using user input and display even no.s from stackstack = []

'''Create a stack using user input and display even numbers from stack

'''
# STACK
stack=[]

def push(n):
    for i in range (n):
        ele=int(input("Enter element:"))
        stack.append(ele)
    print("Insertion Succesful!!")
    
def pop():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("Removed Element:",e)
       
def display():
    print(stack)
def peek():
    print("PEEK ELEMENT IS:",stack[len(stack)-1])
while True:
    print("\nSelect Operation :\n1.PUSH \n2.POP \n3.DISPLAY STACK \n4.PEEK ELEMENT \n5.EXIT")
    choice=input()
    match choice:
        case '1':
            n = int(input("Enter total no.of elements :"))
            push(n)
        case '3':
            even, odd=[],[]
            for x in stack:
                if x%2==0:
                    even.append(x)
                else:
                    odd.append(x)
            opt=input("1 or 2:")
            
            if opt=='1':
                print(even)
            elif opt=='2':
                print(odd)
            else:
                print("Error!Try Again!")
        case '4':
            peek()
        case '5':
            exit()
        case _:
            print("PLEASE ENTER VALID INPUT")