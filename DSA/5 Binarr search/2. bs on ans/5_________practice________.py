

def f(a, k):
    fre = [0]*13
    for i in range(len(a)):
        fre[a[i]]  += 1
    fre.pop(0)
    
    print(fre) #[0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]    

    cnt = 0 
    for j in range(1, len(fre)):
        if fre[j] == 0 : cnt += 1 
        if cnt == k: break
   
    return j
arr= [ 2,3,4,7,11]
print(f(arr, 5))

# op 
# 9


