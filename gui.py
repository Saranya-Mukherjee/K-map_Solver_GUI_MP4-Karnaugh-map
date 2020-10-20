from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sqlite3
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageFont, ImageDraw
import colors
import exp_make

typ=0
e=None
selected=[]

def quitApp():
    v = askquestion("Exit?", "Sure to Quit K-Map Solver?")
    if v == "yes":
        root.destroy()

def ne():
    quitApp()

def sop():
    global typ,selected,exp
    if typ==0:
        b1.pack_forget()
        b2.pack_forget()
        e1.pack_forget()
        lbl1.pack_forget()
        lbl2.pack_forget()
        var.pack_forget()
        e1.pack_forget()
        boxes.pack_forget()
        delete_all_boxes()
        col_back()
        solve.pack_forget()
        selected = []
        e1.config(text="")
        solve.config(height=2)
        b1.pack(anchor="n", side="top", fill="x")
        f.pack(anchor="n", side="top", fill="x")
        lbl1.pack(anchor="n", side="top", fill="x")
        e1.pack(expand=True,fill="x",pady=10)
        lbl2.pack(anchor="n", side="top", fill="x")
        var.pack(anchor="n", side="top", fill="x")
        solve.pack(anchor="n", side="top", fill="x")
        boxes.pack(anchor="n", side="top", fill="both")
        typ = 1
        make_all_boxes("sop",int(var.get()))
        show_all_boxes(int(var.get()))
    else:
        typ=0
        pos()

def pos():
    global typ,selected,exp
    if typ == 0:
        b1.pack_forget()
        b2.pack_forget()
        e1.pack_forget()
        lbl1.pack_forget()
        lbl2.pack_forget()
        var.pack_forget()
        e1.pack_forget()
        boxes.pack_forget()
        delete_all_boxes()
        col_back()
        solve.pack_forget()
        selected = []
        e1.config(text="")
        solve.config(height=2)
        b2.pack(anchor="n", side="top", fill="x")
        f.pack(anchor="n", side="top", fill="x")
        lbl1.pack(anchor="n", side="top", fill="x")
        e1.pack(expand=True, fill="x", pady=10)
        lbl2.pack(anchor="n", side="top", fill="x")
        var.pack(anchor="n", side="top", fill="x")
        solve.pack(anchor="n", side="top", fill="x")
        boxes.pack(anchor="n", side="top", fill="both")
        make_all_boxes("pos", int(var.get()))
        show_all_boxes(int(var.get()))
        typ = -1
    else:
        typ=0
        sop()

def full(event):
    root.state('normal')

def full2():
    root.state('zoomed')

def col_back():
    o1.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o2.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o3.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o4.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o5.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o6.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o7.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o8.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o9.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o10.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o11.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o12.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o13.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o14.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o15.config(bg=colors.btn_bg, fg=colors.btn_fg)
    o16.config(bg=colors.btn_bg, fg=colors.btn_fg)

def col_ret(box):
    box += 1
    if box == 1:
        o1.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 2:
        o2.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 3:
        o3.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 4:
        o4.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 5:
        o5.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 6:
        o6.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 7:
        o7.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 8:
        o8.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 9:
        o9.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 10:
        o10.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 11:
        o11.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 12:
        o12.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 13:
        o13.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 14:
        o14.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 15:
        o15.config(bg=colors.btn_bg,fg=colors.btn_fg)
    elif box == 16:
        o16.config(bg=colors.btn_bg,fg=colors.btn_fg)

def colChange(n):
    n+=1
    if n==1:
        o1.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==2:
        o2.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==3:
        o3.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==4:
        o4.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==5:
        o5.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==6:
        o6.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==7:
        o7.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==8:
        o8.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==9:
        o9.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==10:
        o10.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==11:
        o11.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==12:
        o12.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==13:
        o13.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==14:
        o14.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==15:
        o15.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)
    elif n==16:
        o16.config(bg=colors.btn_bg_lat,fg=colors.btn_fg_lat)

def getexp(n):
    global exp,selected
    selected.sort()
    if n in selected:
        col_ret(n)
        selected.remove(n)
        # return
    else:
        selected.append(n)
        colChange(n)
    mode=""
    if typ==1:
        mode="sop"
    elif typ==-1:
        mode="pos"
    value=exp_make.make(selected,int(var.get()),mode)
    if typ==1:
        value=value[:-2:]
    elif typ== -1:
        value = value[:-1:]
    value=value.strip()
    e1.config(text=value)
    selected.sort()
    print(selected)

