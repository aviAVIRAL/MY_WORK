





cnt = 0
def f():
    global cnt 
    if cnt == 5 : return 
    cnt += 1 
    print("acv")
    f()

if __name__=="__main__":
    f()






# def f():
#     cnt = 0  

#     if cnt == 5 : return 
#     cnt += 1 
#     print("a")
#     f()

# if __name__=="__main__":
#     f()