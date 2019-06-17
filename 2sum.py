class Solution:
    def duplicates(self, lst, item):   
        return [i for i, x in enumerate(lst) if x == item]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        srt = nums[:]
        srt.sort()
        i = 0
        while(i < len(srt)):
            if srt[i] > target/2:
                break
            j = i+1; 
            while(j < len(srt)):
                if  (srt[i] + srt[j]) > target:
                    break
                if  (srt[i] + srt[j]) == target:
                    first = nums.index(srt[i])
                    second = nums.index(srt[j])
                    if first == second:
                        dpl = self.duplicates(nums, srt[i])
                        if len(dpl) >1:
                            lst.append(dpl[0])
                            lst.append(dpl[1])
                    else:
                        lst.append(first)
                        lst.append(second)
                    return lst
                j += 1
            i += 1
