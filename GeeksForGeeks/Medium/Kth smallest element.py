import heapq

# Approach 1/2 - Intuitive
def kthSmallest(self, arr, n, k):
    arr.sort()
    return arr[k-1]

# Approach 2/2 - Priority Queue
def kthSmallest(arr, k):
    min_heap = []
    for i in arr:
        heapq.heappush(min_heap, i)
        if (len(min_heap) > k):
            heapq.heappop(min_heap)
    return min_heap[0]
