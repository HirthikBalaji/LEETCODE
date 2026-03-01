import bisect
class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n

        lastRain = {}      # lake -> last rain day
        dryDays = []       # sorted list of indices where rains[i] == 0

        for i, lake in enumerate(rains):
            if lake > 0:
                # Flood risk
                if lake in lastRain:
                    # Find a dry day after last rain
                    idx = bisect.bisect_right(dryDays, lastRain[lake])
                    if idx == len(dryDays):
                        return []  # impossible
                    dry_day = dryDays[idx]
                    ans[dry_day] = lake
                    dryDays.pop(idx)

                lastRain[lake] = i
                ans[i] = -1
            else:
                dryDays.append(i)
                ans[i] = 1  # placeholder

        return ans