class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n=len(nums)
        ans=[]
        for i in range(0,n):
            start=i+1
            end=n-1
            while start<end:
                total=nums[i]+nums[start]+nums[end]

                if total>0:
                    end-=1
                elif total<0:
                    start+=1
                else:
                    temp=[nums[i],nums[start],nums[end]]
                    if temp not in ans:
                        ans.append(temp)
                    start+=1
                    end-=1

        
        return ans
