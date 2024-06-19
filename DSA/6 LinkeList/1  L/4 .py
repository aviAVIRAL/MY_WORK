
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev =  None

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])# temp = Node(arr[i], None, prev)
        temp.prev = prev # impo 
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
