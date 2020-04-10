class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        increasing = []
        for j in range(n):
            count = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    count += 1
            increasing.append(count)
        decreasing = []
        for j in range(n):
            count = 0
            for i in range(j):
                if rating[i] > rating[j]:
                    count += 1
            decreasing.append(count)
        result = 0
        for k in range(n):
            for j in range(k):
                if rating[j] < rating[k]:
                    result += increasing[j]
                if rating[j] > rating[k]:
                    result += decreasing[j]
        return result