def make(sel, var, mode):
    exp=""
    sel.sort()
    if mode =="sop":
        if var == 4:
            for i in sel:
                if i == 0:
                    exp += " A'B'C'D' +"
                elif i == 1:
                    exp += " A'B'C'D +"
                elif i == 2:
                    exp += " A'B'CD' +"
                elif i == 3:
                    exp += " A'B'CD +"
                elif i == 4:
                    exp += " A'BC'D' +"
                elif i == 5:
                    exp += " A'BC'D +"
                elif i == 6:
                    exp += " A'BCD' +"
                elif i == 7:
                    exp += " A'BCD +"
                elif i == 8:
                    exp += " AB'C'D' +"
                elif i == 9:
                    exp += " AB'C'D +"
                elif i == 10:
                    exp += " AB'CD' +"
                elif i == 11:
                    exp += " AB'CD +"
                elif i == 12:
                    exp += " ABC'D' +"
                elif i == 13:
                    exp += " ABC'D +"
                elif i == 14:
                    exp += " ABCD' +"
                elif i == 15:
                    exp += " ABCD +"
        elif var == 3:
            for i in sel:
                if i == 0:
                    exp += " A'B'C' +"
                elif i == 1:
                    exp += " A'B'C +"
                elif i == 2:
                    exp += " A'BC +"
                elif i == 3:
                    exp += " A'BC' +"
                elif i == 4:
                    exp += " AB'C' +"
                elif i == 5:
                    exp += " ABC' +"
                elif i == 6:
                    exp += " ABC' +"
                elif i == 7:
                    exp += " ABC +"
        elif var == 2:
            for i in sel:
                if i == 0:
                    exp += " A'B' +"
                elif i == 1:
                    exp += " A'B +"
                elif i == 2:
                    exp += " AB' +"
                elif i == 3:
                    exp += " AB +"
    elif mode =="pos":
        if var == 4:
            for i in sel:
                if i == 0:
                    exp += " (A+B+C+D) "
                elif i == 1:
                    exp += " (A+B+C+D') "
                elif i == 2:
                    exp += " (A+B+C'+D) "
                elif i == 3:
                    exp += " (A+B+C'+D') "
                elif i == 4:
                    exp += " (A+B'+C+D) "
                elif i == 5:
                    exp += " (A+B'+C+D') "
                elif i == 6:
                    exp += " (A+B'+C'+D) "
                elif i == 7:
                    exp += " (A+B'+C'+D') "
                elif i == 8:
                    exp += " (A'+B+C+D) "
                elif i == 9:
                    exp += " (A'+B+C+D') "
                elif i == 10:
                    exp += " (A'+B+C'+D) "
                elif i == 11:
                    exp += " (A'+B+C'+D') "
                elif i == 12:
                    exp += " (A'+B'+C+D) "
                elif i == 13:
                    exp += " (A'+B'+C+D') "
                elif i == 14:
                    exp += " (A'+B'+C'+D) "
                elif i == 15:
                    exp += " (A'+B'+C'+D') "
        elif var == 3:
            for i in sel:
                if i == 0:
                    exp += " (A+B+C) "
                elif i == 1:
                    exp += " (A+B+C') "
                elif i == 2:
                    exp += " (A+B'+C) "
                elif i == 3:
                    exp += " (A+B'+C') "
                elif i == 4:
                    exp += " (A'+B+C) "
                elif i == 5:
                    exp += " (A'+B+C') "
                elif i == 6:
                    exp += " (A'+B'+C) "
                elif i == 7:
                    exp += " (A'+B'+C') "
        elif var == 2:
            for i in sel:
                if i == 0:
                    exp += " (A+B) "
                elif i == 1:
                    exp += " (A+B') "
                elif i == 2:
                    exp += " (A'+B) "
                elif i == 3:
                    exp += " (A'+B') "
    return exp