root=Tk()
root.config(bg=colors.bg_color)
root.protocol('WM_DELETE_WINDOW', ne)
cb = ttk.Combobox(root, values=[])
full2()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# Todo: define all k map box variable here
boxes=Frame(root,bg=colors.bg_color)
o1=Button(boxes,text="0",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(0))
o2=Button(boxes,text="1",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(1))
o3=Button(boxes,text="2",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(2))
o4=Button(boxes,text="3",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(3))
o5=Button(boxes,text="4",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(4))
o6=Button(boxes,text="5",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(5))
o7=Button(boxes,text="6",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(6))
o8=Button(boxes,text="7",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(7))
o9=Button(boxes,text="8",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(8))
o10=Button(boxes,text="9",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(9))
o11=Button(boxes,text="10",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(10))
o12=Button(boxes,text="11",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(11))
o13=Button(boxes,text="12",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(12))
o14=Button(boxes,text="13",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(13))
o15=Button(boxes,text="14",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(14))
o16=Button(boxes,text="15",width=w//75,font="comicsans 15",bg=colors.btn_bg,fg=colors.btn_fg,command=lambda: getexp(15))
t1=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t2=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t3=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t4=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t5=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t6=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t7=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t8=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 15")
t9=Label(boxes,text="",bg=colors.bg_color,fg=colors.btn_fg,font="comicsans 20 bold")
# t10=Label(boxes,text="CD",font="comicsans")
# t11=Label(boxes,text="",font="comicsans")
# t12=Label(boxes,text="",font="comicsans")
# t13=Label(boxes,text="",font="comicsans")
# t14=Label(boxes,text="",font="comicsans")
# t15=Label(boxes,text="",font="comicsans")
# t16=Label(boxes,text="",font="comicsans")

def show_all_boxes(n):
    t9.grid(row=0, column=0, padx=w / 12)
    if n==4:
        t1.grid(row=1,column=1,padx=w/12)
        t2.grid(row=1,column=2,padx=w/12)
        t3.grid(row=1,column=3,padx=w/12)
        t4.grid(row=1,column=4,padx=w/12)
        t5.grid(row=2,column=0,padx=w/12,pady=h//15)
        t6.grid(row=3,column=0,padx=w/12,pady=h//15)
        t7.grid(row=4,column=0,padx=w/12,pady=h//15)
        t8.grid(row=5,column=0,padx=w/12,pady=h//15)
        o1.grid(row=2,column=1)
        o2.grid(row=2,column=2)
        o4.grid(row=2,column=3)
        o3.grid(row=2,column=4)
        o5.grid(row=3, column=1)
        o6.grid(row=3, column=2)
        o8.grid(row=3, column=3)
        o7.grid(row=3, column=4)
        o13.grid(row=4, column=1)
        o14.grid(row=4, column=2)
        o16.grid(row=4, column=3)
        o15.grid(row=4, column=4)
        o9.grid(row=5, column=1)
        o10.grid(row=5, column=2)
        o12.grid(row=5, column=3)
        o11.grid(row=5, column=4)
    elif n==3:
        t1.grid(row=1, column=1, padx=w / 12)
        t2.grid(row=1, column=2, padx=w / 12)
        t3.grid(row=1, column=3, padx=w / 12)
        t4.grid(row=1, column=4, padx=w / 12)
        t5.grid(row=2, column=0, padx=w / 12, pady=h // 7)
        t6.grid(row=3, column=0, padx=w / 12, pady=h // 7)
        o1.grid(row=2, column=1)
        o2.grid(row=2, column=2)
        o4.grid(row=2, column=3)
        o3.grid(row=2, column=4)
        o5.grid(row=3, column=1)
        o6.grid(row=3, column=2)
        o8.grid(row=3, column=3)
        o7.grid(row=3, column=4)
    elif n==2:
        t1.grid(row=1, column=1, padx=w / 6)
        t2.grid(row=1, column=2, padx=w / 6)
        t3.grid(row=2, column=0, padx=w / 12, pady=h // 7)
        t4.grid(row=3, column=0, padx=w / 12, pady=h // 7)
        o1.grid(row=2, column=1)
        o2.grid(row=2, column=2)
        o3.grid(row=3, column=1)
        o4.grid(row=3, column=2)

def make_all_boxes(s,n):
    if s== "sop":
        if n==4:
            t1.config(text="00")
            t2.config(text="01")
            t3.config(text="11")
            t4.config(text="10")
            t5.config(text="00")
            t6.config(text="01")
            t7.config(text="11")
            t8.config(text="10")
            t9.config(text="AB _|_ CD-->")
        if n==3:
            t1.config(text="00")
            t2.config(text="01")
            t3.config(text="11")
            t4.config(text="10")
            t5.config(text="0")
            t6.config(text="1")
            t7.config(text="")
            t8.config(text="")
            t9.config(text="A _|_ BC-->")
        if n==2:
            t1.config(text="0")
            t2.config(text="1")
            t3.config(text="0")
            t4.config(text="1")
            t5.config(text="")
            t6.config(text="")
            t7.config(text="")
            t8.config(text="")
            t9.config(text="A _|_ B-->")
    elif s=="pos":
        if n==4:
            t1.config(text="0+0")
            t2.config(text="0+1")
            t3.config(text="1+1")
            t4.config(text="1+0")
            t5.config(text="0+0")
            t6.config(text="0+1")
            t7.config(text="1+1")
            t8.config(text="1+0")
            t9.config(text="AB _|_ CD-->")
        if n==3:
            t1.config(text="0+0")
            t2.config(text="0+1")
            t3.config(text="1+1")
            t4.config(text="1+0")
            t5.config(text="0")
            t6.config(text="1")
            t7.config(text="")
            t8.config(text="")
            t9.config(text="A _|_ BC-->")
        if n==2:
            t1.config(text="0")
            t2.config(text="1")
            t3.config(text="0")
            t4.config(text="1")
            t5.config(text="")
            t6.config(text="")
            t7.config(text="")
            t8.config(text="")
            t9.config(text="A _|_ B-->")

def delete_all_boxes():
    o1.grid_forget()
    o2.grid_forget()
    o3.grid_forget()
    o4.grid_forget()
    o5.grid_forget()
    o6.grid_forget()
    o7.grid_forget()
    o8.grid_forget()
    o9.grid_forget()
    o10.grid_forget()
    o11.grid_forget()
    o12.grid_forget()
    o13.grid_forget()
    o14.grid_forget()
    o15.grid_forget()
    o16.grid_forget()
    t1.grid_forget()
    t2.grid_forget()
    t3.grid_forget()
    t4.grid_forget()
    t5.grid_forget()
    t6.grid_forget()
    t7.grid_forget()
    t8.grid_forget()
    t9.grid_forget()

def ready():
    x.destroy()
    b1.pack(fill="both", expand=True)
    # e1.pack(fill="x")
    b2.pack(fill="both", expand=True)

def change(event):
    global typ,selected,exp
    if typ==1:
        typ = 0
        selected=[]
        e1.config(text="")
        col_back()
        sop()
    elif typ == -1:
        typ=0
        selected = []
        e1.config(text="")
        col_back()
        pos()

def show_result(answer):
    ans=Toplevel()
    ans.state("zoomed")
    ans.title("SEE THE RESULTS")
    Label(ans, text="This part is under processing...\nThis will show the answer in video form...\n BTW see your solution").pack()
    Label(ans,text=answer).pack()

def result():
    if len(selected)==0:
        return
    v=int(var.get())
    val=[]
    for i in selected:
        val.append(i)
    mode=0
    res=""
    if typ==1:
        mode=1
    elif typ== -1:
        mode=2
    if v==4:
        import solve_4
        res=solve_4.inp4_k_map(val,mode)
    elif v==3:
        import solve_3
        res=solve_3.inp3_k_map(val, mode)
    elif v==2:
        import solve_2
        res=solve_2.inp2_k_map(val, mode)
    show_result(res)

if __name__ == '__main__':
    root.title("K-Map Solver")
    root.geometry("644x644")
    root.bind('<Control-Key-f>', full)
    f=Frame(root,bg=colors.bg_color)
    x=Label(f,text="Welcome\n to\n K-Map Solver\n Mukherjee INC ",font="algerian 65 bold")
    x.pack(fill="both",expand=True)
    x.after(3000,ready)
    b1=Button(f,text="SOP",font="comicsans 50",bg=colors.bg_color,fg="#E54444",command=sop)
    b2=Button(f,text="POS",font="comicsans 50",bg=colors.bg_color,fg="#E54444",command=pos)
    exp=StringVar()
    # exp.set(exp_make.make([0,1,2,3])[:-2:])
    # e1 = Entry(f,font="comicsans 20", textvariable=exp)
    e1=Label(f,text="",font="comicsans 20")
    f.pack(fill="both",expand=True)
    # e = Text(f, font="comicsans", undo=True)
    var= ttk.Combobox(f,font="comicsans",values=[2, 3, 4])
    var.current(2)
    var.bind("<<ComboboxSelected>>", change)
    lbl1=Label(f, text="Your expression below: ", font="comicsans 10", bg=colors.bg_color, fg="white")
    lbl2=Label(f, text="Choose number of variables below: ", font="comicsans 10", bg=colors.bg_color, fg="white")
    solve=Button(root,font="comicsans 10",text="Solve",bg=colors.solve_b,fg=colors.solve_f,height="2",command=result)
root.mainloop()
