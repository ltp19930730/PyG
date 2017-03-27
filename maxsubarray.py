import sys

# algorithm using Divide and Conquer 
# ITA3_PAGE_73
def Find_max_crossing_subarray(A,low,mid,high):
    left_sum = -sys.maxsize-1
    sum = 0
    for i in range (mid,low-1,-1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -sys.maxsize-1
    sum = 0
    for j in range(mid+1,high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return left_sum + right_sum

def Find_max_subarray(A,low,high):
    if low == high:
        return A[low]
    else:
        mid = (low+high)//2
        left_sum = Find_max_subarray(A,low,mid)
        right_sum = Find_max_subarray(A,mid+1,high)
        cross_sum = Find_max_crossing_subarray(A,low,mid,high)
        return max(left_sum,right_sum,cross_sum)


if __name__ == '__main__':
    A = [0,3,4,-2,-3,11,2]
    print (Find_max_crossing_subarray(A,0,0,1))
    print (Find_max_subarray(A,0,6))
