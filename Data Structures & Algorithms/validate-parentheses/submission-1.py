class Solution:
    def isValid(self, s: str) -> bool:

        valid_set={
            '(':')',
            '{':'}',
            '[':']'
        }
        
        sets=[]
        for char in s:
            if char in valid_set.keys():
                sets.append(char)
            else:
                if len(sets)!=0 and valid_set[sets[-1]]==char:
                    sets.pop()
                else:
                    return False

        return True if len(sets)==0 else False


        