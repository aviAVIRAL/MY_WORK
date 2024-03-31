
# super incre Arr



def f(n, k , x):

    if  x >= 2**(k-1) :
        return "Yes"
    else :
        return "No"  





if __name__=="__main__":
    T = int(input())
    for _ in range(T):    
        n,k,x = map(int,input().split())
        print(f(n, k, x))

