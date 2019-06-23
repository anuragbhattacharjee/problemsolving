class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = tempSum = 0
        cumSum = {}
        cumSum[0] = 1
        
        for i in nums:
            tempSum += i
            temp = tempSum - k
            if temp in cumSum:
                count += cumSum[temp]
                
            if tempSum in cumSum:
                cumSum[tempSum] += 1
            else:
                 cumSum[tempSum] = 1
        return count
