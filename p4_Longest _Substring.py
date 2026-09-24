"""Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring that contains
no repeating characters.

Example:
Input:  "abcabcbb"
Output: 3
Longest substring: "abc"

Input:  "bbbbb"
Output: 1
Longest substring: "b"

Input:  "pwwkew"
Output: 3
Longest substring: "wke"

Approach: Sliding Window + Set

- Use two pointers: left and right.
- `right` expands the window by adding new characters.
- A set is used to keep track of characters currently inside the window.
- If the character at `right` already exists in the set, we have a
  duplicate.
- Move `left` forward and remove characters until the duplicate is removed.
- Add the new character to the set.
- Calculate the current window length using:
      right - left + 1
- Keep track of the maximum length found.
- Also store the longest substring when a new maximum is found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def longest_substring(x):
    character = set()
    left = 0
    max_length = 0
    longest = ""

    for right in range(len(x)):

        while x[right] in character:
            character.remove(x[left])
            left += 1

        character.add(x[right])

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length
            longest = x[left:right + 1]

    print("Length:", max_length)
    print("Longest substring:", longest)


longest_substring("abcabcbb")
longest_substring("bbbbb")
longest_substring("pwwkew")


# Output:
#
# Length: 3
# Longest substring: abc
#
# Length: 1
# Longest substring: b
#
# Length: 3
# Longest substring: wke


# Trace for "abcabcbb":
#
# left = 0, right = 0:
# x[0] = 'a'
# 'a' is not in the set.
# Add 'a'.
# Window = "a"
# Length = 1
#
# left = 0, right = 1:
# x[1] = 'b'
# 'b' is not in the set.
# Add 'b'.
# Window = "ab"
# Length = 2
#
# left = 0, right = 2:
# x[2] = 'c'
# 'c' is not in the set.
# Add 'c'.
# Window = "abc"
# Length = 3
#
# left = 0, right = 3:
# x[3] = 'a'
# 'a' is already in the set.
# Remove x[left] = 'a'.
# Move left to 1.
# Add the new 'a'.
# Window = "bca"
# Length = 3
#
# left = 1, right = 4:
# x[4] = 'b'
# 'b' is already in the set.
# Remove x[left] = 'b'.
# Move left to 2.
# Add the new 'b'.
# Window = "cab"
# Length = 3
#
# The maximum length remains 3.
#
# The longest substring is "abc" (other valid substrings of length 3
# also exist, such as "bca" and "cab").
#
# The important Sliding Window idea:
#
# right -> expands the window
# left  -> shrinks the window when a duplicate is found
# set   -> keeps track of unique characters in the current window
#
# The window always contains unique characters.