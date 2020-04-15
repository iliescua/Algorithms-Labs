def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)

def heap_extract_max(A):
    if (len(A) < 1):
        raise ValueError("Heap underflow")
    biggest = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    max_heapify(A, 0)
    return biggest

def max_heap_insert(A, key):
    A.append(float('-inf'))
    heap_increase_key(A, len(A)-1, key)

def heapsort(A):
    build_max_heap(A)
    sortedList = []
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        sortedList.insert(0, A.pop())
        max_heapify(A, 0)
    for data in sortedList:
        A.append(data)

def heap_increase_key(A, i, key):
    if (key < A[i]):
        raise ValueError("New key is smaller than current key")
    A[i] = key
    while (i > 0 and A[_parent(i)] < A[i]):
        A[i], A[_parent(i)] = A[_parent(i)], A[i]
        i = _parent(i)

def max_heapify(A, i):
    l = _left(i)
    r = _right(i)
    largest = i
    if (l < len(A) and A[l] > A[largest]):
        largest = l
    if (r < len(A) and A[r] > A[largest]):
        largest = r
    if (largest != i):
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest) 


def _left(i):
    return 2*i + 1
def _right(i):
    return 2*i + 2
def _parent(i):
    return i // 2
  