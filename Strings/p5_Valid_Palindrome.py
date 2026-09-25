"""Valid Palindrome

Given a string, determine whether it is a palindrome after:
- Converting uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

Example:
Input:  "A man, a plan, a canal: Panama"
Output: True

Input:  "race a car"
Output: False

Input:  " "
Output: True

Approach: String Cleaning + Two Pointers

- Convert the string to lowercase.
- Remove all non-alphanumeric characters using `isalnum()`.
- Use two pointers:
      left  -> starts from the beginning
      right -> starts from the end
- Compare the characters at both pointers.
- If they match, move both pointers toward the center.
- If they do not match, the string is not a palindrome.
- If all characters match, the string is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_palindrome(x):
    # Convert the string to lowercase
    x = x.lower()

    # Remove non-alphanumeric characters
    result = ""

    for ch in x:
        if ch.isalnum():
            result += ch

    # Two-pointer approach
    left = 0
    right = len(result) - 1

    is_palindrome_result = True

    while left < right:
        if result[left] == result[right]:
            left += 1
            right -= 1
        else:
            is_palindrome_result = False
            break

    if is_palindrome_result:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")


is_palindrome("A man, a plan, a canal: Panama")
is_palindrome("race a car")
is_palindrome(" ")


# Output:
#
# Given string is a palindrome
# Given string is not a palindrome
# Given string is a palindrome


# Trace for "A man, a plan, a canal: Panama":
#
# Step 1: Convert to lowercase
# "A man, a plan, a canal: Panama"
# becomes:
# "a man, a plan, a canal: panama"
#
# Step 2: Remove non-alphanumeric characters
# "amanaplanacanalpanama"
#
# Step 3: Use two pointers
#
# left = 0, right = 20:
# result[0]  = 'a'
# result[20] = 'a'
# They match.
# Move left forward and right backward.
#
# left = 1, right = 19:
# result[1]  = 'm'
# result[19] = 'm'
# They match.
#
# Continue comparing characters from both ends.
#
# Every corresponding pair matches, so the string is a palindrome.
#
# Important ideas:
#
# isalnum() -> checks whether a character is a letter or number.
# left      -> moves from left to right.
# right     -> moves from right to left.
# break     -> stops the loop immediately when a mismatch is found.
#