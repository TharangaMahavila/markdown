def sort_array(array):
    if array and len(array) > 1:
        center = len(array) // 2
        sorted_array = []
        if center > 1:
            sort_array(array[:center])
            sort_array(array[center:])
        else:
            if array[0] > array[1]:
                sorted_array.append(array[1])
                sorted_array.append(array[0])
        return sorted_array
    elif len(array) == 1:
        return array
    else:
        return "Input is not valid"

data1 = [1]
data2 = [2,1]

print(sort_array(data1))
print(sort_array(data2))
