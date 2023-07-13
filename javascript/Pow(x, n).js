// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

// Example 1:

// Input: x = 2.00000, n = 10
// Output: 1024.00000
// Example 2:

// Input: x = 2.10000, n = 3
// Output: 9.26100

// Solution

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    function helper(x, n){
        if(n == 0) return 1
        if(x == 0) return 0

        const half = helper(x, Math.floor(n/2))

        if (n%2==1){
            return half * half * x
        }
        else{
            return half * half
        }
    }

    let result = helper(x,Math.abs(n))

    return result = n>0 ? result : 1/result
};

