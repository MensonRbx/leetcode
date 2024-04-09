class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Time taken equivalent to number of operations
        count = 0
        while True:
            count += 1
            tickets[0] -= 1            
            if k == 0:
                if tickets[k] == 0:
                    return count
                k = len(tickets) - 1
            else:
                k -= 1
            if tickets[0] == 0:
                tickets.pop(0)
            else:
                tickets.append(tickets.pop(0))

# Runtime: 49ms (>44%)
# Memory: 16.61 (>16%)
