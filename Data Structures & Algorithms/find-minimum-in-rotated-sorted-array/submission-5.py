class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        low=0
        high=len(nums)-1

        while low<=high:

            mid=(low+high)//2

            if nums[low]<=nums[mid]<=nums[high]:
                return nums[low]
            
            elif mid!=0 and mid!= len(nums)-1 and nums[mid-1]>nums[mid]<nums[mid+1]:
                return nums[mid]
            
            elif nums[low]<=nums[mid]:
                low=mid+1
            
            else:
                high=mid


                
