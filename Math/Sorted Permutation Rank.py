class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        def fact(n):
            if n == 0:
                return 1
            else:
                return n*(fact(n-1))
        l = list(A)
        m = sorted(l)
        arr = []
        for i in l:
            arr.append(m.index(i))
        word = [0]*len(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i]:
                    word[i] += 1
        tot_words = [0]*len(arr)
        n = 0
        for i in range(len(arr)-1, -1,-1):
            tot_words[i] = word[i]*fact(n)
            n = n + 1
        sum_of_no = 0
        for i in tot_words:
            sum_of_no += i
        sum_of_no += 1
        return sum_of_no%1000003
