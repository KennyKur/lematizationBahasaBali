lineList = [line.rstrip('\n') for line in open('non_filter.txt')]
print(lineList)
print(len(lineList))

result = sorted(list(set(lineList)))

print(result)
print(len(result))


with open('BaliVocab.txt', 'w') as f:
    for i in result:
        f.write("%s\n" % i)

