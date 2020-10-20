# Todo: K_Map for 3 inputs.
def inp3_k_map(mt, nip):
    for i in range(50): print("-", end='')
    print()
    var_re =["A","B","C"]
    ansg = [[0, 0, 0, 0], [0, 0, 0, 0]]
    ansgmx = [[0, 0, 0, 0], [0, 0, 0, 0]]
    op = ''
    flag = 0
    qrd = []
    dul = []
    sngl = []
    if nip == 1:
        qrd_var_2_2 = ["B' ", "C ", "B ", "C' "]
        qrd_var_1_4 = ["A' ", "A "]
        dul_vert = ["B'C' ", "B'C ", "BC ", "BC' "]
        dul_horz = [["A'B' ", "A'C ", "A'B ", "A'C' "], ["AB' ", "AC ", "AB ", "AC'"]]
        sngl_val = [["A'B'C' ", "A'B'C ", "A'BC ", "A'BC' "], ["AB'C' ", "AB'C ", "ABC ", "ABC' "]]
    elif nip == 2:
        qrd_var_2_2 = ["(B) ", "(C') ", "(B') ", "(C) "]
        qrd_var_1_4 = ["(A) ", "(A') "]
        dul_vert = ["(B+C) ", "(B+C') ", "(B'+C') ", "(B'+C) "]
        dul_horz = [["(A+B) ", "(A+C') ", "(A+B') ", "(A+C) "], ["(A'+B) ", "(A'+C') ", "(A'+B') ", "(A'+C) "]]
        sngl_val = [["(A+B+C) ", "(A+B+C') ", "(A+B'+C') ", "(A+B'+C) "],
                    ["(A'+B+C) ", "(A'+B+C') ", "(A'+B'+C') ", "(A'+B'+C) "]]
    for i in range(2):
        for j in range(4):
            p = int('0b' + bin(i)[2:] + bin(j)[2:], 2)
            if (i == 1) and (j == 0 or j == 1):
                p = int('0b' + bin(i)[2:] + '0' + bin(j)[2:], 2)
            if p in mt:
                ansg[i][j] = 1

    for i in range(2):
        (ansg[i][2], ansg[i][3]) = (ansg[i][3], ansg[i][2])
    for i in range(50): print("-", end='')
    print()
    print("K-Map plotted : ")
    if nip == 1:
        for each in ansg: print(*each)
    elif nip == 2:
        for i in range(2):
            for j in range(4):
                if ansg[i][j] == 1:
                    ansgmx[i][j] = 0
                else:
                    ansgmx[i][j] = 1
        for each in ansgmx: print(*each)

    if ansg == [[1] * 4, [1] * 4]:
        op = op + '1'
        flag = 1
    if flag == 0:
        for j in range(-1, 3):
            if ansg[0][j] == 1 and ansg[-1][j] == 1 and ansg[0][j + 1] == 1 and ansg[-1][j + 1] == 1:
                qrd.append([(0, j), (-1, j)])
                if j < 2:
                    qrd.append([(0, j + 1), (-1, j + 1)])
                    qrd.append([(0, j), (0, j + 1)])
                    qrd.append([(-1, j), (-1, j + 1)])
                else:
                    qrd.append([(0, -1), (-1, -1)])
                    qrd.append([(0, j), (0, -1)])
                    qrd.append([(-1, j), (-1, -1)])
                op = op + qrd_var_2_2[j]
    if flag == 0:
        for i in range(-1, 1):
            if ansg[i] == [1, 1, 1, 1]:
                qrd.append([(i, -1), (i, 0)])
                qrd.append([(i, 0), (i, 1)])
                qrd.append([(i, 1), (i, 2)])
                qrd.append([(i, 2), (i, -1)])
                op = op + qrd_var_1_4[i]
    if flag == 0:
        for j in range(-1, 3):
            if ansg[0][j] == 1 and ansg[1][j] == 1:
                temp = 0
                if [(0, j), (-1, j)] in qrd:
                    temp = 1
                elif [(-1, j), (0, j)] in qrd:
                    temp = 1
                if temp == 0:
                    dul.append([(0, j), (-1, j)])
                    op = op + dul_vert[j]

    if flag == 0:
        for i in range(-1, 1):
            for j in range(-1, 3):
                if ansg[i][j] == 1 and ansg[i][j + 1] == 1:
                    temp = 0
                    if j == 2:
                        if [(i, j), (i, -1)] in qrd:
                            temp = 1
                        elif [(i, -1), (i, j)] in qrd:
                            temp = 1
                    else:
                        if [(i, j), (i, j + 1)] in qrd:
                            temp = 1
                        elif [(i, j + 1), (i, j)] in qrd:
                            temp = 1
                    if temp == 0:
                        if j == 2:
                            dul.append([(i, 2), (i, -1)])
                        else:
                            dul.append([(i, j), (i, j + 1)])
                        op = op + dul_horz[i][j]

    op = op.rstrip(" ")
    opl = op.split(" ")
    for i in range(len(opl)):
        opl[i] = opl[i] + " "

    for each in dul:
        d1cnt = 0
        d2cnt = 0
        (d1, d2) = (each[0], each[1])
        for each1 in dul:
            if d1 in each1:
                d1cnt += 1
            if d2 in each1:
                d2cnt += 1
        if d1cnt > 1 and d2cnt > 1:
            (d1i, d1j) = d1
            (d2i, d2j) = d2
            if d1i == d2i:
                p = dul_horz[d1i][d1j]
                opl.remove(p)
            else:
                p = dul_vert[d1j]
                opl.remove(p)
            dul.remove([d1, d2])
    op = "".join(opl)

    for _ in qrd:
        for each in _:
            sngl.append(each)
    for _ in dul:
        for each in _:
            sngl.append(each)

    if flag == 0:
        for i in range(-1, 1):
            for j in range(-1, 3):
                if ansg[i][j] == 1:
                    if (i, j) not in sngl:
                        op = op + sngl_val[i][j]

    op = op.rstrip(" ")
    if nip == 1:
        op = op.replace(' ', ' + ')

    op = op.replace("A", var_re[0])
    op = op.replace("B", var_re[1])
    op = op.replace("C", var_re[2])
    for i in range(50): print("*", end='')
    print()
    print("The simplified equation is :", op)
    for i in range(50): print("*", end='')
    print()
    return op
