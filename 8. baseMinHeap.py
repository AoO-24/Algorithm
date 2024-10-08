import heapq

# Initial list of numbers
numbers = [7, 2, 5, 3, 8, 4]

# Convert the list into a heap : heapify
heapq.heapify(numbers)

# Print the heapified list :
print("Heapified list:", numbers)

# Pop the smallest element : heappop
smallest = heapq.heappop(numbers)
print("Smallest element:", smallest)

# Print the heap after popping the smallest element
print("Heap after popping:", numbers)