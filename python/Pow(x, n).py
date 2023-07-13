# // Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# // Example 1:

# // Input: x = 2.00000, n = 10
# // Output: 1024.00000
# // Example 2:

# // Input: x = 2.10000, n = 3
# // Output: 9.26100

# // Solution


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        flag = False
        if n == 0:
            return 1
        if n < 1:
            flag = True
            n = n*-1
        while(n>1):
            if n % 2 ==1:
                ans =  ans * x
        
            x = x * x
            n = n//2
        x *= ans 
        if flag:
            x = 1/x
        return x 
                