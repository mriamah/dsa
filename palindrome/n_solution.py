def isPalindrome(self, s: str) -> bool:
        alpha_s = re.findall(r'[A-Za-z0-9]', s)
        n = len(alpha_s)
        for i in range(n):
            if alpha_s[i].lower() != alpha_s[n-1-i].lower():
                return False
            
        return True
