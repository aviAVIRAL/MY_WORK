





print()

print()


def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[ord(x) - ord('a')] += 1

    # Printing Non-Repeating Characters
    for x in s :
        if freq[ord(x) - ord('a')] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 



print()
print()
print()
print()


def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[ord(x)] += 1

    print(freq )
    # Printing Non-Repeating Characters
    for x in s :
        if freq[ord(x)] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 



print()
print()






