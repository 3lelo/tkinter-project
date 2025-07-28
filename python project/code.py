from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# إنشاء الشاشة والألوان
bg_color = 'black'
fg_color = 'white'

w = Tk()
w.title("Password Box")
w.configure(bg=bg_color)
w.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

# إضافةالصور
p = PhotoImage(file='python project\\close.png')
p = p.subsample(25,25)

p_show = PhotoImage(file='python project\\show.png')
p_show = p_show.subsample(31,31)

p_hide = PhotoImage(file='python project\\hide.png')
p_hide = p_hide.subsample(31,31)

p_lock = PhotoImage(file='python project\\lock.png')
p_lock = p_lock.subsample(30,30)

p_delete = PhotoImage(file='python project\\delete.png')
p_delete = p_delete.subsample(30,30)

p_backspace = PhotoImage(file='python project\\backspace.png')
p_backspace = p_backspace.subsample(30,30)

p_btreq = PhotoImage(file='python project\\btreq.png')
p_btreq = p_btreq.subsample(2,4)


p_happy = PhotoImage(file='python project\\jorge_happy.png')
p_happy = p_happy.subsample(2,2)

# Customizing the style for TButton
style.configure('TButton',
                font=('Arial', 12),
                foreground=fg_color,
                background=bg_color,
                borderwidth=0,
                relief="raised",
                padding=3)

style.map('TButton',
          foreground=[('active', bg_color)],
          background=[('active', fg_color)])

# Customizing the style for show.TButton
style.configure('show.TButton',
                font=('Arial', 10),
                foreground=fg_color,
                background=bg_color,
                borderwidth=0,
                relief="raised",
                padding=6)

style.map('show.TButton',
          foreground=[('active', bg_color)],
          background=[('active', fg_color)])

# Customizing the style for C.TButton
style.configure('C.TButton',
                font=('Arial', 5),
                foreground=fg_color,
                background=bg_color,
                borderwidth=0,
                relief="raised",
                padding=0)

style.map('C.TButton',
          foreground=[('active', bg_color)],
          background=[('active', "#ff4242")])

# Customizing the style for TLabel
style.configure('TLabel',
                font=('Arial', 10),
                foreground=fg_color,
                background=bg_color)


# Customizing the style for SLabel
style.configure('S.TLabel',
                font=('Arial', 20),
                foreground='green',
                background=bg_color)

# Customizing the style for TEntry
style.configure('TEntry',
                font=('Arial', 15),
                foreground=fg_color,
                background=bg_color,
                fieldbackground=bg_color,
                insertcolor=fg_color,
                padding=6)

# submit الأمر الذي سيحصل بعد الضغط على
def submit():
    def destroy():
        back_space.destroy()
        del_b.destroy()
        sub_b.destroy()
        ent.destroy()
        shw.destroy()
        note.destroy()
        note2.destroy()
        photo.destroy()

    if ent.get().strip() == '':
        messagebox.showwarning(title='Error', message="Don't leave the box empty")
    elif len(ent.get()) < 8:
        messagebox.showwarning(title='Error', message="Did you read the note down?")
    else:
        w.title("success")
        ttk.Label(w, style='S.TLabel', text='You have successfully logged in!').place(x=0,y=0)

        ttk.Label(w,state='TLabel',image=p_happy).place(x=70,y=50)
        destroy()


# delete أمر حذف النص كامل عند الضغط على
def delete():
    ent.delete(0, END)

# backspace أمر حذف اخر حرف كتب بعد الضغط على
def backspace():
    ent.delete(len(ent.get()) - 1, END)

# أمر إظهار كلمة المرور بعد الضغط على المربع
def show():
    if ent.cget('show') == '':
        ent.configure(show='*')
        shw.configure(text='Show password ',image=p_show)
    else:
        ent.configure(show='')
        shw.configure(text='Hide password  ',image=p_hide)


# صندوق ادخال النص
ent = ttk.Entry(w, style='TEntry', show='*')
ent.pack(anchor=W, padx=10, pady=5)

# submit زر
sub_b = ttk.Button(w, text='Submit', style='TButton',
                   image=p_lock,
                   compound=LEFT,
                   command=submit)
sub_b.pack(anchor=W, padx=10, pady=5)

# delete زر
del_b = ttk.Button(w, text='Delete', style='TButton',
                   image=p_delete,
                   compound=LEFT,
                   command=delete)
del_b.pack(anchor=W, padx=10, pady=5)

# backspace زر
back_space = ttk.Button(w, text='Backspace', style='TButton',
                        image=p_backspace,
                        compound=LEFT,
                        command=backspace)
back_space.pack(anchor=W, padx=10, pady=5)

# زر إغلاق البرنامج
ttk.Button(w,image=p,style='C.TButton',command=w.destroy).place(x=425,y=0)

# زر إظهار كلمة المرور
shw = ttk.Button(w, text='Show password ', style='show.TButton',
                image=p_show, compound= LEFT,
                command=show)
shw.pack(anchor=W, padx=10, pady=5)

# قواعد كلمة المرور الصحيحة
note = ttk.Label(w, text='* Note: The length of the password should be >= 8 and do not leave it null',
                style='TLabel')
note.pack(anchor=W, padx=10, pady=5)

# الإرشاد لمكان إدخال كلمة المرور
note2 = ttk.Label(w,style='TLabel',text='<-- Enter your password here')
note2.place(x=150,y=7)

# صورة هبل
photo = ttk.Label(w,style='TLabel',image=p_btreq)
photo.place(x=150,y=40)

# تشغيل الكود
w.mainloop()
