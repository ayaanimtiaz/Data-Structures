from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # okay we're gonna us ecounters
        # variable sized sliding window
        # smallest substring of s that has every char in t
        # have a required and a have variable
        # required = len(t)
        # have = how many variables match the necessary amount that t has
        # if required  = have 
        # subtract one if the newly removed variable doesnt match
        # obviously replace min length etc, save the left and right pointers add one for window length
        # what was the while thing claude told me at

        if len(t) > len(s):
            return ''

        t_counter = Counter(t)
        s_counter = Counter()
        t_unique = set(t)
        required = len(t_unique)
        have = 0
        matches = 0
        min_length = float("inf")
        left = 0        
        r_saved = len(s)
        l_saved = 0

        for right in range(len(s)):
            s_counter[s[right]] += 1
            if s_counter[s[right]] == t_counter[s[right]]:
                have += 1
            while have == required:
                matches += 1
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    r_saved = right
                    l_saved = left
                s_counter[s[left]] -= 1
                if t_counter[s[left]] != 0 and s_counter[s[left]] < t_counter[s[left]]:
                    have -= 1
                left += 1

        if matches == 0:
            return ''
        return s[l_saved:r_saved+1]



