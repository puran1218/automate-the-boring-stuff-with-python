tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def column_width(table):
    colWidth = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if colWidth[i] < len(table[i][j]):
                colWidth[i] = len(table[i][j])
    return colWidth

def print_table(table, colWidth):
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidth[j]), end=' ')
        print()

col_width = column_width(tableData)
print_table(tableData, col_width)
    