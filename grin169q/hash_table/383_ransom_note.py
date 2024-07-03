class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = {}
        for char in ransomNote:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in magazine:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    char_count.pop(char)
        return not char_count