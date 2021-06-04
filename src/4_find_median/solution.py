# -*- coding: utf-8 -*-
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

 示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

 示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

 示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

 示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

 示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

 提示：
 nums1.length == m
 nums2.length == n
 0 <= m <= 1000
 0 <= n <= 1000
 1 <= m + n <= 2000
 -106 <= nums1[i], nums2[i] <= 106

 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
 Related Topics 数组 二分查找 分治算法
"""
import heapq


class Solution(object):
    """
    小顶堆，堆顶最小
    """
    @staticmethod
    def find_median_sorted_arrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        if len(nums) < 1:
            raise Exception("Invalid Input")

        if len(nums) == 1:
            return float(nums[0])

        if len(nums) % 2 == 1:
            length = (len(nums) + 1) // 2
        else:
            length = (len(nums)) // 2 + 1

        h = nums[:length]
        heapq.heapify(h)
        for i in nums[length:]:
            if i > h[0]:
                heapq.heapreplace(h, i)

        if len(nums) % 2 == 1:
            return float(h[0])
        else:
            return float((heapq.heappop(h) + heapq.heappop(h)) / 2)

    @staticmethod
    def find_median_sorted_arrays_2(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index1, index2 = 0, 0

        tmp = []
        for i in range((len(nums1) + len(nums2)) // 2 + 1):
            if index1 == len(nums1):
                tmp.append(nums2[index2])
                index2 += 1
            elif index2 == len(nums2):
                tmp.append(nums1[index1])
                index1 += 1
            else:
                if nums1[index1] < nums2[index2]:
                    tmp.append(nums1[index1])
                    index1 += 1
                else:
                    tmp.append(nums2[index2])
                    index2 += 1
            i += 1

        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(tmp[-1])
        else:
            return float(tmp[-1] + tmp[-2]) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = Solution.find_median_sorted_arrays(nums1, nums2)
    assert result == float(2.5)

    nums1 = [1, 5]
    nums2 = [3, 4, 7]
    result2 = Solution.find_median_sorted_arrays_2(nums1, nums2)
    print(result2)
    assert result2 == float(4)
