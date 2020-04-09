# Approach

## Intuition

## Algorithm

First off, for each soldier with index ![](http://latex.codecogs.com/gif.latex?j), we can count the number of vaild soldier with index ![](http://latex.codecogs.com/gif.latex?i<j) where `rating[i] < rating[j]` and `rating[i] > rating[j]` respectively.

``` py
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
```

## Complexity Analysis

* Time Complexity ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n^2))
* Space Complexity ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n))
