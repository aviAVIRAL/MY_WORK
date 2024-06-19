

print()

class Node:
    def __init__(self, data, next_pointer=None):
        self.data = data
        self.next = next_pointer

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

if __name__ == "__main__":
    arr = [2, 4, 5]
    head = convert_arr_to_ll(arr)# traveses kr diya LL mein 
    temp = head
    while temp: # while temp != None:
        print(temp.data, end=" ")
        temp = temp.next
   
# 2 4 5  op 


print()
















