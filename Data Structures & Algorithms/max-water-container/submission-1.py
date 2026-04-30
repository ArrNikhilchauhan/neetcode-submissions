class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        
        ans=0
        while low<high:
            area=min(heights[low],heights[high])*(high-low)
            ans=max(area,ans)
            if heights[low]<=heights[high]:
                low+=1
            else:
                high-=1

        
        return  ans
