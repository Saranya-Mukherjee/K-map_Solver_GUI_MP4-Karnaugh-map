# Todo: K_Map for 2 inputs.
def inp2_k_map(mt, nip):
    for i in range(50): print("-", end='')
    print()
    prnt = ["A", "B"]
    for i in range(len(mt)):
        mt[i] = '0b' + bin(mt[i])[2:].lstrip('0')
    op = ''
    ans = [[0, 0], [0, 0]]
    ansmx = [[0, 0], [0, 0]]
    flag = 0
    temp = []
    for i in range(2):
        for j in range(2):
            p = '0b' + (bin(i)[2:] + bin(j)[2:]).lstrip('0')
            if p in mt:
                ans[i][j] = 1
    for i in range(50): print("-", end='')
    print()
    print("The kmap plotted : ")
    if nip == 1:
        for each in ans: print(*each)
    elif nip == 2:
        for i in range(2):
            for j in range(2):
                if ans[i][j] == 1:
                    ansmx[i][j] = 0
                else:
                    ansmx[i][j] = 1
        for each in ansmx: print(*each)
    if ans == [[1, 1], [1, 1]]:
        flag = 1
        op = '1'

    if flag == 0:
        for i in range(2):
            if ans[i] == [1, 1]:
                if nip == 1:
                    op = 'A ' if i == 1 else "A' "
                elif nip == 2:
                    op = "(A') " if i == 1 else "(A) "
                temp.extend([(i, 0), (i, 1)])

    if flag == 0:
        if ans[0][0] == 1 and ans[1][0] == 1:
            if nip == 1:
                op = op + "B' "
            elif nip == 2:
                op = op + "(B) "
            temp.extend([(0, 0), (1, 0)])
        elif ans[0][1] == 1 and ans[1][1] == 1:
            if nip == 1:
                op = op + "B "
            elif nip == 2:
                op = op + "(B') "
            temp.extend([(0, 1), (1, 1)])
    if nip == 1:
        vr = ["A'B' ", "A'B ", "AB' ", "AB "]
    elif nip == 2:
        vr = ["(A+B) ", "(A+B') ", "(A'+B) ", "(A'+B') "]

    if flag == 0:
        for i in range(2):
            for j in range(2):
                if ans[i][j] == 1 and (i, j) not in temp:
                    op = op + vr[int('0b' + bin(i)[2:] + bin(j)[2:], 2)]
    op = op.rstrip(" ")
    if nip == 1:
        op = op.replace(" ", "+")
    op = op.replace("A", prnt[0])
    op = op.replace("B", prnt[1])
    for i in range(50): print("*", end='')
    print()
    print("The simplified equation is :", op)
    for i in range(50): print("*", end='')
    print()
    return op
