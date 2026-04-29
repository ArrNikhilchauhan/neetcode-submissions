class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq=defaultdict(int)
        for x in nums:
            freq[x]+=1

        sorted_freq=sorted(freq.items(),key=lambda x:x[1])

        ans=[]
        n=len(sorted_freq)

        for i in range(n-1,n-k-1,-1):
            ans.append(sorted_freq[i][0])

        return ans

        