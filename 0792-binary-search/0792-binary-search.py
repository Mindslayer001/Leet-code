class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1