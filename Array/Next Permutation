class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        i = len(A) - 2
        while A[i]>= A[i+1]:
            i = i - 1
            if i < 0:
                break
        if i < 0:
            A = A[::-1]
            return A
        else:
            j = len(A) - 1
            while A[j] <= A[i]:
                j -= 1
            A[i],A[j] = A[j],A[i]
            A[i+1:] = sorted(A[i+1:])
            return A
