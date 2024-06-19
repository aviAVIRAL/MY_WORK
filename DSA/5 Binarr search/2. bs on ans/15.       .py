def kth_element(nums1, nums2, m, n, k):
    if m > n:
        return kth_element(nums2, nums1, n, m, k)
    low = max(0, k-m)
    high = min(k, n)
    while low <= high:
        cut1 = (low+high)//2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
        r1 = float('inf') if cut1 == m else nums1[cut1]
        r2 = float('inf') if cut2 == n else nums2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1
    return 1




if __name__ == '__main__':
    nums1 = [2, 3, 6, 7, 9]
    nums2 = [1, 4, 8, 10]
    m = len(nums1)
    n = len(nums2)
    k = 5
    print(
        f'The element at the kth position in the final sorted array is {kth_element(nums1, nums2, m, n, k)}')


def kth_element(nums1, nums2, m, n, k):
    if m > n:
        return kth_element(nums2, nums1, n, m, k)
    low = 0
    high = n
    while low <= high:
        cut1 = (low+high)//2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
        r1 = float('inf') if cut1 == m else nums1[cut1]
        r2 = float('inf') if cut2 == n else nums2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1
    return 1




if __name__ == '__main__':
    nums1 = [2, 3, 6, 7, 9]
    nums2 = [1, 4, 8, 10]
    m = len(nums1)
    n = len(nums2)
    k = 5
    print(
        f'The element at the kth position in the final sorted array is {kth_element(nums1, nums2, m, n, k)}')
