# Specify filename to read the input from
filename = 'qs_numbers.txt'

# Build a list of ints from the file
with open(filename, "r") as f:
	lines_list = [int(line) for line in f]

def swap(first, second):
    temp = first
    first = second
    second = temp
    return first, second

# Question 1

QS_PIVOT_FIRST_COUNTER = 0

def partition_first(array, left_ptr, right_ptr):
    # Use the first element
    pivot = array[left_ptr]
    i = left_ptr + 1
    for j in range(left_ptr + 1, right_ptr):
        # Only swap with the ith element,
        #  if jth element is less than pivot
        if array[j] < pivot:
            array[j], array[i] = swap(array[j], array[i])
            i += 1

    # Swap the the pivot with the ith location
    array[left_ptr], array[i-1] = swap(array[left_ptr], array[i-1])
    return i - 1



def quick_sort_first(array, left_index, right_index):
    global QS_PIVOT_FIRST_COUNTER
    if left_index < right_index:

        pivot_index = partition_first(array, left_index, right_index)
        # Add the length of the subarray in this recursive call to
        # global counter
        QS_PIVOT_FIRST_COUNTER += (right_index - left_index - 1)

        quick_sort_first(array, left_index, pivot_index)

        quick_sort_first(array, pivot_index + 1, right_index)


# quick_sort_first(lines_list, 0, len(lines_list))
# print QS_PIVOT_FIRST_COUNTER


# Question 2 

QS_PIVOT_LAST_COUNTER = 0

def partition_last(array, left_ptr, right_ptr):
    # Use the first element
    pivot = array[right_ptr-1]

    array[right_ptr-1] = array[left_ptr]
    array[left_ptr] = pivot

    # Same as before
    i = left_ptr + 1
    for j in range(left_ptr + 1, right_ptr):
        # Only swap with the ith element,
        #  if jth element is less than pivot
        if array[j] < pivot:
            array[j], array[i] = swap(array[j], array[i])
            i += 1

    # Swap the the pivot with the ith location
    array[left_ptr], array[i-1] = swap(array[left_ptr], array[i-1])
    return i - 1



def quick_sort_last(array, left_index, right_index):
    global QS_PIVOT_LAST_COUNTER
    if left_index < right_index:

        pivot_index = partition_last(array, left_index, right_index)
        # Add the length of the subarray in this recursive call to
        # global counter
        QS_PIVOT_LAST_COUNTER += (right_index - left_index - 1)

        quick_sort_last(array, left_index, pivot_index)

        quick_sort_last(array, pivot_index + 1, right_index)



# quick_sort_last(lines_list, 0, len(lines_list))
# print QS_PIVOT_LAST_COUNTER

# Question 3

QS_PIVOT_MEDIAN_COUNTER = 0

def middle_value(a, b, c):
    if (a <= b and b <= c) or (c <= b  and b <= a):
        return b

    elif (b <= a and a <= c) or (c <= a  and a <= b):
        return a

    else:
        return c


def partition_median(array, left_ptr, right_ptr):
    left = array[left_ptr]
    right = array[right_ptr -1]
    len = right_ptr - left_ptr
    if len % 2 == 0:
        middle = array[left_ptr + len/2 - 1]
    else:
        middle = array[left_ptr + len/2]

    pivot_item = middle_value(left, right, middle)

    pivot_index = array.index(pivot_item)

    array[pivot_index] = array[left_ptr]
    array[left_ptr] = pivot_item

    i = left_ptr + 1
    for j in range(left_ptr + 1, right_ptr):
        if array[j] < pivot_item:
            array[j], array[i] = swap(array[j], array[i])
            i += 1

    # Swap the the pivot with the ith location
    array[left_ptr], array[i-1] = swap(array[left_ptr], array[i-1])
    return i - 1


def quick_sort_median(array, left_index, right_index):
    global QS_PIVOT_MEDIAN_COUNTER
    if left_index < right_index:

        pivot_index = partition_median(array, left_index, right_index)
        # Add the length of the subarray in this recursive call to
        # global counter
        QS_PIVOT_MEDIAN_COUNTER += (right_index - left_index - 1)

        quick_sort_median(array, left_index, pivot_index)

        quick_sort_median(array, pivot_index + 1, right_index)


# quick_sort_median(lines_list, 0, len(lines_list))
# print QS_PIVOT_MEDIAN_COUNTER