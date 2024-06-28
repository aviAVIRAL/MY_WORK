






def f(i,ans ):
    if i < 1  :
        print(ans) 
        return 
    f(i - 1 , i*ans)

f(3, ans = 1)








