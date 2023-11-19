class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        steps=0
        nums=sorted(nums)
        ele=nums[0]
        for i in range(len(nums)):
            if  ele<nums[i]:
                steps+=(len(nums)-i)
                ele=nums[i]
        return steps