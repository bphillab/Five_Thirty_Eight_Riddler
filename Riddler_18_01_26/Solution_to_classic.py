'''
From Josh Streeter, graph theory meets ancient Greece in a puzzle that takes two classic mathematical ideas and mashes
them together:

The famous four-color theorem states, essentially, that you can color in the regions of any map using at most four
colors in such a way that no neighboring regions share a color. A computer-based proof of the theorem was offered in
1976.

Some 2,200 years earlier, the legendary Greek mathematician Archimedes described something called an Ostomachion. It’s a
group of pieces, similar to tangrams, that divides a 12-by-12 square into 14 regions. The object is to rearrange the
pieces into interesting shapes, such as a Tyrannosaurus rex. It’s often called the oldest known mathematical puzzle.

Your challenge today: Color in the regions of the Ostomachion square with four colors such that each color shades an
equal area. (That is, each color needs to shade 36 square units.)

'''

def checker(config):
    connections = {1:[2,5],
                         2:[3,1],
                         3:[2,4],
                         4:[3,5,7],
                         5:[6,1,4,13],
                         6:[5,7,8],
                         7:[4,6],
                         8:[6,9,13,11],
                         9:[10,11,8],
                         10:[9,11],
                         11:[12,14,9,10,8],
                         12:[11,14],
                         13:[5,8,14],
                         14:[11,12,13]
                         }
    areas = {1:8,
             2:1,
             3:3,
             4:2,
             5:4,
             6:2,
             7:4,
             8:7,
             9:1,
             10:2,
             11:4,
             12:4,
             13:2,
             14:4}


    color_areas = {'R':0,'G':0,'B':0,'Y':0}
    for i in areas.keys():
        color_areas[config[i-1]] += areas[i]

    if color_areas['R']!=color_areas['G']:
        return False
    if color_areas['R']!=color_areas['B']:
        return False
    if color_areas['R']!=color_areas['Y']:
        return False

    for i in connections.keys():
        for j in connections[i]:
            if config[i-1] == config[j-1]:
                return False
    return True

config = []
possible_colors = ['R','G','B','Y']
counter = 0
for i1 in possible_colors:
    for i2 in possible_colors:
        for i3 in possible_colors:
            for i4 in possible_colors:
                for i5 in possible_colors:
                    for i6 in possible_colors:
                        for i7 in possible_colors:
                            for i8 in possible_colors:
                                for i9 in possible_colors:
                                    for i10 in possible_colors:
                                        for i11 in ['R']:
                                            for i12 in ['B']:
                                                for i13 in possible_colors:
                                                    for i14 in ['G']:
                                                        if checker(
                                            [i1,i2,i3,i4,i5,i6,i7,i8,
                                             i9,i10,i11,i12,i13,i14]):
                                                            counter = counter+1