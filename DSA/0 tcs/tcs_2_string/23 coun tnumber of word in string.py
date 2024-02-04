# print()
# count number of words in string  

# ip = google doc avira sharma 
# op = 4 

def f(s):
    
    arr = s.split()   
    count = 0 

    for x in arr:
        count += 1            
    return count 

if __name__=="__main__":
    s = 'google doc aviral sharma'
    print(f(s))

