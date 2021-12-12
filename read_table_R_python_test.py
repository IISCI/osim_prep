# read.table R python test
from csv import reader
import numpy as np
import itertools


def read_csv(csv_file):
    
    file = open(csv_file)
    csv_content = file.readlines()
    csv_header = csv_content[:19]
    csv_data = csv_content[19:]
    file.close()
    # pos_source = reader(csv_data, quotechar="")
    data_source = list(csv_data)
    # pos_source_transposed = pos_source.T
    print('csv header: ', csv_header)
    # print('csv data: ',pos_source)

    for idx, line in enumerate(data_source):
        data_source[idx] = [float(i) for i in line.split('\t')]
    return data_source


test_csv_file = './data/jump_jo_3/gait_reduced_nonscaled-scaled_BodyKinematics_pos_global.sto'

pos_source = read_csv(test_csv_file)

print('\n\n1:::', pos_source[0], '\n\n2:::',
      pos_source[1], '\n\n3:::', pos_source[2])

print('\n\n...')

print('\n\nend::', pos_source[len(pos_source)-1])

# for line in pos_source_transposed:
#     line = list(line.split('\t'))
#     for item in line:
#         print(float(str(item)))
#     i = 0
#     break
