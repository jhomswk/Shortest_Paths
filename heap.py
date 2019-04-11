class Heap_Item:
    """
    Heap item data structure.
    """

    def __init__(self, k, v):
        """
        Generates a heap item with key k and value v.
        """
        self.key = k
        self.value = v


    def __repr__(self):
        """
        Represents a heap item.
        """
        return "({},{})".format(self.key, self.value)



class Min_Heap:
    """
    Min-Heap data structure.
    """

    def __init__(self):
        """
        Generates an empty min-heap.
        """
        self.heap = []
        self.index = {}


    def key(self, v):
        """
        Returns the key of the heap element with value v.
        """
        return self.heap[self.index[v]].key


    def left(self, i):
        """
        Returns the i-th item's left child index.
        """
        return 2*i+1


    def right(self, i):
        """
        Returns the i-th item's right child index.
        """
        return 2*(i+1)


    def parent(self, i):
        """
        Returns the i-th item's parent index.
        """
        return (i-1)//2


    def min_heapify(self, i):
        """
        Restores the min-heap property on the i-th item, assuming
        that its left and right sub-heaps are correct min-heaps.
        """
        l = self.left(i)
        r = self.right(i)
        min = i

        if l < len(self) and self.heap[l].key < self.heap[min].key:
            min = l
        if r < len(self) and self.heap[r].key < self.heap[min].key:
            min = r

        if min != i:
            self.swap(i, min)
            self.min_heapify(min)


    def extract_min(self):
        """
        Extracts the pair (key, value) containing the smallest key
        from the heap.
        """
        if not self:
            return None
        self.swap(0, len(self)-1)
        min = self.heap.pop()
        del self.index[min.value]
        self.min_heapify(0)
        return (min.key, min.value)


    def insert(self, k, v):
        """
        Inserts the pair (k, v) into the heap.
        """
        self.heap.append(Heap_Item(k,v))
        self.index[v] = len(self)-1
        self.decrease_key(v,k)


    def decrease_key(self, v, k):
        """
        Decreases the key of the heap element containing value
        v to k.
        """
        # NOTE: assumes that value v is present in the heap 
        # NOTE: assumes that the key of the element holding
        #       value v is >= k.
        i = self.index[v]
        item = self.heap[i]
        item.key = k

        p = self.parent(i)
        while i > 0 and k < self.heap[p].key:
            self.heap[i] = self.heap[p]
            self.index[self.heap[p].value] = i
            i, p = p, self.parent(p)

        self.heap[i] = item
        self.index[item.value] = i


    def swap(self, i, j):
        """
        Swaps the i-th and j-th items in the heap.
        """
        self.index[self.heap[i].value], self.index[self.heap[j].value] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def __len__(self):
        """
        Returns the number of items in the heap.
        """
        return len(self.heap)


    def __bool__(self):
        """
        Returns True if the heap is not empty, and False otherwise.
        """
        return len(self.heap) > 0


    def __contains__(self, v):
        """
        Checks whether value v is present in the heap.
        """
        return v in self.index

