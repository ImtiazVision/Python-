def find_max_in_bitonic_array(arr):
    start = 0
    end = len(arr) - 1
    print('initial end is:',end)
    #start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        print('middle number is: ' , mid)
        if arr[mid] > arr[mid + 1]:
            print('array middle pointer is:', arr[mid])
            end = mid
            print('end number is:',end)
        else:
            start = mid + 1
            print('start is :', start)

    # at the end of the while loop, 'start == end'
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 5, 6, 4, 2]))
    # print(find_max_in_bitonic_array([3, 8, 3, 1]))
    # print(find_max_in_bitonic_array([1, 3, 8, 12]))
    # print(find_max_in_bitonic_array([10, 9, 8]))


main()
