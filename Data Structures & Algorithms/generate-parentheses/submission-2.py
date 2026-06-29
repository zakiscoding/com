class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_count, close_count):
            if len(stack)==n*2:
                res.append(''.join(stack))
                return
            if open_count<n:
                stack.append('(')
                backtrack(open_count+1, close_count)
                stack.pop()
            if open_count > close_count:
                stack.append(')')
                backtrack(open_count, close_count+1)
                stack.pop()

        backtrack(0,0)
        return res

