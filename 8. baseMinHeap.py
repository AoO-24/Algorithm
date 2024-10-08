import heapq

# Initialize an empty list to represent the min heap
min_heap = []

# Function to push an element onto the min heap
def push_min_heap(heap, item):
    heapq.heappush(heap, item)

# Function to pop the minimum element from the min heap
def pop_min_heap(heap):
    return heapq.heappop(heap)

# Add elements to the min heap
push_min_heap(min_heap, 10)
push_min_heap(min_heap, 5)
push_min_heap(min_heap, 20)

# Print the min heap
print("Min heap:", min_heap)

# Pop the minimum element
min_element = pop_min_heap(min_heap)
print("Minimum element:", min_element)

# Print the min heap after popping
print("Min heap after popping:", min_heap)