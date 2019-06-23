class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = tempSum = 0
        cumSum = {}
        cumSum[0] = 1
        
        for i in A:
            tempSum += i
            temp = tempSum % K
            if temp in cumSum:
                count += cumSum[temp]
                
            if tempSum % K in cumSum:
                cumSum[tempSum%K] += 1
            else:
                 cumSum[tempSum%K] = 1
        return count
        
