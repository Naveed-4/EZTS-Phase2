# QUEUE using
# Insertion and deletion happends at differeent sides.
# QUEUE implementation using list/array

queue=[]
def enqueue():
    element = input("Enter element")
    queue.append(element)
    print("Insertion Successful")

def dequeue():
    if not queue:
        print("Queue is Empty")
    else:
        e = queue.pop(0)
        print("Popped ele :", e)

def display():
    print(queue)

while True:
    print("Select Operations \n1. ADD\n2. REMOVE \n3. SHOW\n4. QUIT")
    ch = input()
    match ch:
        case '1':
            enqueue()
        case '2':
            dequeue()
        case '3':
            display()
        case '4':
            break