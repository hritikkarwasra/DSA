# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# {
#     2: 'abc',
#     3: 'def',
#     4: 'ghi',
#     5: 'jkl',
#     6: 'mno',
#     7: 'pqrs',
#     8: 'tuv',
#     9: 'wxyz'
# }
 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]


class Solution:
    def generator(self, digit, char, to_process, ans, res):
        if len(res) == len(to_process):
            print(res)
            ans.append(res)
            return 

        for letter in to_process[digit]:
            digit+=1
            self.generator(digit, char, to_process, ans, res+ letter)
            digit-=1

        # if digit < len(to_process) and char < len(to_process[digit]):
        #     res += to_process[digit][char]
        #     digit +=1
        #     self.generator(digit, char, to_process, ans, res)

        #     digit-=1
        #     char+=1
        #     res = res[:-1]
        #     self.generator(digit, char, to_process, ans, res)
        #     char -=1



    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        to_process = [letters[int(digit)] for digit in digits]
        print(to_process)
        ans = []
        if len(digits)>0:
            self.generator(0,0,to_process, ans, "")

        return ans