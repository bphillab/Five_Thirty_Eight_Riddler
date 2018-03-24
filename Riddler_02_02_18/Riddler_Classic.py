from math import sqrt
import numpy as np
import copy
import matplotlib.pylab as plt

grasshopper_distance = 1.0
filename = 'grasshopper'+str(int(grasshopper_distance*100))
gif_flag = 0

# -------------------------------------------------------------------------
# parameters --------------------------------------------------------------
# -------------------------------------------------------------------------

# pixels
pixel_length = 0.01

# yard
yard_area = 1
yard_length = round(sqrt(yard_area) / pixel_length)
yard_pixels = round(yard_area/pixel_length**2)

# space (from which yard is sampled)
space_length = 2
length_pixels = round(space_length/pixel_length)
space_pixels = length_pixels**2

# grasshopper
grasshopper_pixels = round(grasshopper_distance/pixel_length)

# -------------------------------------------------------------------------
# calculation matrices ----------------------------------------------------
# -------------------------------------------------------------------------

# yard_matrix (1 if yard, 0 if not yard)
yard_matrix = np.zeros([space_length/pixel_length,space_length/pixel_length])

# neighbor_matrix (number of yard_matrix 1's that are grasshopper_distance
# away
neighbor_matrix = np.zeros([space_length/pixel_length,space_length/pixel_length])

# grasshopper_matrix (matrix containing 1's that are grasshopper_distance
# from center)
grasshopper_checker = [np.zeros(2)]
for i in range(-grasshopper_pixels, grasshopper_pixels+1):
    for j in range(-grasshopper_pixels, grasshopper_pixels+1):
        distance_from_center = sqrt(i**2 + j**2)
        if round(distance_from_center) == grasshopper_pixels:
            grasshopper_checker = grasshopper_checker+ [np.array([i, j])]


# select a number (yard_pixels) of random points in the space
offset = round((length_pixels - yard_length) / 2)
for i in range(yard_length):
    for j in range(yard_length):
        yard_matrix[i + offset][ j + offset] = 1

# calculate initial neighbor_matrix
for i in range(length_pixels):
    for j in range(length_pixels):
        for k in range(len(grasshopper_checker)):
            delta_x = grasshopper_checker[k][0]
            delta_y = grasshopper_checker[k][1]
            if (i + delta_x) >= 0 and (i + delta_x) < length_pixels and (j + delta_y) >= 0 and (j + delta_y) < length_pixels:
                if yard_matrix[i + delta_x][ j + delta_y] == 1:
                    neighbor_matrix[i][ j] = neighbor_matrix[i][j] + 1

old_yard_matrix = np.zeros([len(yard_matrix),len(yard_matrix)])
counter = 0
graph_counter = 0
tries_in_a_row = 0
while (counter==0 or (tries_in_a_row<3 and counter<3000)):
    counter = counter+1
    old_yard_matrix = copy.deepcopy(yard_matrix)
    condition = (yard_matrix == 1)
    l = np.extract(condition,range(len(yard_matrix)*len(yard_matrix)))
    yard_table = [(divmod(i,len(yard_matrix))[0],divmod(i,len(yard_matrix))[1]) for i in l]
    neighbor_value = np.zeros([len(yard_table), 1])
    for i in range(len(yard_table)):
        neighbor_value[i] = neighbor_matrix[yard_table[i][0]][ yard_table[i][1]]

    p = min(neighbor_value)
    condition = (neighbor_value == p)
    min_array = np.extract(condition,range(len(neighbor_value)))
    q = min_array[np.random.choice(range(len(min_array)), 1)]

    yard_to_remove = yard_table[q]
    yard_matrix[yard_to_remove[0]][yard_to_remove[1]] = 0

    for k in range(len(grasshopper_checker)):
        delta_x = grasshopper_checker[k][ 0]
        delta_y = grasshopper_checker[k][ 1]
        if (yard_to_remove[0] + delta_x) >= 0 and (yard_to_remove[0] + delta_x) < length_pixels and (yard_to_remove[1] + delta_y) >= 0 and (yard_to_remove[1] + delta_y) < length_pixels:
            neighbor_matrix[yard_to_remove[0] + delta_x][ yard_to_remove[1] + delta_y] = neighbor_matrix[yard_to_remove[0] + delta_x][ yard_to_remove[1] + delta_y] - 1
    condition = (yard_matrix == 0)

    l = np.extract(condition, range(len(yard_matrix)*len(yard_matrix)))
    yard_table = [(divmod(i,len(yard_matrix))[0],divmod(i,len(yard_matrix))[1]) for i in l]
    neighbor_value = np.zeros([len(yard_table), 1])
    for i in range(len(yard_table)):
        neighbor_value[i] = neighbor_matrix[yard_table[i][0]][ yard_table[i][1]]

    p = max(neighbor_value)
    condition = (neighbor_value == p)
    max_array = np.extract(condition, range(len(neighbor_value)))
    q = max_array[np.random.choice(range(len(max_array)), 1)]

    yard_to_add = yard_table[q]
    yard_matrix[yard_to_add[0]][ yard_to_add[1]] = 1

    for k in range(len(grasshopper_checker)):
        delta_x = grasshopper_checker[k][0]
        delta_y = grasshopper_checker[k] [1]
        if (yard_to_add[0] + delta_x) >= 0 and (yard_to_add[0] + delta_x) < length_pixels and(yard_to_add[1] + delta_y) >= 0 and (yard_to_add[1] + delta_y) < length_pixels:
            neighbor_matrix[yard_to_add[0] + delta_x][ yard_to_add[1] + delta_y] = neighbor_matrix[yard_to_add[0] + delta_x][ yard_to_add[1] + delta_y] + 1
        if yard_to_add == yard_to_remove:
            tries_in_a_row = tries_in_a_row + 1
        if yard_to_add != yard_to_remove:
            tries_in_a_row = 0

plt.matshow(yard_matrix)
plt.show()
plt.savefig(filename)

