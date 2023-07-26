// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

// Example 1:

// Input: n = 3
// Output: ["((()))","(()())","(())()","()(())","()()()"]
// Example 2:

// Input: n = 1
// Output: ["()"]

class Solution {
public:
    vector<string> generator (int i, int j, int n, vector<string> & ans, string &res){
        if (i ==j == n) {
            return ans.push_back(res);
        }
        if (i < n){
            res.push_back('(');
            generator(i+1, j, n, ans, res);
        }
        if (j<i){
            res.push_back(')');
            generator(i, j+1, n, ans, res);
        } 
    }
    vector<string> generateParenthesis(int n) {
        int i, j;
        vector<string> ans, res;
        string s;

        res = generator(i, j, n, ans, s);
        return res;
    }
};