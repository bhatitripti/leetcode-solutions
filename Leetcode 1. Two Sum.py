#!/usr/bin/env python
# coding: utf-8

# # 1. Two Sum
# 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
#  
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# In[ ]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=len(nums)
        for i in range(m):
            for j in range(i+1,m):
                if nums[i]+nums[j]==target:
                    return [i,j]


# In[ ]:




