"""Reverse Words in a String

Given a string containing words separated by spaces, reverse the order
of the words.

Leading, trailing, and multiple spaces should be handled so that the
result contains exactly one space between words.

Example:
Input:  "the sky is blue"
Output: "blue is sky the"

Input:  "  hello   world  "
Output: "world hello"

Approach: Split + Reverse + Join

- Use `split()` to separate the string into individual words.
- Use `reverse()` to reverse the order of the words.
- Use `join()` to combine the words back into a string.
- `split()` without an argument automatically handles multiple spaces
  and removes leading/trailing spaces.

Time Complexity: O(n)
Space Complexity: O(n)
"""

s = "the sky is blue"

# Separate the string into words
x = s.split()

# Reverse the order of the words
x.reverse()

# Join the words using a single space
result = " ".join(x)

print(result)


# Output:
#
# blue is sky the


# Trace:
#
# Input:
# "the sky is blue"
#
# Step 1: split()
# ['the', 'sky', 'is', 'blue']
#
# Step 2: reverse()
# ['blue', 'is', 'sky', 'the']
#
# Step 3: join()
# "blue is sky the"
#
# Important concepts:
#
# split()  -> converts a string into a list of words.
# reverse() -> reverses the existing list in-place and returns None.
# join()   -> combines list elements into a single string.
