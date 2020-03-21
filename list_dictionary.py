def list2str(row_list):
    output = ''
    for i in range(len(row_list)):
        if i != len(row_list) - 1:
            output += str(row_list[1]) + ', '
        else:
            output += 'and ' + str(row_list[i])

    return output


spam = ['apple', 'banana', 'tofu', 'cat']

print(list2str(spam))
