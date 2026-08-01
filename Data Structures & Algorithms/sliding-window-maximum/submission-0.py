class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        low=0
        high=k
        output=[]
        while high<=len(nums):
            output.append(max(nums[low:high]))
            low+=1
            high+=1

        return  output


