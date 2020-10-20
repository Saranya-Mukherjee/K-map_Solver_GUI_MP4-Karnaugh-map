# Todo: K_Map for 4 inputs.
def inp4_k_map(mt, nip):
    import copy
    for _ in range(50): print("-", end='')
    print()
    pr_v = ["A","B","C","D"]
    an = []
    anmx = []
    (tmp, flag) = (0, 0)
    op = ''
    for i in range(4):
        an.append([0] * 4)
        anmx.append([0] * 4)

    for i in range(4):
        for j in range(4):
            if i < 2:
                bi = '0' + bin(i)[2:]
            else:
                bi = bin(i)[2:]
            if j < 2:
                bj = '0' + bin(j)[2:]
            else:
                bj = bin(j)[2:]
            p = int('0b' + bi + bj, 2)
            if p in mt:
                an[i][j] = 1
    for i in range(4):
        (an[i][2], an[i][3]) = (an[i][3], an[i][2])
    for i in range(4):
        (an[2][i], an[3][i]) = (an[3][i], an[2][i])

    for _ in range(50): print("-", end='')
    print()
    print("The K-Map plotted : ")
    if nip == 1:
        for each in an:
            print(*each)
    elif nip == 2:
        for i in range(4):
            for j in range(4):
                if an[i][j] == 1:
                    anmx[i][j] = 0
                else:
                    anmx[i][j] = 1
        for each in anmx: print(*each)

    octa = []
    qrd = []
    qrd_ref = []
    qrd_rep = []
    dul = []
    sngl = []
    if nip == 1:
        octa_val = [["C' ", "D ", "C ", "D' "], ["A' ", "B ", "A ", "B' "]]  # 0 for vert and 1 for horz
        qrd_val = [["C'D' ", "C'D ", "CD ", "CD' "], ["A'B' ", "A'B ", "AB ", "AB' "]]  # 0 for vert and 1 for horz
        qrd_val_4 = [["A'C' ", "A'D ", "A'C ", "A'D' "], ["BC' ", "BD ", "BC ", "BD' "], ["AC' ", "AD ", "AC ", "AD' "],
                     ["B'C' ", "B'D ", "B'C ", "B'D' "]]
        dul_vert = [["A'C'D' ", "A'C'D ", "A'CD ", "A'CD' "], ["BC'D' ", "BC'D ", "BCD ", "BCD' "],
                    ["AC'D' ", "AC'D ", "ACD ", "ACD' "], ["B'C'D' ", "B'C'D ", "B'CD ", "B'CD' "]]
        dul_horz = [["A'B'C' ", "A'B'D ", "A'B'C ", "A'B'D' "], ["A'BC' ", "A'BD ", "A'BC ", "A'BD' "],
                    ["ABC' ", "ABD ", "ABC ", "ABD' "], ["AB'C' ", "AB'D ", "AB'C ", "AB'D' "]]
        sngl_val = [["A'B'C'D' ", "A'B'C'D ", "A'B'CD ", "A'B'CD' "], ["A'BC'D' ", "A'BC'D ", "A'BCD ", "A'BCD' "],
                    ["ABC'D' ", "ABC'D ", "ABCD ", "ABCD' "], ["AB'C'D' ", "AB'C'D ", "AB'CD ", "AB'CD' "]]
    elif nip == 2:
        octa_val = [["(C) ", "(D') ", "(C') ", "(D) "], ["(A) ", "(B') ", "(A') ", "(B) "]]  # 0 for vert and 1 for horz
        qrd_val = [["(C+D) ", "(C+D') ", "(C'+D') ", "(C'+D) "],
                   ["(A+B) ", "(A+B') ", "(A'+B') ", "(A'+B) "]]  # 0 for vert and 1 for horz
        qrd_val_4 = [["(A+C) ", "(A+D') ", "(A+C') ", "(A+D) "], ["(B'+C) ", "(B'+D') ", "(B'+C') ", "(B'+D) "],
                     ["(A'+C) ", "(A'+D') ", "(A'+C') ", "(A'+D) "], ["(B+C) ", "(B+D') ", "(B+C') ", "(B+D) "]]
        dul_vert = [["(A+C+D) ", "(A+C+D') ", "(A+C'+D') ", "(A+C'+D) "],
                    ["(B'+C+D) ", "(B'+C+D') ", "(B'+C'+D') ", "(B'+C'+D) "],
                    ["(A'+C+D) ", "(A'+C+D') ", "(A'+C'+D') ", "(A'+C'+D) "],
                    ["(B+C+D) ", "(B+C+D') ", "(B+C'+D') ", "(B+C'+D) "]]
        dul_horz = [["(A+B+C) ", "(A+B+D') ", "(A+B+C') ", "(A+B+D) "],
                    ["(A+B'+C) ", "(A+B'+D') ", "(A+B'+C') ", "(A+B'+D) "],
                    ["(A'+B'+C) ", "(A'+B'+D') ", "(A'+B'+C') ", "(A'+B'+D) "],
                    ["(A'+B+C) ", "(A'+B+D') ", "(A'+B+C') ", "(A'+B+D) "]]
        sngl_val = [["(A+B+C+D) ", "(A+B+C+D') ", "(A+B+C'+D') ", "(A+B+C'+D) "],
                    ["(A+B'+C+D) ", "(A+B'+C+D') ", "(A+B'+C'+D') ", "(A+B'+C'+D) "],
                    ["(A'+B'+C+D) ", "(A'+B'+C+D') ", "(A'+B'+C'+D') ", "(A'+B'+C'+D) "],
                    ["(A'+B+C+D) ", "(A'+B+C+D') ", "(A'+B+C'+D') ", "(A'+B+C'+D) "]]

    if an == [[1] * 4, [1] * 4, [1] * 4, [1] * 4]:
        op = '1'
    else:
        for i in range(-1, 3):
            if an[i][0] == 1 and an[i][1] == 1 and an[i][2] == 1 and an[i][-1] == 1 and an[i + 1][0] == 1 and an[i + 1][1] == 1 and an[i + 1][2] == 1 and an[i + 1][-1] == 1:
                op = op + octa_val[1][i]
                octa.append([(i, 0), (i, 1), (i, 2), (i, -1)])
                if i < 2:
                    octa.append([(i + 1, 0), (i + 1, 1), (i + 1, 2), (i + 1, -1)])
                else:
                    octa.append([(-1, 0), (-1, 1), (-1, 2), (-1, -1)])
                if i < 2:
                    octa.append([(i, 0), (i + 1, 0), (i, 1), (i + 1, 1)])
                    octa.append([(i, 1), (i + 1, 1), (i, 2), (i + 1, 2)])
                    octa.append([(i, 2), (i + 1, 2), (i, -1), (i + 1, -1)])
                    octa.append([(i, -1), (i + 1, -1), (i, 0), (i + 1, 0)])
                else:
                    octa.append([(i, 0), (-1, 0), (i, 1), (-1, 1)])
                    octa.append([(i, 1), (-1, 1), (i, 2), (-1, 2)])
                    octa.append([(i, 2), (-1, 2), (i, -1), (-1, -1)])
                    octa.append([(i, -1), (-1, -1), (i, 0), (-1, 0)])

        for i in range(-1, 3):
            if an[0][i] == 1 and an[1][i] == 1 and an[2][i] == 1 and an[-1][i] == 1 and an[0][i + 1] == 1 and an[1][i + 1] == 1 and an[2][i + 1] == 1 and an[-1][i + 1] == 1:
                op = op + octa_val[0][i]
                octa.append([(0, i), (1, i), (2, i), (-1, i)])
                if i < 2:
                    octa.append([(0, i + 1), (1, i + 1), (2, i + 1), (-1, i + 1)])
                else:
                    octa.append([(0, -1), (1, -1), (2, -1), (-1, -1)])
                if i < 2:
                    octa.append([(0, i), (1, i), (0, i + 1), (1, i + 1)])
                    octa.append([(1, i), (2, i), (1, i + 1), (2, i + 1)])
                    octa.append([(2, i), (-1, i), (2, i + 1), (-1, i + 1)])
                    octa.append([(-1, i), (0, i), (-1, i + 1), (0, i + 1)])
                else:
                    octa.append([(0, i), (1, i), (0, -1), (1, -1)])
                    octa.append([(1, i), (2, i), (1, -1), (2, -1)])
                    octa.append([(2, i), (-1, i), (2, -1), (-1, -1)])
                    octa.append([(-1, i), (0, i), (-1, -1), (0, -1)])

        for i in range(-1, 3):
            if an[i][0] == 1 and an[i][1] == 1 and an[i][2] == 1 and an[i][-1] == 1:
                qrd_ref.append([(i, 0), (i, 1), (i, 2), (i, -1)])
            if an[0][i] == 1 and an[1][i] == 1 and an[2][i] == 1 and an[-1][i] == 1:
                qrd_ref.append([(0, i), (1, i), (2, i), (-1, i)])

        for i in range(-1, 3):
            for j in range(-1, 3):
                if an[i][j] == 1 and an[i][j + 1] == 1 and an[i + 1][j] == 1 and an[i + 1][j + 1] == 1:
                    if i == 2 and j == 2:
                        temp = [(i, j), (-1, j), (i, -1), (-1, -1)]
                    elif i == 2 and j < 2:
                        temp = [(i, j), (-1, j), (i, j + 1), (-1, j + 1)]
                    elif j == 2 and i < 2:
                        temp = [(i, j), (i + 1, j), (i, -1), (i + 1, -1)]
                    else:
                        temp = [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
                    qrd_ref.append(temp)

        for i in range(-1, 3):
            if an[i][0] == 1 and an[i][1] == 1 and an[i][2] == 1 and an[i][-1] == 1:
                if [(i, 0), (i, 1), (i, 2), (i, -1)] not in octa:
                    op = op + qrd_val[1][i]
                    qrd.append([(i, 0), (i, 1)])
                    qrd.append([(i, 1), (i, 2)])
                    qrd.append([(i, 2), (i, -1)])
                    qrd.append([(i, -1), (i, 0)])

        for i in range(-1, 3):
            if an[0][i] == 1 and an[1][i] == 1 and an[2][i] == 1 and an[-1][i] == 1:
                if [(0, i), (1, i), (2, i), (-1, i)] not in octa:
                    op = op + qrd_val[0][i]
                    qrd.append([(0, i), (1, i)])
                    qrd.append([(1, i), (2, i)])
                    qrd.append([(2, i), (-1, i)])
                    qrd.append([(-1, i), (0, i)])

        for i in range(-1, 3):
            for j in range(-1, 3):
                if an[i][j] == 1 and an[i][j + 1] == 1 and an[i + 1][j] == 1 and an[i + 1][j + 1] == 1:
                    if i == 2 and j == 2:
                        temp = [(i, j), (-1, j), (i, -1), (-1, -1)]
                    elif i == 2 and j < 2:
                        temp = [(i, j), (-1, j), (i, j + 1), (-1, j + 1)]
                    elif j == 2 and i < 2:
                        temp = [(i, j), (i + 1, j), (i, -1), (i + 1, -1)]
                    else:
                        temp = [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
                    if temp not in octa:
                        op = op + qrd_val_4[i][j]
                        if i < 2 and j < 2:
                            qrd.append([(i, j), (i, j + 1)])
                            qrd.append([(i + 1, j), (i + 1, j + 1)])
                            qrd.append([(i, j), (i + 1, j)])
                            qrd.append([(i, j + 1), (i + 1, j + 1)])
                        if j == 2 and i < 2:
                            qrd.append([(i, j), (i, -1)])
                            qrd.append([(i + 1, j), (i + 1, -1)])
                            qrd.append([(i, j), (i + 1, j)])
                            qrd.append([(i, -1), (i + 1, -1)])
                        if j < 2 and i == 2:
                            qrd.append([(i, j), (i, j + 1)])
                            qrd.append([(-1, j), (-1, j + 1)])
                            qrd.append([(i, j), (-1, j)])
                            qrd.append([(i, j + 1), (-1, j + 1)])
                        if i == 2 and j == 2:
                            qrd.append([(i, j), (i, -1)])
                            qrd.append([(-1, j), (-1, -1)])
                            qrd.append([(i, j), (-1, j)])
                            qrd.append([(i, -1), (-1, -1)])

        for i in range(-1, 3):
            for j in range(-1, 3):
                if an[i][j] == 1 and an[i][j + 1] == 1:
                    if j == 2:
                        temp = [(i, j), (i, -1)]
                    else:
                        temp = [(i, j), (i, j + 1)]
                    if temp not in qrd:
                        op = op + dul_horz[i][j]
                        if j == 2:
                            dul.append([(i, j), (i, -1)])
                        else:
                            dul.append([(i, j), (i, j + 1)])
                if an[i][j] == 1 and an[i + 1][j] == 1:
                    if i == 2:
                        temp = [(i, j), (-1, j)]
                    else:
                        temp = [(i, j), (i + 1, j)]
                    if temp not in qrd:
                        op = op + dul_vert[i][j]
                        if i == 2:
                            dul.append([(i, j), (-1, j)])
                        else:
                            dul.append([(i, j), (i + 1, j)])

        for each in octa:
            sngl.extend(each)
        for each in qrd:
            sngl.extend(each)
        for each in dul:
            sngl.extend(each)
        for i in range(-1, 3):
            for j in range(-1, 3):
                if an[i][j] == 1:
                    if (i, j) not in sngl:
                        op = op + sngl_val[i][j]

        op = op.strip()
        opl = op.split(" ")
        for i in range(len(opl)):
            opl[i] = opl[i] + " "

        dulref = copy.deepcopy(dul)

        for each in dul:
            (d1, d2) = (each[0], each[1])
            (cntd1, cntd2) = (0, 0)
            for each in dulref:
                if d1 in each:
                    cntd1 += 1
                if d2 in each:
                    cntd2 += 1
            for each in qrd_ref:
                if d1 in each:
                    cntd1 += 1
                if d2 in each:
                    cntd2 += 1
            if cntd1 > 1 and cntd2 > 1:
                try:
                    if d1[0] == d2[0]:
                        opl.remove(dul_horz[d1[0]][d1[1]])
                    if d1[1] == d2[1]:
                        opl.remove(dul_vert[d1[0]][d1[1]])
                    dulref.remove([(d1[0], d1[1]), (d2[0], d2[1])])
                except ValueError:
                    continue

        for each in qrd_ref:
            (d1, d2, d3, d4) = (each[0], each[1], each[2], each[3])
            (d1cnt, d2cnt, d3cnt, d4cnt) = (0, 0, 0, 0)
            for each1 in dul:
                if d1 in each1:
                    d1cnt += 1
                if d2 in each1:
                    d2cnt += 1
                if d3 in each1:
                    d3cnt += 1
                if d4 in each1:
                    d4cnt += 1
            for each2 in qrd_ref:
                if each != each2:
                    if d1 in each2:
                        d1cnt += 1
                    if d2 in each2:
                        d2cnt += 1
                    if d3 in each2:
                        d3cnt += 1
                    if d4 in each2:
                        d4cnt += 1
            if d1cnt > 0 and d2cnt > 0 and d3cnt > 0 and d4cnt > 0:
                try:
                    if d1[0] != d2[0] and d1[1] != d3[1]:
                        opl.remove(qrd_val_4[d1[0]][d1[1]])
                except ValueError:
                    continue

        for each in qrd_ref:
            (d1, d2, d3, d4) = (each[0], each[1], each[2], each[3])
            (d1cnt, d2cnt, d3cnt, d4cnt) = (0, 0, 0, 0)
            for each1 in qrd_ref:
                if each1 != each:
                    if d1 in each1:
                        d1cnt += 1
                    if d2 in each1:
                        d2cnt += 1
                    if d3 in each1:
                        d3cnt += 1
                    if d4 in each1:
                        d4cnt += 1
                if d1cnt > 0 and d2cnt > 0 and d3cnt > 0 and d4cnt > 0:
                    try:
                        if d1[0] == d2[0] == d3[0] == d4[0]:
                            opl.remove(qrd_val[1][d1[0]])
                        elif d1[1] == d2[1] == d3[1] == d4[1]:
                            opl.remove(qrd_val[0][d1[1]])
                    except ValueError:
                        continue

        op = ''.join(opl)
    for _ in range(50): print("*", end='')
    print()
    op = op.strip(" ")
    if nip == 1:
        op = op.replace(" ", " + ")
    op = op.replace("A", pr_v[0])
    op = op.replace("B", pr_v[1])
    op = op.replace("C", pr_v[2])
    op = op.replace("D", pr_v[3])
    print("Simplified equation is :", op)

    for _ in range(50): print("*", end='')
    print()
    return op
