class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if (target - n) in hashmap:
                return [hashmap[target-n], i]
            hashmap[n] = i

"""
Notes:
in - time complexity depends on container
List access time = O(n)
Dictionary/Hash/Set = O(1), O(n) worst time

"""
