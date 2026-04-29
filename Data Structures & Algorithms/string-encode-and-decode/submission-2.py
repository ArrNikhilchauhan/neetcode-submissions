class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "empty"
        return ":;".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="empty":
            return  []
        word=""
        ans=[]
        for i in range(len(s)):
            if s[i] == ":" and s[i+1]==";" :
                ans.append(word)
                word=""
                continue
            elif s[i]==";":
                continue
            word+=s[i]
        
        ans.append(word)
        return ans


