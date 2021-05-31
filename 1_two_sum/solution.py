# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]

"""


class Solution(object):

    def two_sum(self, nums: list, target: int) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, v in enumerate(nums):
            if (target - v) in nums and nums.index(target - v) != i:
                return [i, nums.index(target - v)]
        return []

    def two_sum1(self, nums: list, target: int) -> list:
        tmp = dict()
        for i, v in enumerate(nums):
            if tmp.get(target-v) is not None:
                return [i, tmp.get(target-v)]
            tmp[v] = i


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 11
    result = Solution().two_sum(nums, target)
    print(result)
    assert result == [2, 3]

    result1 = Solution().two_sum1(nums, target)
    print(result1)
    assert result1 == [2, 3]

