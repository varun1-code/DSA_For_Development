"""Valid Anagram

Given two strings, determine whether one is an anagram of the other
(same characters, same counts, order doesn't matter).

Example:
    Input:  s1 = "listen", s2 = "silent"
    Output: True

    Input:  s1 = "hello", s2 = "world"
    Output: False

Includes:
1. Two-dict solution (one frequency count per string, then compare)
2. One-dict optimized solution (increment for s1, decrement for s2)

Both start with an O(1) early exit: two strings can only be anagrams
if they have the same length, so there's no point doing any O(n) work
otherwise.
"""


def is_anagram_two_dict(s1, s2):
    """Time: O(n), Space: O(n) - two separate frequency dicts."""
    if len(s1) != len(s2):
        return False

    dict1 = {}
    dict2 = {}

    for ch in s1:
        dict1[ch] = dict1.get(ch, 0) + 1

    for ch in s2:
        dict2[ch] = dict2.get(ch, 0) + 1

    return dict1 == dict2


def is_anagram_one_dict(s1, s2):
    """Time: O(n), Space: O(n) - single frequency dict, roughly half
    the space of the two-dict version.
    """
    if len(s1) != len(s2):
        return False

    counts = {}

    for ch in s1:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in s2:
        counts[ch] = counts.get(ch, 0) - 1

    return all(count == 0 for count in counts.values())


print(is_anagram_two_dict("listen", "silent"))  # True
print(is_anagram_two_dict("hello", "world"))    # False

print(is_anagram_one_dict("listen", "silent"))  # True
print(is_anagram_one_dict("hello", "world"))    # False

# Output:
# True
# False
# True
# False

# Trace for is_anagram_one_dict("listen", "silent"):
# After s1 ("listen"): counts = {l:1, i:1, s:1, t:1, e:1, n:1}
# After s2 ("silent") decrements each: every key goes back to 0
#   counts = {l:0, i:0, s:0, t:0, e:0, n:0}
# all(count == 0) -> True
#
# If a character appears a different number of times in s1 vs s2, its
# count won't return to 0, so all(...) correctly returns False.
