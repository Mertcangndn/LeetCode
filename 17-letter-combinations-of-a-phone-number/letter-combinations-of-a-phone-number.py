class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        result = []

        dic = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, curr_path):
            if index == len(digits):
                result.append(curr_path)
                return
            
            for letter in dic[digits[index]]:
                backtrack(index+1, curr_path+letter)

        backtrack(0,"")

        return result