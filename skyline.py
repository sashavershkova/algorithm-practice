# Add your clarifying questions here
# Imagine a skyline of buildings and you were standing 
# in front of them at ground level 0. 
# How many of these buildings could you see?

# Given a list [-1, 1, 3, 7, 7, 3] 
# determine which values could be "seen."

# Output: [1,3,7]

# PSEUDOCODE
# if a number is negative: ignore it
# if a number 

def skyline(building_list):
    visible = []
    for i in range(len(building_list)):
        if building_list[i] < 0:
            continue
        elif building_list[i-1] == building_list[i]:
            break
        
        visible.append(building_list[i])

    return visible

print(skyline([-1, 1, 3, 7, 7, 3]))
print(skyline([-1, 1, 3, 11, 11, 5]))