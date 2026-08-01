class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapped={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        results=[]
        if not digits:
            return []

        def combination(index,combo):

            if len(combo)==len(digits):
                results.append("".join(combo.copy()))
                return 
            
            curr=digits[index]
            for x in mapped[curr]:
                combo.append(x)
                combination(index+1,combo)
                combo.pop()

        combination(0,[])
        return results

            
