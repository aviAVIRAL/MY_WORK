
# inserting at head 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insert_at_first(value, head):
    temp = ListNode(value)
    temp.next = head
    head = temp    # no need 
    return head   # return temp  act as head 

def print_list(head):
    curr = head
    while curr != None: # while curr is not None:
        print(curr.val, end="  ")
        curr = curr.next
  

if __name__ == "__main__":
 
    arr = [12, 5, 8, 7]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])


    head = insert_at_first(6, head)
 
    print_list(head)

print()
# also rep 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insert_at_first(value, head):
    temp = ListNode(value)
    temp.next = head
    # head = temp    # no need 
    return temp   # return temp  act as head 

def print_list(head):
    temp = head
    while temp != None: # while temp is not None:
        print(temp.val, end="  ")
        temp = temp.next
  

if __name__ == "__main__":
 
    arr = [12, 5, 8, 7]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])


    head = insert_at_first(6, head)
 
    print_list(head)


print()
# also repre  

class ListNode:
    def __init__(self, x, nextnode = None):  # i m p o
        self.val = x
        self.next = nextnode

def insert_at_first(value, head):
    temp = ListNode(value, head)  #impo node[val,next->head]
    # temp.next = head
    # head = temp    # no need 
    return temp   # return temp  act as head 

def print_list(head):
    curr = head
    while curr != None: # while curr is not None:
        print(curr.val, end="  ")
        curr = curr.next
  

if __name__ == "__main__":
 
    arr = [12, 5, 8, 7]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])


    head = insert_at_first(6, head)
 
    print_list(head)

















