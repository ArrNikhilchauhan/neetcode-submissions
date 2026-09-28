class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    curr_set = set()
    left = 0
    ans = 0

    for right in range(len(s)):
      # If the current character is a duplicate, shrink the window from the left
      while s[right] in curr_set:
        curr_set.remove(s[left])
        left += 1

      # Add the new character and update the maximum length
      curr_set.add(s[right])
      ans = max(ans, right - left + 1)

    return ans