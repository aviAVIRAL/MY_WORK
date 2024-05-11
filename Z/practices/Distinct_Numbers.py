

n = int(input())
arr = list(map(int, input().split(" ")))

mp = {}
for x in arr : 
    if x not in mp : mp[x] = 1
    else : mp[x] += 1 
cnt = 0 
for x in mp :
    cnt += 1 
print(cnt) 
    



