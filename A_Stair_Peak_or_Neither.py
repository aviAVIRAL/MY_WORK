
def f(a, b, c):
    if a<b and b <c :
        return "STAIR"
    elif a<b and b>c :
        return "PEAK"
    else:
        return "NONE"



if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a,b,c = map(int, input().split())

        print(f(a,b,c))