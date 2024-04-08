
def f(x,y):
    if x+y >= 2000:
        return "YES"
    return "NO"


if __name__=="__main__":
    x, y = map(int, input().split())
    print(f(x,y))