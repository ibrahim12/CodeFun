


def check_valid(grid):

    n = len(grid[0])

    #row
    for i in xrange(n):
        last_row = grid[i][0]
        last_col = grid[0][i]
        for index in xrange(1, n):
            if grid[i][index] > last_row:
                return False

            last_row = grid[i][index]

            if grid[index][i] > last_col:
                return False

            last_col = grid[index][i]


    return True





input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')
T = int(input_lines[0])

case_start_index = 0
line_index = 1

for case in xrange(T):
    N = int(input_lines[line_index])
    line_index += 1

    grid = [0] * 2501

    rows = []
    for index in xrange(2*N-1):
        rows.append( map(int, input_lines[line_index].split(' ')) )
        line_index += 1

    for r in rows:
        for n in r:
            grid[n] ^= 1

    out = []
    for index in xrange(2501):
        if grid[index]:
            out.append(str(index))

    value = ' '.join(out)
    output_lines.append('Case #%s: %s' % (case+1, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)