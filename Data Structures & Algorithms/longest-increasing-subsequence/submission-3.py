from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(index,last):

            if index>=len(nums):
                return 0
            
            take=0
            not_take=dp(index+1,last)
            if nums[index]>last:
                take=1+dp(index+1,nums[index])


            return max(take,not_take)

        return dp(0,-10001)