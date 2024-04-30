def largest_element_in_array(arr):
    max = 0

    for el in arr:
        if max > el:
            pass
        elif max < el:
            max = el

#    arr.sort()

    print(max)

largest_element_in_array([1000,400, 55,54,110])