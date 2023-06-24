# Get combination of brackets as input and check whether it is balanced or not

while True:
    stack = []

    def push(data):
        stack.append(data)
        #display()

    def pop():
        if stack:
            popped = stack.pop()
            #print("Popped element is :",popped)
            return popped
            #display()
            
    s = input()

    flag = 0
    for i in range (len(s)):
        if( s[i] == '(' or s[i]== '{' or s[i] == '[' ):
            push(s[i])
            #print(i, len(s), s[i])
        elif(s[i] == ')' or s[i]== '}' or s[i] == ']'):
            x = pop()
            if (x == '(' and s[i]!=')'):
                flag = 1
                print("Not balanced")
                break
            elif (x == '[' and s[i]!=']'):
                flag = 1
                print("Not balanced")
                break
            elif (x == '{' and s[i]!='}'):
                flag = 1
                print("Not balanced")
                break
            elif (x==None):
                flag = 1
                print("Not balanced")
                break
            #print(i, len(s), x, s[i])

    if flag == 0 and len(stack) == 0 and i == len(s)-1:
        print("Balanced")
    elif flag == 0:
        print("Not balanced")
        
        
                


