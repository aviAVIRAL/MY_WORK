
#   gfg quetion hai . LL mein
#    bus head and target elem  given hoga,
#  you have to travel  and see the elem is present or not 

# ..................

# search elem in LL  

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

def searchelm(head, x):
    temp = head
    while temp: # while temp != None:
        if temp.data == x: return True 
        temp = temp.next
    return False

if __name__ == "__main__":
    arr = [2, 4, 5]
    head = convert_arr_to_ll(arr)
    x = 12
    ans  = searchelm(head, x )
    print(ans)

# op  False 













