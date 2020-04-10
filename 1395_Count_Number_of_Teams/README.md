# Approach: Preprocessing

## Intuition

If we first calculate the possible teams with `rating[i] < rating[j]` or `rating[i] > rating[j]`, we can count the number of teams under given conditions more efficiently.

## Algorithm

First off, for each soldier with index ![](http://latex.codecogs.com/gif.latex?j), we can count the number of soldiers with index ![](http://latex.codecogs.com/gif.latex?i<j) and denote `increasing[j]` and `decreasing[j]` where `rating[i] < rating[j]` and `rating[i] > rating[j]` respectively.

Then, for each soldier with index ![](http://latex.codecogs.com/gif.latex?k), we compare to soldier with index ![](http://latex.codecogs.com/gif.latex?j<k). If `rating[j] < rating[k]`, we have `increasing[j]` possible teams under given conditions, which means `rating[i] < rating[j] < rating[k]` where `0 <= i < j < k < n`; otherwise, there are `decreasing[j]` possible teams satisfied `rating[i] > rating[j] > rating[k]` since all elements in array `rating` are distinct.

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

* Time Complexity ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n^2)), where ![](http://latex.codecogs.com/gif.latex?n) is the length of array `rating`

Time complexity of calculation of `increasing` and `decreasing` is ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n^2)), respectively. The accumulation of `result` takes ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n^2)) time. Total time complaxity is ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n^2)).

* Space Complexity ![](http://latex.codecogs.com/gif.latex?\\mathcal{O}(n))

We use two array `increasing` and `decreasing` with length ![](http://latex.codecogs.com/gif.latex?n).
