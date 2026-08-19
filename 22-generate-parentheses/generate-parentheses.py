class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recFunc(localPath="", left=0, right=0):
            # Base case
            if len(localPath) == n*2:
                result.append(localPath)
                return
            
            if left < n:
                recFunc(localPath + "(", left + 1, right)
            
            if left > right:
                recFunc(localPath + ")", left, right + 1)

        recFunc()

        return result