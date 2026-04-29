from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        groups=defaultdict(list)

        for x in strs:
            key="".join(sorted(x))
            groups[key].append(x)     

        return list(groups.values())