"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces
"""

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        retStr:str = ""
        currStr:str = ""
        for outerIndex in range(0, len(s)):
            for index in range(outerIndex, len(s)):
                currentChar:chr = s[index]
                if currentChar not in currStr:
                    currStr = f"{currStr}{currentChar}"
                else:
                    break
                #print(f"|currentChar: [{currentChar}], currStr: [{currStr}], retStr: [{retStr}]|")
            if len(currStr) > len(retStr):
                retStr = currStr
            currStr = ""
        print(f"retStr: [{retStr}]")
        return len(retStr)

sol:Solution = Solution()
s = "jbpnbwwd"
ans:int = sol.lengthOfLongestSubstring(s)
print(ans)