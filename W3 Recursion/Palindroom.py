def isPalindroom(s):
    return isPalindromeHelper(s,0,len(s)-1)
def isPalindromeHelper(s,low,high):
    if high<=low:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return isPalindromeHelper(s,low+1,high-1)