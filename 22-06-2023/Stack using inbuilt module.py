#METHOD 2nd
#While implementing stack using LL we can opt/use this method also
#Here we do insert node at beginning, delete in the head/first node.
# NOTE:- In these two methods, 2nd is effiecient cuz in the 1st to do the pop() operation we have to traverse till last node4

from queue import LifoQueue

s = LifoQueue(maxsize=3)

print(s.qsize())

s.put('a')
s.put('b')
s.put('c')

print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())