import random
import time
l = [random.randint(-50,50) for _ in range(6000)]
#l = [7,4,1,3]
l2 = l.copy()

def bubblesort(l):
    for i in range(len(l)-1):
        flag = True
        for j in range(len(l) - i -1):
            if l[j] > l[j+1]:
                flag = False
                l[j], l[j+1] = l[j+1], l[j]
        if flag:
            break
    return l

def selectionsort(l):
    for r in range(1, len(l)):
        min_idx = r-1
        for i in range(r, len(l)):
            if l[min_idx] > l[i]:
                min_idx = i
        l[r-1], l[min_idx] = l[min_idx], l[r-1]
    return l

def insertionsort(l):
    t0 = time.time()
    for r in range(1, len(l)):
        key = l[r]
        i = r - 1
        while i >=0 and l[i] > key:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key
    print(time.time()-t0)
    return l

def shellsort(l):
    t0 = time.time()
    def _insertion(s, g):
        for r in range(s+g, len(l), g):
            key = l[r]
            i = r - g
            while i >= s and l[i] > key:
                l[i+g] = l[i]
                i -= g
            l[i+g] = key

    g = len(l)
    while 1:
        g //= 2
        if g % 2 == 0:
            g += 1
        for s in range(g):
            _insertion(s, g)
        if g == 1:
            break
    print(time.time()-t0)
    return l

def mergesort(l):
    t0 = time.time()
    def _merge(s, m, e):
        temp = []
        i, j = s, m+1
        while i <= m or j <= e:
            if j > e:
                temp.append(l[i])
                i += 1
            elif i > m:
                temp.append(l[j])
                j += 1
            elif l[j] < l[i]:
                temp.append(l[j])
                j += 1
            else:
                temp.append(l[i])
                i += 1
            
        l[s:e+1] = temp

    def _mergesort(s, e):

        if s == e:
            return
        
        m = (s+e)//2
        _mergesort(s, m)
        _mergesort(m+1, e)
        _merge(s, m, e)

    _mergesort(0, len(l)-1)
    print(time.time()-t0)
    return l

def quicksort(l):
    t0 = time.time()
    def _quicksort(s, e):
        
        if e-s < 2:
            return
        
        pivot = l[s]
        i = s+1
        j = e-1

        while 1:
            while i <= j and l[i] <= pivot:
                i += 1
            while i <= j and l[j] > pivot:
                j -= 1
            if j < i :
                break
            else:
                l[i], l[j] = l[j], l[i]
        l[s], l[j] = l[j], l[s]
        _quicksort(s, j)
        _quicksort(j+1, e)
    
    _quicksort(0, len(l))
    print(time.time()-t0)
    return l

def heapsort(l):

    t0 = time.time()
    def heapify(l):
        for i in range(len(l)):
            while i > 0:
                p = (i-1)//2
                if l[p] >= l[i]:
                    break
                l[i], l[p] = l[p], l[i]
                i = p
    
    def heappop(l, e):
        p, c = 0, 1
        l[p], l[e] = l[e], l[p]
        while c < e:
            if c + 1 < e and l[c] < l[c+1]:
                c += 1
            if l[p] < l[c]:
                l[c], l[p] = l[p], l[c]
                p, c = c, 2*c + 1
            else:
                break

    heapify(l)
    for e in range(len(l))[::-1]:
        heappop(l, e)
    print(time.time()-t0)
    return l

l_sorted = heapsort(l)
print(l_sorted == sorted(l2))