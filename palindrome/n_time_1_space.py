 def isPalindrome(self, s: str) -> bool:
        regex = re.compile(r'[A-Za-z0-9]')
        n = len(s)
        i = 0
        j = n - 1
        while i < n and j >= 0:
            if regex.fullmatch(s[j]) and regex.fullmatch(s[i]):
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            elif not regex.fullmatch(s[j]) and regex.fullmatch(s[i]): # skip non alphanum char
                j -= 1
            elif regex.fullmatch(s[j]) and not regex.fullmatch(s[i]):
                i += 1
            else:
                # none r alphanumeric
                i += 1
                j -= 1
        return True
