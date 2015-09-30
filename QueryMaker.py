__author__ = 'benjamin_sanchez'


def getList(i):
    query_hold = list()
    f = open(i, 'r')
    for line in f:
        line = line.translate('\n')
        query_hold.append(line)
    return query_hold


def makeQuery(i):
    answer = [int(x.rstrip('\n')) for x in i]
    
    return answer


def writeOut(i):


def main():
    f = getList('inputList.txt')
    a = makeQuery(f)
    print (a)
    #writeOut(a)

main()
