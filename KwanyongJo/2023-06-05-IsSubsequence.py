# Given two strings s and t,
# return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        for letter in t :
            # index = t.index(i)
            # print(index)

            if i == len(s):
                return True

            if s[i] == letter:
                i = i + 1

        return i == len(s)



if __name__ == '__main__':
    solution = Solution()
    s = 'aabc'
    t = 'aeabece'

    solution.isSubsequence(s,t)