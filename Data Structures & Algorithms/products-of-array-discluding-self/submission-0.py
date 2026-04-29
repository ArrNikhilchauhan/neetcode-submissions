class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)

        left_product=[]
        right_product=[]

        product=1
        for x in nums:
            left_product.append(product)
            product*=x

        product=1
        for i in range(n-1,-1,-1):
            right_product.append(product)
            product*=nums[i]
        
        right_product=right_product[::-1]
        
        ans=[]
        for i in range(n):
            ans.append(left_product[i]*right_product[i])

        return ans

            


        