
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')
T = int(input_lines[0])

case_start_index = 0
line_index = 1

for case in xrange(T):

    n = int(input_lines[line_index])
    line_index += 1

    inputs = map(int, input_lines[line_index].split(' '))
    line_index += 1

    bff = {}
    r_bff = {}
    for index in xrange(n):
        bff[index+1] = inputs[index]
        r_bff[inputs[index]] = index+1

    gc = 0




    value = gc
    output_lines.append('Case #%s: %s' % (case+1, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)