









# # def f(s):
    
# #     for i in range(1, len(s)):
# #         if s[i].isdigit():
# #             newstr = s.replace(s[i],"")
# #             break        
# #     return(f(newstr))

# # if __name__=="__main__":
# #     s = "cd34"
# #     print(f(s))


# def f(s):
#     for i in range(len(s)):
#         if s[i].isdigit():
#             # Remove the digit character at index i
#             s = s[:i] + s[i+1:]
#             # Call the function recursively with the updated string
#             return f(s)
#     # Base case: return the string if no digits are found
#     return s

# if __name__ == "__main__":
#     s = "cd34"
#     print(f(s))  # Output: cd




# # s = 'cdc34'
# # substring_to_remove = '34'

# # if substring_to_remove in s:
# #     new_string = s.replace(substring_to_remove, '')
# # else:
# #     new_string = s

# # print(new_string)  # Output: cdc




# # .....




print()

arr =  [ 1,2,3,4,5]
v = arr.pop(1)
print(v)
print(arr)

print()
print()
def f(s):
    ans = []
    for c in s:
        if c.isdigit():
            ans.pop()
        else:
            ans.append(c)
    return "".join(ans)

s = "cb34"
print(f(s))

s = "abc"
print(f(s))
print("...")
print()
def f(s):
    ans = []
    for c in s:
        if c.isdigit():
            ans.pop()
        else:
            ans.append(c)
    print(ans)
    y = ans.pop()
    print(y, end = " ")
    print()

    return "".join(ans)

print()
s = "abc"
print(f(s))


print( 1, 2 )
print( {1, 2 })
print( f"{1}, {2}")






