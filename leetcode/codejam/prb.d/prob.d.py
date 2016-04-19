
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')


case = 0
for a_input in input_lines[1:]:
    case += 1
    n = len(a_input)

    K, C, S = map(int, a_input.split(' '))



    value = 0
    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)