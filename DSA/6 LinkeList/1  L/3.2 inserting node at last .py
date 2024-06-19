print("aa")
# also rep 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_last(x, head): 
    # edge case  
    if head is None:
        return Node(x) 
# If the list is empty, create a new node and return it as the head
# or rep    
    # if head == None:
    #     return Node(x)

    temp = head 
    while temp.next != None:
        temp = temp.next
    newnode = Node(x)
    temp.next = newnode

    return head   # return temp  act as head 

def print_list(head):
    temp = head
    while temp != None: # while temp is not None:
        print(temp.data, end="  ")
        temp = temp.next
  
if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])


    head = insert_at_last(6, head)
 
    print_list(head)


print()




