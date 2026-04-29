class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset=set(nums)
        longest=0

        for x in nums:
            if (x-1) not in numset:
                count=1
                while (x+1) in numset:
                    count+=1
                    x+=1
                longest=max(count,longest)

        return longest
        