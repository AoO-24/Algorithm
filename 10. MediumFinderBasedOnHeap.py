import heapq
class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num) -> None:
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self) -> int:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)



# Assuming the MedianFinder class is implemented as described
median_finder = MedianFinder()

# Test Case 1: Adding a single element
median_finder.addNum(1)
print("Median after adding 1:", median_finder.findMedian())  # Expected: 1.0

# Test Case 2: Adding another element
median_finder.addNum(2)
print("Median after adding 2:", median_finder.findMedian())  # Expected: 1.5

# Test Case 3: Adding a third element
median_finder.addNum(3)
print("Median after adding 3:", median_finder.findMedian())  # Expected: 2.0

# Test Case 4: Adding more elements
median_finder.addNum(4)
median_finder.addNum(5)
print("Median after adding 4 and 5:", median_finder.findMedian())  # Expected: 3.0

# Test Case 5: Adding elements in a different order
median_finder.addNum(10)
median_finder.addNum(6)
print("Median after adding 10 and 6:", median_finder.findMedian())  # Expected: 4.0

# Test Case 6: Adding duplicate elements
median_finder.addNum(5)
print("Median after adding another 5:", median_finder.findMedian())  # Expected: 5.0