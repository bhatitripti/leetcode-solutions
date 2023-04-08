#!/usr/bin/env python
# coding: utf-8

# # 9. Palindrome Number
# 
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.
# 
#  
# 
# Example 1:
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# In[ ]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        b=x
        p=0
        while x:
            p=(p*10)+(x%10)
            x//=10
        return b==p
    


# In[ ]:


# Another way 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False 
        a1=str(x)
        b=a1[::-1]
        return a1==b

