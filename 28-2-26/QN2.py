class Solution:
    def maxBottlesDrunk(self,numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        need = numExchange
        drunk = 0

        while full > 0:
            # Drink all full bottles
            drunk += full
            empty += full
            full = 0

            # Try to exchange
            if empty >= need:
                empty -= need
                full += 1
                need += 1
            else:
                break

        return drunk
        