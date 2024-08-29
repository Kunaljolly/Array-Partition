class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for x in range(0,len(nums),2):
            s += nums[x]
        return s

