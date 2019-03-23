from collections import Counter
def canMakePalindrom(s):
    if len([v for v in Counter(s).values() if v % 2 == 1]) <= 1: 
        return 1
    else:
        return 0
print(canMakePalindrom('aabbe2'))