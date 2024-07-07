class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return
        res = strs[0]
        for strs_index in range(1, len(strs)):
            cur_str = strs[strs_index]
            for i in range(len(res)):
                if i >= len(cur_str):
                    res = res[:i]
                    break
                if cur_str[i] != res[i]:
                    res = res[:i]
                    break
        return res
print(Solution().longestCommonPrefix(["ab","a"]))