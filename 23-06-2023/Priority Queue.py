# Types of Queues
# 1. Circular Queue
# 2. Priority Queue

#		PRIORITY QUEUE
# Jobs will be in queue however priorir=ties will be assigned.	As for the priority task/jobs will be alloted
# Ex:- priority no. in priority scheduling algorithm

# Priority  queue (here high no. -> high priority)
students_grade = []

students_grade.append((1, 'Akash'))

students_grade.append((4, 'Ankitha'))

students_grade.append((3, 'Sid'))

students_grade.append((2, 'Akshay'))

print("Original queue :")

print(students_grade)

students_grade.sort(reverse = True)
print(type(students_grade))
print(type(students_grade[0]))
print(type(students_grade[0][0]))
print(type(students_grade[0][1]))
print(type(students_grade[0][2]))
print("priority wise sorted :")

print(students_grade)

