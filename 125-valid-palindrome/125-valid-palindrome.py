class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','').lower()
        
        first = 0
        last = len(s)-1
        
        while first <= last:
            f = s[first]
            l = s[last]
            
            if f.isalnum() and l.isalnum():
                if f == l:
                    first += 1
                    last -= 1
                else:
                    return False
            else:
                if f.isalnum():
                    last -= 1
                else:
                    first += 1
        
        return True