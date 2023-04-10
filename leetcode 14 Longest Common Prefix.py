#!/usr/bin/env python
# coding: utf-8

# # 14. Longest Common Prefix
# 
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
#  
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#     
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# In[ ]:


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=len(strs)
        if m==0:
            return ""
        elif m==1:
            return strs[0]
        strs.sort()
        e=min(len(strs[0]),len(strs[m-1]))
        i=0
        while i<e and strs[0][i]==strs[m-1][i]:
            i+=1
        pre=strs[0][0:i]
        return pre

