



# def f(cnt = 1, n):
     

#     if cnt == n : return 
#     cnt += 1 
#     print(cnt)
#     f(cnt, n)

# if __name__=="__main__":
#     f(1, 5)

def f(cnt, n):
    if cnt > n:  # Base case: stop when cnt exceeds n
        return
    print(cnt)  # Print the current number
    f(cnt + 1, n)  # Recursive call with incremented cnt

if __name__ == "__main__":
    f(1, 5)  # Start printing from 1 to 5
