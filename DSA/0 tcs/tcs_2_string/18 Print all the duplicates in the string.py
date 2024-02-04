
# Example 1:

# Input:
# str= "sinstriiintng"

# Output : 
# i - 4
# n - 3
# s - 2
# t - 2




# m 1 

def f( s):

    freq= [0]*200 

    for x in s : 
        freq[ord(x)] +=1 

    # for y in freq :  # * yaha avoid ye wala loop     
    #     if y > 1 : 
    #         print( freq[chr(y)] , y)  # * error 

    for i in range(len(freq)) : 
        if freq[i] > 1 : 
            print( chr(i) , freq[i] )


if __name__=="__main__":
    s = "sinstriiintng"
    f(s)


print( )
# m 2
 
# hash map  in c++ == mapping or dictinory in pyhton 

def f( s):

    str = ""  # impo  No space between " "

    mp ={ }

    for x in s : 
        if x in mp :
            mp[x] += 1
        else:
            mp[x] = 1 

    return mp 

if __name__=="__main__":

    s = "sinstriiintng"
    
    ans = f(s)
    for y in ans: 
        if ans[y] != 1 :
            #   print(y , ans[y] )
            print(f"{y} --> {ans[y]}")
    
    print()




    



