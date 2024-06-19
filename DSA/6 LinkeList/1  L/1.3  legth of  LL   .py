

print()

class Node:
    def __init__(self, data, next_pointer=None):
        self.data = data
        self.next = next_pointer

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    mover = head
    cnt = 0  #
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
        cnt += 1 #
    return cnt

if __name__ == "__main__":
    arr = [2, 4, 5]
    length  = convert_arr_to_ll(arr)
    print(length )
    