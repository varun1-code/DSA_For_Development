"""Palindrome Check

Given a string, determine whether it reads the same forwards and
backwards.

Example:
    Input:  "abcba"
    Output: Palindromic

    Input:  "hello"
    Output: Not Palindromic

Approach: Two pointers
- i starts at the beginning, j starts at the end.
- Compare x[i] and x[j]; if they differ, it's not a palindrome.
- If they match, move both pointers toward the center.
- while i < j (not <=) is enough: a middle character never needs to
  be compared with itself.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def palindrome(x):
    i = 0
    j = len(x) - 1

    while i < j:
        if x[i] != x[j]:
            print("Not Palindromic")
            return

        i += 1
        j -= 1

    print("Palindromic")


palindrome("abcba")
palindrome("hello")

# Output:
# Palindromic
# Not Palindromic

# Trace for "abcba":
# i=0, j=4: x[0]='a' == x[4]='a' -> match, i=1, j=3
# i=1, j=3: x[1]='b' == x[3]='b' -> match, i=2, j=2
# i=2, j=2: loop condition i < j is False -> exit loop -> Palindromic
#
# The middle character ('c') never needs comparing against itself,
# which is why "i < j" is the correct condition instead of "i <= j".
