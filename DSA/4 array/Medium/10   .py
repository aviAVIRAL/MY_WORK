





def f(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    for i in range(n):
        st.add(a[i])

    for elm in st:
        if elm - 1 not in st:
            cnt = 1
            x = elm
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

if __name__=="__main__":
    a = [100,200,1,2,3,3,101,101,2,3, 4]
    ans = f(a)
    print(ans)
