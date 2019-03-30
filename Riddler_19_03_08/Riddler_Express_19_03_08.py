import copy
def count_num_inst(num_dict, counted):
    count = 0
    for key in num_dict.keys():
        if num_dict[key] == counted and key < str(counted):
            count = count + 1
    return count


def test_instance(num_dict):
    temp_word = sorted(''.join([i*num_dict[i] for i in num_dict.keys()]))
    test_word = ''
    for i in num_dict.keys():
        if num_dict[i] > 0:
            test_word = test_word+str(num_dict[i])+i
    return sorted(test_word) == temp_word


temp_dict = {}
count_working = 0
examps = []

for i0 in range(2):
    temp_dict['0'] = i0
    for i1 in range(count_num_inst(temp_dict,1),10):
        temp_dict['1'] = i1
        for i2 in range(count_num_inst(temp_dict, 2), 7):
            temp_dict['2'] = i2
            for i3 in range(count_num_inst(temp_dict, 3), 6):
                temp_dict['3'] = i3
                for i4 in range(count_num_inst(temp_dict, 4), 5):
                    temp_dict['4'] = i4
                    for i5 in range(count_num_inst(temp_dict, 5), 4):
                        temp_dict['5'] = i5
                        for i6 in range(count_num_inst(temp_dict, 6), 4):
                            temp_dict['6'] = i6
                            for i7 in range(count_num_inst(temp_dict, 7), 4):
                                temp_dict['7'] = i7
                                for i8 in range(count_num_inst(temp_dict, 8), 4):
                                    temp_dict['8'] = i8
                                    for i9 in range(count_num_inst(temp_dict, 9), 3):
                                        temp_dict['9'] = i9
                                        if test_instance(temp_dict):
                                            count_working = count_working + 1
                                            examps = examps + [copy.deepcopy(temp_dict)]
print(count_working)
print(examps)