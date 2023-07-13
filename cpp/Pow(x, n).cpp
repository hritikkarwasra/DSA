// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

// Example 1:

// Input: x = 2.00000, n = 10
// Output: 1024.00000
// Example 2:

// Input: x = 2.10000, n = 3
// Output: 9.26100

// Solution

class Solution {
public:
    double myPow(double x, int n) {
        double ans = 1.0;
        if (n ==0) return 1;
        bool flag = false;
        if (n < 0){
            n = abs(n);
            flag = true;  
        } 
        
        while(n>0){
            if(n&1){
                ans = ans * x;
            }
            x = x*x;
            n>>=1;
        }
        if (flag == true) ans = 1/ans;
        return ans;
    }
};
