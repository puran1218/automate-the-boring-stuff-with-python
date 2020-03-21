import re

def strip_charactor(charactor, strip_char = ''):
    if strip_char == '':
        return charactor.strip()
    else:
        charactor = charactor.strip()
        charactorRegex = re.compile(strip_char)
        return charactorRegex.sub('', charactor)

charactor = input("Please input the full charactor: ")
strip_char = input("Please input the charactor you want to striped: ")

strip_charactor = strip_charactor(charactor, strip_char)
print(strip_charactor)