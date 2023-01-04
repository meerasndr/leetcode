def isPalindrome(s: str) -> bool:
    l = ''
    rev = ''
    for char in s.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz0123456789':
            l += char
    for i in range(len(s)-1, -1, -1):
        if s[i].lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            rev += s[i].lower()
    return rev == l


print(isPalindrome("anna"))
print(isPalindrome("A man, a plan, a canal: Panama"))