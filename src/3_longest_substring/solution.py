# -*- coding: utf-8 -*-
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

 示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

 示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

 示例 4:
输入: s = ""
输出: 0

 提示：

 0 <= s.length <= 5 * 104
 s 由英文字母、数字、符号和空格组成

 Related Topics 哈希表 双指针 字符串 Sliding Window
 """


class Solution(object):

    @staticmethod
    def longest_substring(s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        substring = ""
        for i in s:
            if i not in substring:
                substring += i
            else:
                length = len(substring) if len(substring) > length else length
                substring = (substring.split(i)[1] or "") + i

        if len(substring) > length:
            return len(substring)
        return length


if __name__ == '__main__':
    s = "abcabcbb"
    result = Solution().longest_substring(s)
    print("length:", result)
    assert result == 3
