
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
        if inputs[index] not in r_bff:
            r_bff[inputs[index]] =[]

        r_bff[inputs[index]].append( index+1 )

    gc = 0
    gpath = []
    g_start = 0
    g_last = 0
    g_node_c = {}
    for index in xrange(1, n+1):

        current = index
        visited = {}
        path = []
        node_c = {}
        last = 0
        start = 0
        c = 0
        while current in bff:
            node_c[current] = c
            c += 1
            path.append(current)
            visited[current] = True
            last = current
            current = bff[current]

            if current in visited:
                start = current
                break

        if c > gc:
            gc = c
            gpath = path
            g_last = last
            g_start = start
            g_node_c = node_c


    print gpath
    print start
    print 'gc', gc
    print 'loop start, %s, loop end %s' % ( g_start, g_last)
    print 'r_bff start, %s, r_bff end %s' % ( r_bff[g_start], r_bff[g_last])
    print 'node_c g_start, %s, node_c g_end %s' % ( g_node_c[g_start], g_node_c[g_last])
    # value = gc - g_node_c[g_start]

    cycle_paths = []

    c_start = g_start
    cycle_paths.append(c_start)
    while c_start != g_last:
        c_start = bff[c_start]
        cycle_paths.append(c_start)

    value = len(cycle_paths)

    if value == 2:

        max_l = 0
        max_r = 0
        for index in xrange(1, n+1):
            print ''
            print index
            if index not in cycle_paths:
                l = 0
                l_l = 0
                l_r = 0
                fl = 0
                fr = 0
                s = bff[index]
                while s in bff and s != index:
                    print s
                    if s == g_start:
                        l_l = l

                    if s == g_last and not l_l:
                        l_r = l

                    if l_l and l_r:
                        break

                    l += 1
                    s = bff[s]

                print l_l, l_r
                max_l = max(max_l, l_l)
                max_r = max(max_r, l_r)


        print value, max_l, max_r
        value += max_l + max_r





    # print 'cycle paths', cycle_paths
    # print value
    #
    # for index in xrange(1, n+1):
    #     if index not in gpath and g_start in r_bff:
    #         if index in r_bff[g_start]:
    #             value += 1
    #             print 'v', value, 'i', index
    #             break
    #
    # for index in xrange(1, n+1):
    #     if index not in gpath and g_last in r_bff:
    #         if index in r_bff[g_last]:
    #             value += 1
    #             print 'v1', value, 'i', index
    #             break


    print value

    print ''
    output_lines.append('Case #%s: %s' % (case+1, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)