





# def f ( s): 

# #     frq = [0]*200

# #     for x in s :
# #         frq [ ord(x)  -  ord ('a') ] +=1 

    
# #     # max = -float('inf')

# #     for x in s :
# #         frq[ord(x)  -  ord ('a')]
# #     return  x  

# # if __name__=="__main__": 
# #     s = "aviralaaaazzzz"
# #     print(f(s))

# print (" upeer wala wrong ")
print ()


def max_occuring_char(s):
    ans = ''
    max_freq = 0
    freq = [0] * 256
    
    for x in s:
        freq[ord(x)] += 1
        if freq[ord(x)] > max_freq:
            max_freq = freq[ord(x)]
            ans = x
    
    return ans

if __name__ == "__main__":
    string_input = "takeuforward"
    print("Maximum occurring character is", max_occuring_char(string_input))


# .........................................
print('.....................')
print('.....................')
print('.....................')









