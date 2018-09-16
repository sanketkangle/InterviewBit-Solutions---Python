class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A >= 0:
            n = len(str(A))
            A = int(A)
            p = 0
            for i in range(n-1, -1, -1):
                p = p + (A%10)*(10**i)
                A=A//10
            if p > 2**31 - 1:
                return 0
            else:
                return p
        
        else:
            A= (-1)*A
            n = len(str(A))
            A = int(A)
            p = 0
            for i in range(n-1, -1, -1):
                p = p + (A%10)*(10**i)
                A= A//10
            if p > 2**31 - 1:
                return 0
            else:
                p = (-1)*p
                return p
