# def LongestSubstring(s):
#     char_set = set()
#     left = 0
#     max_len = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# print(LongestSubstring("abcabcbb"))

import re

def is_valid_username(username):
    # Rule 3: Length check
    if len(username) < 6 or len(username) > 20:
        return False

    # Rule 1, 2, 5: Pattern must start with a lowercase letter,
    # end with letter or digit, and contain only valid characters
    if not re.match(r'^[a-z][a-z0-9._]*[a-z0-9]$', username):
        return False

    # Rule 4: No consecutive special characters
    if re.search(r'[._]{2,}', username):
        return False

    return True

print(is_valid_username("john_doe"))        # ✅ True
print(is_valid_username("john..doe"))       # ❌ False
print(is_valid_username("john_doe."))       # ❌ False
print(is_valid_username("jo"))              # ❌ False
print(is_valid_username("john__doe"))       # ❌ False
print(is_valid_username("john.doe_123"))    # ✅ True
print(is_valid_username("1john"))           # ❌ False
