# Add your clarifying questions here
# Imagine a skyline of buildings and you were standing 
# in front of them at ground level 0. 
# How many of these buildings could you see?

# Given a list [-1, 1, 3, 7, 7, 3] 
# determine which values could be "seen."

# Output: [1,3,7]


def skyline(building_list):
    visible = []
    for i in range(len(building_list)-1):
        if building_list[i] < 0:
            continue
)
        visible.append(building_list[i])

    print(visible)

skyline([-1, 1, 3, 7, 7, 3])
skyline([-1, 1, 3])