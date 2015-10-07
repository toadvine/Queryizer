__author__ = 'benjamin_sanchez'


def get_list(i):
    query_hold = list()
    f = open(i, 'r')
    for line in f:
        line = line.translate('\n')
        query_hold.append(line)
    return query_hold


def make_query(i):
    temp_answer = [int(x.rstrip('\n')) for x in i]
    hold_answer = ""
    for x in temp_answer:
        if temp_answer.index(x) == len(temp_answer) - 1:
            hold_answer += str(x)
        else:
            hold_answer += str(x)
            hold_answer += ", "
    answer = "SELECT * FROM /**put in your table here**/ WHERE /**put variable there**/ in (" + hold_answer + ")"
    return answer


def write_out(i):
    return i


def main():
    f = get_list('inputList.txt')
    a = make_query(f)
    write_out(a)
    print(a)

main()
