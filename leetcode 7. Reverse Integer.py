7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
  
Example 2:

Input: x = -123
Output: -321
  
  Solution:
    
    
    class Solution:
      def reverse(self, x: int) -> int:
         neg=False
         if x<0:
            neg=True
            x=-x
         p=0
         while x:
            p=p*10+(x%10)
            x//=10
         if p>=2**31-1 or p<= -2**31:
            return 0
         return -p if neg else p
