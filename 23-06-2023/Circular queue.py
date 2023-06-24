# Circular Queue		#FIFO

# Diagram  https://www.geeksforgeeks.org/introduction-to-circular-queue/

# In a normal queue even if there's space after deleting item we would not be able to utilize those spaces.
# In order to use those spaces we are coming with this concept Circular queue

# 1. Initializing Circular queue:
# 			Front = rear = -1
# 2. Insertion happens at rear
# 3. Delete happens at front
# 4. Inserting first element:
#			Front = rear = 0
# 5. Insertion from there after:
#			rear = rear +1		thgen insert
# 6. Deletion: After deleting front element:
#				front = front +1

# Example

class CircularQueue:
    def __init__(self, size):
        #initializing the class
        self.size = size
        #can use self.queue=[None]*size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
        
    def enqueue(self, data):
        #condition if Queue is Full
        if ((self.rear+1)%self.size == self.front):
            print("Queue is Full")
        #Conditio for Empty Queue
        elif(self.front==-1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            #alwasy add element at rear place
        else:
            #next position of rear
            self.rear = (self.rear +1)%self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if (self.front == -1):
            # condition for empty queue
            print("Queue is empty")
        #Condition for only one element
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1)%self.size
            return temp
    def display(self):
        #COndition for empty queue
        if (self.front == -1):
            print("queue is empty")
        elif (self.rear >= self.front):
            print("Elemets in the Circular queue :")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = ' ')
            print()
        else:
            print("Elements in Circular  Queue are :", end= '')
            for i in range (self.front, self.size):
                print(self.queue[i], end = '')
            for i in range(0, self.rear+1):
                print(self.queue[i], end = '')
            print()
        if( (self.rear +1)%self.size == self.front):
            print("Queue is Full")
            
cq1 = CircularQueue(5)

cq1.enqueue(14)
cq1.enqueue(22)
cq1.enqueue(13)
cq1.enqueue(-6)

cq1.display()

print("Deleted value : ", cq1.dequeue())
print("Deleted value : ", cq1.dequeue())

cq1.display()
cq1.enqueue(9)
cq1.enqueue(20)