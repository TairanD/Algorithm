from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


"""
将元素加入新列表比操作原有列表简单，主要是因为以下几个原因：

1. **避免频繁的删除操作**：
    - 在原有列表中频繁地删除元素会导致复杂度增加。删除操作会导致后续元素的移动，这在列表较大时会非常低效。
    - 使用新列表时，只需顺序地添加元素，不会涉及删除操作，从而提高了代码的效率和简洁性。

2. **逻辑更清晰**：
    - 当直接操作原有列表时，需要小心处理索引的变化和元素的移除，容易导致逻辑混乱和错误。
    - 使用新列表时，可以将每一个步骤（处理不重叠区间、合并重叠区间、处理剩余区间）独立进行，使代码逻辑更加清晰和直观。

3. **边界条件处理更简单**：
    - 在原有列表中操作时，处理边界条件往往需要额外的判断和临时变量来跟踪状态，增加了代码的复杂性。
    - 使用新列表时，每个步骤都是独立的，边界条件处理可以通过简单的条件判断完成，减少了额外的状态跟踪。

### 具体分析：

**第一种方法的问题**：
- 在原有列表中直接操作，每次删除元素后，索引和列表长度都会变化，需要额外的逻辑来处理这些变化。
- 代码中使用了多个嵌套的条件判断和索引操作，逻辑复杂且容易出错。
- 边界条件处理繁琐，需要额外的变量和状态跟踪。

**第二种方法的优点**：
- 使用一个新的结果列表，每一步都将合适的元素添加到结果列表中，避免了对原有列表的频繁操作。
- 逻辑分为三个独立的步骤，每个步骤处理一种情况（不重叠的区间、重叠的区间、剩余的区间），清晰明了。
- 边界条件通过简单的条件判断来处理，无需额外的状态跟踪，代码简洁易读。

### 总结：

将元素加入新列表而不是操作原有列表，可以避免不必要的复杂操作，使代码逻辑更加清晰，处理边界条件更简单，提升代码的可读性和维护性。这种方法更符合编程中的“分而治之”的思想，有助于写出简洁高效的代码。
"""