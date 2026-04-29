class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n==0:
            return 0

        ans=0
        count=1
        for i in range(1,n):
            if nums[i]-nums[i-1]==1:
                count+=1
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                ans=max(count,ans)
                count=1

        
        ans=max(ans,count)

        return ans