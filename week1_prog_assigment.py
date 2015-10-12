# Specify filename to read the input from
filename = 'numbers.txt'

# Build a list of ints from the file
with open(filename) as f:
    lines_list = f.read().splitlines()


# Implement merge count inversion algorithm
def merge_and_count(left, right):
    result = []
    i, j = 0, 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if int(left[i]) < int(right[j]):
            result.append(left[i])
            i += 1
        elif int(right[j]) < int(left[i]):
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count


def sort_and_count(array):
    if len(array) < 2:
        return array, 0
    middle = len(array) / 2
    left, inv_left_count = sort_and_count(array[:middle])
    right, inv_right_count = sort_and_count(array[middle:])
    merged_list, merge_inv_count = merge_and_count(left, right)
    merge_inv_count += (inv_left_count + inv_right_count)
    return merged_list, merge_inv_count

result_list, total_inv_count = sort_and_count(lines_list)

print total_inv_count