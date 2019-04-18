# 1.1.) Implement an algorithm to determine if a string has all unique
#       characters. What if you cannot use additional data structures?

# Clarifying Questions:
#   - What set of characters does the input string contain?

def isUnique(str):
    charList = []   # list containing all unique characters of str

    for c in str:   # loop through each character of str
        # if c is not found in str
        if c in charList:
            return False
        else:
            charList.append(c)

    return True

print(isUnique("Marisa"))
print(isUnique("abcdefg"))

# Analysis of Solution:
# Space Complexity:
# Time Complexity:
