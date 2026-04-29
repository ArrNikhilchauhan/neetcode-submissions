class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        start=0
        end=len(s)-1

        while start<end:
            # if s[start]
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue

            if s[start]!=s[end]:
                print(s[start],s[end])
                return False
            
            print(s[start],start,s[end],end)
            start+=1
            end-=1

        return True