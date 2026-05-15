class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict= {}
        for i, n in enumerate(nums):
            x = target - n 
            if x in numsdict:
                return [numsdict[x], i] 
            numsdict[n] = i