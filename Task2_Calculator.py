from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("400x480+50+100")
win.resizable(False,False)

ico=PhotoImage(file='calculator.png')
win.iconphoto(False,ico)


# functionlity and logic


def click(event):
    global output_val
    text=event.widget.cget("text")
    if(text=="="):
        if output_val.get().isdigit():
            value=float(output_val.get())
        else:
            try:
                value=eval(output_val.get())
            except Exception as e:
                output_val.set("Error")
        output_val.set(value)
        enty.update()
    elif(text=="C"):
        output_val.set("")
        enty.update()
    else:
        output_val.set(output_val.get()+text)
        enty.update()
    



# OutPut Screen for Result

output_val=StringVar()
output_val.set("")

output_frame=Frame(win,width=500,height=100,relief=RIDGE,bg="white"
                   ,borderwidth=10)
output_frame.pack(side=TOP,fill=X)

#entry
enty=Entry(output_frame,textvariable=output_val,fg="black",bg="white",
           font=("times new roman",50,"bold"),justify='right',state='readonly')
enty.pack(side=TOP,fill=BOTH)

# Input Screen

# frame

input_frame=Frame(win,width=395,height=370,bg="light grey",
                  relief=RIDGE)
input_frame.place(x=0,y=110)

#buttons

btn = Button(input_frame,text="7",width=3,height=1,font=("Arial",30))
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="8",width=3,height=1,font=("Arial",30))
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="9",width=3,height=1,font=("Arial",30))
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="/",width=3,height=1,font=("Arial",30))
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",click)

btn = Button(input_frame,text="4",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=1,column=0,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="5",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=1,column=1,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="6",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=1,column=2,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="*",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=1,column=3,padx=5,pady=5)
btn.bind("<Button-1>",click)

btn = Button(input_frame,text="1",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=2,column=0,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="2",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=2,column=1,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="3",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=2,column=2,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="-",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=2,column=3,padx=5,pady=5)
btn.bind("<Button-1>",click)

btn = Button(input_frame,text="C",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=3,column=0)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="0",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=3,column=1,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="=",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=3,column=2,padx=5,pady=5)
btn.bind("<Button-1>",click)
btn = Button(input_frame,text="+",width=3,height=1,font=("Arial",30),padx=5)
btn.grid(row=3,column=3,padx=5,pady=5)
btn.bind("<Button-1>",click)

win.mainloop()