#	IMPLEMENTATION OF ARRAY

def Array_Operations(array):
    ch = int(input("1. Insert\n2. Delete\n3. Search\n4. Sort\n0. Exit\n\t Choice : "))
    match ch:
        case 1:
            x = int(input(("Enter an element to insert : ")))
            array.append(x)
            print(array)
        case 2:
            #delete an element or from index ???????
            print(array)
            dlt = int(input("\t1. Delete an element \n\t2.Delte thru index pos\n\t\t Choice : "))
            if dlt == 1:
                x = int(input(("Enter an element to delete: ")))
                array.remove(x)
                print(array)
            elif dlt == 2:
                x = int(input(("Enter element pos to delete : ")))
                array.pop(x)
                print(array)
        case 3:
            x = int(input(("Enter an element to search: ")))
            if x in array:
                print("Element exits at pos ", array.index(x))
            else:
                print("Element doesnt exist")
        case 4:
            print("Sorted Array :-\n", array)
        case 5:
            return 0
        case _:
            print("Invalid Choice. Try Again")
    input("Press Enter to continue")
    Array_Operations(array)
    
n = int(input("Enter array size :")) #n : size of array
print("Enter ", n, "elements :-")
array = list(map(int, input().split()[:n]))
print("Formed list is :", array)
Array_Operations(array)

""" Druva/Group Code
l1=[]
while(True):
    print("1.Insert\n2.Search\n3.Delete\n4.Sort\n5.Quit")
    z=int(input("Enter your choice"))
    match z:
        case 1:
            n=int(input("Enter size of the array"))
            for i in range(n):
                o=int(input("Enter your element"))
                l1.append(o)
            print(l1)
        case 2:
            k=int(input("Enter element to be searched"))
            if k in l1:
                print(k,"Element found")
            else:
                print("Element not found")
        case 3:
            k=int(input("Enter element to delete"))
            if k in l1:
                l1.remove(k)
                print("Deletion Successful")
                print(l1)
            else:
                print("Element not in the list")
        case 4:
            l1.sort()
            print("sorted elements")
            print(l1)
        case 5:
            break
"""