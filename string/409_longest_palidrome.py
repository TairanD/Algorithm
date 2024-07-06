class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dic = {}
        for char in s:
            if char not in char_dic:
                char_dic[char] = 1
            else:
                char_dic[char] += 1

        palindrome_length = 0
        hasOdd = False
        for char, count in char_dic.items():
            if count % 2 != 0:
                hasOdd = True
                palindrome_length += count - 1
            else:
                palindrome_length += count

        return palindrome_length + 1 if hasOdd else palindrome_length