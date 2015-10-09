# this program sort the data with multi index
# use the python 3.5 as default

"""

if a struct has many elements, this sort agorithm can sort the struct depends on
many elements and with different order.

example:

    [(1,4,6), (2,80,67), (23,5,45)]

    with this kind of the data, I here choose the quick sort method for reasons:

        1)  with less swap operation
        2)  with less code

"""
def isswap(data, index_1, index_2, count, sort_mode, sort_type, sort_count):
    "judge to swap the data"
    # do not swap the data
    if count == sort_count:
        return 0
    # get new index
    in_de_crease = sort_mode[count]
    sort_data_index = sort_type[count]-1
    if data[index_1][sort_data_index] > data[index_2][sort_data_index] and in_de_crease:
        return 1
    elif data[index_1][sort_data_index] < data[index_2][sort_data_index] and not in_de_crease:
        return 1
    elif data[index_1][sort_data_index] == data[index_2][sort_data_index]:
        return isswap(data, index_1, index_2, count+1, sort_mode, sort_type, sort_count)
    else:
        return 0

def partition(data, low, high, sort_mode, sort_type, sort_count):
    "part the data"
    part = low
    pivot = high
    for index in range(low, high):
        if(isswap(data, index, pivot, 0, sort_mode, sort_type, sort_count)):
            data[index], data[part] = data[part], data[index]
            part += 1
    data[pivot], data[part] = data[part], data[pivot]
    return part

def quicksort(data, low, high, sort_mode, sort_type, sort_count):
    "quick sort"
    if low < high:
        part = partition(data, low, high, sort_mode, sort_type, sort_count)
        quicksort(data, low, part-1, sort_mode, sort_type, sort_count)
        quicksort(data, part+1, high, sort_mode, sort_type, sort_count)

def sort(data, size, sort_mode, sort_type, sort_count):
    "sort the multi index data"
    quicksort(data, 0, size-1, sort_mode, sort_type, sort_count)

def main():
    "test the main function"
    data = [(1,2,4),
            (12,5,7),
            (5,23,12),
            (2,33,14),
            (4,9,12),
            (12,46,90)]
    sort_mode = (1,0)
    sort_type = (1,3)
    sort_count = 2

    print("The data: ", data)

    sort(data, len(data), sort_mode, sort_type, sort_count)

    print("After sort: ", data)

    input("\n\nPress Enter to exit.\n")

if __name__ == '__main__':
    main()
