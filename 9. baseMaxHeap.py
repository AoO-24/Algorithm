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
# Heapify在MaxHeap构建中的使用
# 1. 先将List用for loop全部取负数 neglist = [-num for num in list]。
# 2. 再用heapq.heapify(neglist) 将负值列表转换为堆。
# 3. 在取最大值时，max_element = -heapq.heappop(neglist)
# 创建一个列表
numbers = [7, 2, 5, 3, 8, 4]

# 将列表中的元素取负值
neg_numbers = [-num for num in numbers]

# 将负值列表转换为堆
heapq.heapify(neg_numbers)

# 打印堆化后的最大堆（内部存储为负值）
print("堆化后的最大堆（负值）:", neg_numbers)

# 弹出最大元素
max_element = -heapq.heappop(neg_numbers)
print("最大元素:", max_element)

# 打印弹出后的最大堆
print("弹出最大元素后的堆（负值）:", neg_numbers)