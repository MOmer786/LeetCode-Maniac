class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_val=str(x)
        rev_str=str_val[::-1]
        if str_val[0]=='-':
            return False
        elif rev_str==str_val:
            return True
        else: 
            return False