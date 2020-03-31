def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key


def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q+1, r)
        merge(lst, p, q, r)

def merge(lst, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q
    L = []
    R = []
    for i in range(0, n_1):
        L.append(lst[p + i])
    for j in range(0, n_2):
        R.append( lst[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i,j = 0,0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
