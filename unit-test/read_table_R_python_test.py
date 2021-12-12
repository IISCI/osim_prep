# read.table R python test


def read_csv(csv_file, skip=18):

    file = open(csv_file)
    csv_content = file.readlines()
    file.close()
    # csv_full_header = csv_content[:skip+1]
    csv_header = [str(i).rstrip()
                  for i in csv_content[skip:skip+1][0].split('\t')]
    # csv_header[-1] = csv_header[-1].rstrip()
    csv_data = csv_content[skip+1:]

    # pos_source = reader(csv_data, quotechar="")
    data_source = list(csv_data)

    for idx, line in enumerate(data_source):
        # split values with \t (tab) symbol
        data_source[idx] = [float(i) for i in line.split('\t')]

    # Transpose data table
    data_source = list(map(list, zip(*data_source)))

    # To dict key = column name, value = data frame by frame
    data_dict = dict(zip(csv_header, data_source))

    return data_dict


test_csv_file = './data/jump_jo_3/gait_reduced_nonscaled-scaled_BodyKinematics_pos_global.sto'

pos_source = read_csv(test_csv_file)

for k in pos_source:
    print(k, '::', pos_source[k], '\n\n')

print((pos_source['time']))  # time column data
print(len((pos_source['time'])))  # number of frames


# print('\n\n1:::', pos_source[0], '\n\n2:::',
#       pos_source[1], '\n\n3:::', pos_source[2])

# print('\n\n...')

# print('\n\nend::', pos_source[len(pos_source)-1])

# for line in pos_source_transposed:
#     line = list(line.split('\t'))
#     for item in line:
#         print(float(str(item)))
#     i = 0
#     break
