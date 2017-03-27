# 1-demension array peak find

def brute_force(A):
    for i in range(1,len(A)-1):
        if A[i]>=A[i-1] and A[i]>=A[i+1]:
            return A[i]
def divide_conquer(A,i,j):
    if i == j:
        return A[i]
    mid = (i+j)/2
    if mid-1 >=0 and A[mid] < A[mid-1]:
        return divide_conquer(A,i,mid-1)
    elif mid+1<=j and A[mid] < A[mid+1]:
        return divide_conquer(A,mid+1,j)
    else:
        return A[mid]
    

if __name__ == '__main__':
    A = [1,3,4,5,4]
    print brute_force(A)
    print divide_conquer(A,0,len(A)-1)



