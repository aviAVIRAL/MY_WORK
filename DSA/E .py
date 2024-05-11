




a,b,c = map(int,["1","2","3"])
print(a,b,c)



ans = list(map(int,["1","2","3"]))
print(ans)



# ans = map(int,["1","2","3"])
# print(ans)

# <map object at 0x0000025ABEF7B940>


print()

ans = map(int,["1","2","3"])

for x in ans :
    print(x, end= " ")

print()

a, b, c = map(int,["1","2","3"])

print(a,b ,c)


print()
# .............................................
# ans = map(int,["1","2","3"])
# for i in range(len(ans)):
#     print(ans[i], end = " ")


# in <module>
#     for i in range(len(ans)):
#                    ^^^^^^^^
# TypeError: object of type 'map' has no
#  len()
# ...........................................
# print(ans)

print()

ans = list(map(int,["123"]))
print(ans)

