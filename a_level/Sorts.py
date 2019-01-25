def bsort(b):
    # Loop through all passes
    for j in range(0, len(b)):
        print("Pass" , j)
        swap = False

        # Comparison for a pass
        for i in range(0, len(b) - 1 - j):
            print("Comparison" , i)
            if b[i] > b[i+1]:
                # Swap
                temp = b[i]
                b[i] = b[i + 1]
                b[i + 1] = temp
                # Set says that something has swapped
                swap = True

        # Check is any swaps has happened in the end of the this pass
        if swap is False:
            # No swaps = sorted therefore end
            return b
    return b

a = [5,1,7,6]
a = bsort(a)
print(a)