# Leetcode 4 find the median of two sorted array
def findMedianSortedArray(A,B):
    c = sorted(A+B)
    mid = len(c)/2
    if len(c) % 2 == 0:
        return (c[mid-1]+c[mid])/2.0
    else:
        return c[mid]
def find_Divide_Conquer(A,B):
    n = len(A) + len(B)
    if n % 2 == 1:
        return findKth(A, B, n/2+1)
    else:
        s = findKth(A, B, n/2)
        l = findKth(A, B, n/2+1)
        return (s+l)/2.0

def findKth(A,B,k):
    if len(A) == 0:
        return B[k-1]
    if len(B) == 0:
        return A[k-1]
    if k == 1:
        return min(A[0],B[0])
    if len(A) >= k/2:
        a = A[k/2-1]
    else:
        a = None
    if len(B) >= k/2:
        b = B[k/2-1]
    else:
        b = None
    if a is None or (a is not None and a > b):
        return findKth(A,B[k/2:],k-k/2)
    return findKth(A[k/2:],B,k-k/2)

if __name__ == '__main__':
    A = [1,2,3,4,5,6,8,9]
    B = []
    print findMedianSortedArray(A,B)
    print find_Divide_Conquer(A,B)
