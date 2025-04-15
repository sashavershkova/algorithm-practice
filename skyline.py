# Add your clarifying questions here
# Imagine a skyline of buildings and you were standing 
# in front of them at ground level 0. 
# How many of these buildings could you see?

# Given a list [-1, 1, 3, 7, 7, 3] 
# determine which values could be "seen."

# Output: [1,3,7]


def my_max(iterable):
    max_value = 0
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value


def skyline(building_list):
    visible = []
    for i in range(len(building_list)):
        # if a number is negative: ignore it
        if building_list[i] < 0:
            continue
        # if a number is equal or smaller that maximum of previous numbers we already iterated through: ignore it (bc we can't see it)
        elif building_list[i] <= my_max(building_list[0:i]):
            continue
        # otherwise add to the visible list
        visible.append(building_list[i])

    return visible

print(skyline([-1, 1, 3, 7, 7, 3]))
print(skyline([-1, 1, 3, 11, 11, 5]))
print(skyline([-1, 3, 4, 5, 5, 5, 2, 7, 3, 11])) # we need to get 3, 4, 5, 7, 11