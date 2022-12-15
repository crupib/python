class Solution(object):
    def isPalindrome(self, s) :
        
        new_str = ''
        
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        return new_str == new_str[::-1]
def main():
   s = "A man, a plan, a canal: Panama"
   sol = Solution()
   print(sol.isPalindrome(s))
   s = "race a car"
   sol = Solution()
   print(sol.isPalindrome(s))
   s = " "
   sol = Solution()
   print(sol.isPalindrome(s))
   

if __name__ == "__main__":
    main()
