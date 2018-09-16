class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A = list(A)
        if len(A) == 1:
            return A[0]
        A = sorted(A)
        i = 0
        while(i < len(A)-2):
            if A[i] == A[i+1]:
                i = i + 3
            else: 
                return A[i]
        return A[-1]       
