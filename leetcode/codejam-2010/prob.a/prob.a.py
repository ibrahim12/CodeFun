import itertools

input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')

T = int(input_lines[0])

input_index = 1

for case in xrange(T):

    n = int(input_lines[input_index])
    input_index += 1

    points = []
    for line in xrange(n):
        points.append(map(int, input_lines[input_index + line].split()))
    input_index += n

    # points.sort(cmp=lambda x, y: x[0] - y[0])
    #
    # print points

    c = 0
    for i in xrange(n):
        for j in xrange(0, i):
            c += (points[i][0] > points[j][0]) != (points[i][1] > points[j][1])
            print 'i', i, 'j', j , points[i][0], ' > ' , points[j][0], '!=', points[i][1] , '> ',  points[j][1], 'c', c

    value = c
    output_lines.append('Case #%s: %s' % (case+1, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)

