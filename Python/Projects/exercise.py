from unittest import result


def sortRoman(names):
    data  = {}
    result = []
    n = len(names)
    for i in range(n):
        name_roman = names[i].split()
        name = name_roman[0]
        if name in data:
            data[name].append(names[i])
        else:
            data[name] = [names[i]]

    for name in sorted(data.keys()):
        result.extend(sorted(data[name]))

    return result

print(sortRoman(['Louis IX', 'Louis VIII']))






