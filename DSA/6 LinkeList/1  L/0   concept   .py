if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create a list of nodes
    nodes = [Node(data) for data in arr]

    # Link the nodes together
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # The head of the linked list
    head = nodes[0]

    # Delete the tail of the linked list
    head = delete_tail(head)

    # Print the modified linked list
    print_ll(head)


# ................................
# convert arr into linkelist 
# ................................      

if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Delete the tail of the linked list
    head = delete_tail(head)

    # Print the modified linked list
    print_ll(head)


# ...........................































