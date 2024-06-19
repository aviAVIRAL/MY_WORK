print()



class Node:
    def __init__(self, data , nextnode = None, backnode = None):
        self.data = data
        self.next = nextnode
        self.back = backnode

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp   #  prev = prev.next 

    return head

def printDLL(head):
    while ( head is not None ): # head != None
        print(head.data, end = "->")
        head = head.next 

if __name__ == "__main__":
    arr = [12, 44, 5]
    head = convert_arr_to_dll(arr)
    printDLL(head)

print()#
# # also rep 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back =  None

def convert_arr_to_dlll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])# temp = Node(arr[i], None, prev)
        temp.back = prev # impo 
        prev.next = temp
        prev = temp   #  prev = prev.next 

    return head

def printDLL(head):
    while ( head is not None ): # head != None
        print(head.data, end = "->") 
# to handle edge casse print(head.data, end=" -> " if head.next else "")
        head = head.next 

if __name__ == "__main__":
    arr = [12, 44, 5]
    head = convert_arr_to_dlll(arr)
    printDLL(head)

# op  12->44->5->

# print(head.data, end=" -> " if head.next else "")
# op  12->44->5

# or also repre as  

# def printDLL(head):
#     while  head.next != None :
#         print(head.data, end = "->") 
#         head = head.next
#     print(head.data, end = " ") 



