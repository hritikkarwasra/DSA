# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generator(self,i,j, n, res, ans):
        if i == j == n :
            ans.append(res)
            return
        if i < n:
            self.generator(i+1, j, n, res + "(", ans)
        if j < i:
            self.generator(i, j+1, n ,res+ ")", ans)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generator(0,0,n, "", ans)
        return ans