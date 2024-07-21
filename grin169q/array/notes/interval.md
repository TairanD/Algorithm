# Interval
Involved Questions: 56, 57, 435

## 1 - Two Techniques in Interval Problems
- Sort: the most common way to sort intervals is to arrange them by their start points
- Drawing Illustrations to Observe Principles (logics)

## 2 - Interval Overlap

## 3 - Interval Merge (Q56)
``` 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
```

## 4 - Interval Intersection