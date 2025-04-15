
def rotate_list(list, shift_by):
    new_list = list.copy()
    for i in range(len(new_list)):
        if (i + shift_by) <= len(new_list) - 1:
            new_index = i + shift_by
        else:
            new_index = (i + shift_by)%len(list)
            
        list[new_index] = new_list[i]
    print(list)

def rotate_list_in_place(list, shift_by):
    border_index = (len(list) - shift_by%len(list)) if shift_by >= len(list) else (len(list) - shift_by)
    list.extend(list[:border_index])
    del list[:border_index]
    return list

print("First function that does rotation while making a new list")
rotate_list([1, 2, 3, 4, 5],2)
rotate_list(["d", 2, "fine", 4, 5],10)

print("Second function that does rotation in place")
print(rotate_list_in_place([1, 2, 3, 4, 5],3))
print(rotate_list_in_place(["d", 2, "fine", 4, 5], 10))