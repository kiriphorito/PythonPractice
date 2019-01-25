class Sorts:

    def partition(self, alist, start, end):
        pivot = alist[start]
        leftmark = start + 1
        rightmark = end
        while 1:
            while leftmark <= rightmark:
                if alist[leftmark] < pivot:
                    leftmark = leftmark + 1
                else:
                    break
            while leftmark <= rightmark:
                if alist[rightmark] > pivot:
                    rightmark = rightmark - 1
                else:
                    break;
            if rightmark < leftmark:
                break
            else:
                temp = alist[rightmark]
                alist[rightmark] = alist[leftmark]
                alist[leftmark] = temp
        alist[start] = alist[rightmark]
        alist[rightmark] = pivot
        return rightmark

    def quicksort(self, alist, start, end):
        if (start < end):
            split = self.partition(alist, start, end)
            self.quicksort(alist, start, split - 1)
            self.quicksort(alist, split + 1, end)

alist = [9,7,5,3,1]

sort = Sorts()
sort.quicksort(alist, 0, len(alist) - 1)
print(alist)



