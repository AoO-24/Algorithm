import heapq

# Initialize an empty list to represent the max heap
max_heap = []

# Function to push an element onto the max heap
def push_max_heap(heap, item):
    # Push the negative of the item to simulate a max heap
    heapq.heappush(heap, -item)

# Function to pop the maximum element from the max heap
def pop_max_heap(heap):
    # Pop the smallest element (which is the negative of the largest)
    return -heapq.heappop(heap)

# Add elements to the max heap
push_max_heap(max_heap, 10)
push_max_heap(max_heap, 5)
push_max_heap(max_heap, 20)

# Print the max heap (internally stored as negatives)
print("Max heap (negatives):", max_heap)

# Pop the maximum element
max_element = pop_max_heap(max_heap)
print("Maximum element:", max_element)

# Print the max heap after popping
print("Max heap after popping:", max_heap)