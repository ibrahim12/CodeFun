
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')
T = int(input_lines[0])

case_start_index = 0
line_index = 1

import itertools

for case in xrange(T):

    n = int(input_lines[line_index])
    line_index += 1

    inputs = map(int, input_lines[line_index].split(' '))
    line_index += 1

    bff = {}
    r_bff = {}
    for index in xrange(n):
        bff[index] = inputs[index]-1
        if inputs[index] not in r_bff:
            r_bff[inputs[index]] =[]

        r_bff[inputs[index]].append( index+1 )

    r = 0
    p = []
    for pattern in itertools.permutations(xrange(n)):
        first = pattern[0]
        second = pattern[1]

        for i in xrange(1, n):
            prev = pattern[i-1]
            cur = pattern[i]

            if ((bff[cur] == first or bff[cur] == prev) and
                    (bff[first] == cur or bff[first] == second)):

                if r < (i+1):
                    r = i+1
                    p = pattern

            if bff[cur] != prev and ( i == n-1 or bff[cur] != pattern[i+1]):
                break

    print [_+1 for _  in p]
    value = r
    output_lines.append('Case #%s: %s' % (case+1, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)