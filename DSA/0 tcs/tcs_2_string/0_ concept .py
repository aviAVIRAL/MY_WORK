
print("........START..........")
# .........................
# important concept 
# .........................

s =  "avijiyl"
x = s.split()
print(x)

print()
s =  "avi ji yl"
x = s.split()
print(x)


print()
s = "1234"
x = s.split()
print(x)

print()
s = "1 2 3 4 "
x = s.split()
print(x)

print()
print("...''.join(s)......")
print()

# .........................

# s is a list of substrings
s = ['avi', 'ji', 'hy']
ans = ''.join(s)
print(ans)

print()
s = ['avi', 'ji', 'hy']
ans = ' '.join(s)
print(ans)

print()
lis = ['1','2','3','4']
sol =  ''.join(lis)
print(sol)


lis = [1 , 2, 3, 4]
sol = ''.join(map(str, lis))
print(sol)


lis =  [1 , 2, 3, 4]
sol = ''.join(str(x) for x in lis)
print(sol)


# ......................

print()

s = "avi"
x = list(s)
print(x)
print()

s = "avi ji yl"
x = list(s)
print(x)
print()

s = "1234"
x = list(s)
print(x)
print()

s = "1 2 3 4"
x = list(s)
print(x)
print()

