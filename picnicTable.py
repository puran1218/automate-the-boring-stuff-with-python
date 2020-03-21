def printPicnicTable(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.'), str(v).rjust(rightWidth))

itemsDict = {
    'sandwiches': 4, 'apples': 2, 'cups': 4, 'cookies': 16
}

printPicnicTable(itemsDict, 9, 10)