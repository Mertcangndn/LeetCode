class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for i in s:
            match i:
                case '(' | '[' | '{':
                    stack.append(i)
                case ')' | ']' | '}':
                    last = stack.pop() if stack else 'X'
                    if dic[i] != last:
                        return False
        
        return not stack