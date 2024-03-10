def max_hamburgers(recipe, nb, ns, nc, pb, ps, pc, r):
    # Count the number of each ingredient needed
    bread_count = recipe.count('B')
    sausage_count = recipe.count('S')
    cheese_count = recipe.count('C')
    
    # Initialize the maximum number of hamburgers
    max_hamburgers = 0
    
    # Binary search to find the maximum number of hamburgers Polycarpus can make
    low = 0
    high = 10**12  # Maximum number of hamburgers possible
    while low <= high:
        mid = (low + high) // 2
        # Calculate the cost of ingredients for mid hamburgers
        cost = max(0, bread_count * mid - nb) * pb + max(0, sausage_count * mid - ns) * ps + max(0, cheese_count * mid - nc) * pc
        if cost <= r:
            max_hamburgers = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return max_hamburgers

# Read input
recipe = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

# Print the maximum number of hamburgers Polycarpus can make
print(max_hamburgers(recipe, nb, ns, nc, pb, ps, pc, r))





