#!/usr/bin/env python
# coding: utf-8

# 290. Word Pattern
# 
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# 
#  
# 
# Example 1:
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# 
# 
# Example 2:
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# 

# In[1]:


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        l1=len(s)
        l2=len(pattern)
        if l1!=l2:
            return False
        d={}
        for i in range(l1):
            if pattern[i] not in d:
                if s[i] in d.values():
                    return False
                else:
                    d.update ({pattern[i]:s[i]})
            elif d[pattern[i]]!=s[i]:
                return False
        return True


# In[ ]:




