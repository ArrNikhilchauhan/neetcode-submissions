from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq=defaultdict(int)

        for x in tasks:
            freq[x]+=1

        pair=[]

        for x in freq.keys():
            heapq.heappush(pair,(-freq[x],x))
        
        cycles=0
        index=1

        while pair:
            count,value = heapq.heappop(pair)
            count=-count
            print(index,count)
            cycles=max(cycles,index+(count-1)*(n+1))
            index+=1

        return max(cycles,len(tasks))
