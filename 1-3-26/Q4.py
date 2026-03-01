import bisect
import math

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for s in spells:
            # Minimum potion strength needed
            need = math.ceil(success / s)

            # Find first potion >= need
            idx = bisect.bisect_left(potions, need)

            result.append(m - idx)

        return result