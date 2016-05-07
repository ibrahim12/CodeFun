import itertools

input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')

def gen_all(s):
    output = []
    indexes = []

    for i in xrange(len(s)):
        if s[i] == '?':
            indexes.append(i)

    output.append(list(s))

    # print output

    while len(indexes):
        p = indexes.pop()
        n_outputs = []
        for a_output in output:
            a_output[p] = str(0)
            for i in xrange(1, 10):
                value = a_output[:]
                value[p] = str(i)
                n_outputs.append(value)

        for i in n_outputs:
            output.append(i)

    final_output = []
    for i in output:
        final_output.append(''.join(i))

    return final_output

case = 0
for a_input in input_lines[1:]:
    case += 1

    c, j = a_input.split(' ')

    nC = len(c)
    nJ = len(j)

    aC = gen_all(c)
    aJ = gen_all(j)

    diffs = {}
    for i in aC:
        for j in aJ:
            a_min = abs(int(i)-int(j))
            if a_min not in diffs:
                diffs[a_min] = []

            diffs[a_min].append( (i, j) )

    sorted_keys = sorted(diffs)

    v = sorted_keys[0]

    arr = diffs[v]
    arr = sorted(arr, cmp=lambda x,y: int(x[1]) - int(y[1]) if int(x[0]) == int(y[0]) else int(x[0]) - int(y[0]) )
    value = str(arr[0][0]) + ' ' + str(arr[0][1])
    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)

