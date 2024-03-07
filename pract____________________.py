





arr= [1,2,1,4,5]
n = len(arr)
cnt = 0 

mini1= float("inf")
mini2= float("inf")

for i in range(n):
    if arr[i] < mini1:
        mini1 = arr[i]
for i in range(n):
    if arr[i] <= mini1 or arr[i] < mini2 :
        mini2 = arr[i]

print(mini1) 
print(mini2) 











