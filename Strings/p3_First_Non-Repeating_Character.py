"""First Non-Repeating Character

Given a string, find the first character that appears only once.

Example:
Input:  "swiss"
Output: "w"

```
Input:  "aabbcdd"
Output: "c"

Input:  "aabb"
Output: None
```

Approach:

1. Use a dictionary to count the frequency of every character.
2. Traverse the dictionary in insertion order.
3. The first character with frequency 1 is the first
   non-repeating character.
4. If no character has frequency 1, return None.

Python dictionaries preserve insertion order, so traversing
freq.items() maintains the original character order.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def first_non_repeating(x):
"""Time: O(n), Space: O(n) - frequency dictionary."""


freq = {}

# Count the frequency of every character
for ch in x:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find the first character with frequency 1
for key, value in freq.items():
    if value == 1:
        return key

# No non-repeating character found
return None


print(first_non_repeating("swiss"))      # w
print(first_non_repeating("aabbcdd"))    # c
print(first_non_repeating("aabb"))       # None

# Output:

# w

# c

# None

# Trace for first_non_repeating("swiss"):

#

# After counting:

# freq = {

# 's': 3,

# 'w': 1,

# 'i': 1

# }

#

# Traverse the dictionary:

# 's' -> 3 -> not unique

# 'w' -> 1 -> first non-repeating character

#

# Therefore:

# return 'w'

#

# For "aabb":

# freq = {

# 'a': 2,

# 'b': 2

# }

#

# No character has frequency 1.

# Therefore:

# return None

#

# The function uses return instead of print so that the result

# can be reused by other code.



