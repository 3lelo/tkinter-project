from tkinter import *
from tkinter import ttk

# إنشاء الشاشة والألوان
bg_color = 'black'
fg_color = 'white'
highlight_color = bg_color

w = Tk()
w.title("Password Box")
w.configure(bg=bg_color)
w.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

# إضافةالصور
p = PhotoImage(file='cancel.png')
p = p.subsample(25,25)

p_show = PhotoImage(file='show.png')
p_show = p_show.subsample(31,31)

p_hide = PhotoImage(file='hide.png')
p_hide = p_hide.subsample(31,31)

p_lock = PhotoImage(file='lock.png')
p_lock = p_lock.subsample(30,30)

p_delete = PhotoImage(file='delete.png')
p_delete = p_delete.subsample(30,30)

p_backspace = PhotoImage(file='backspace.png')
p_backspace = p_backspace.subsample(30,30)

p_btreq = PhotoImage(file='btreq.png')
p_btreq = p_btreq.subsample(2,3)

p_jorge = PhotoImage(file='jorge.png')
p_jorge = p_jorge.subsample(2,2)

p_happy = PhotoImage(file='jorge_happy.png')
p_happy = p_happy.subsample(2,2)

# Customizing the style for TButton
style.configure('TButton',
                font=('Arial', 12),
                foreground=fg_color,
                background=bg_color,
                borderwidth=3,
                relief="raised",
                padding=3)

style.map('TButton',
          foreground=[('active', highlight_color)],
          background=[('active', fg_color)])

# Customizing the style for show.TButton
style.configure('show.TButton',
                font=('Arial', 10),
                foreground=fg_color,
                background=bg_color,
                borderwidth=3,
                relief="raised",
                padding=6)

style.map('show.TButton',
          foreground=[('active', highlight_color)],
          background=[('active', fg_color)])

# Customizing the style for TLabel
style.configure('TLabel',
                font=('Arial', 10),
                foreground=fg_color,
                background=bg_color)

# Customizing the style for FLabel
style.configure('F.TLabel',
                font=('Arial', 20),
                foreground='red',
                background='black')

# Customizing the style for SLabel
style.configure('S.TLabel',
                font=('Arial', 20),
                foreground='green',
                background='black')

# Customizing the style for TEntry
style.configure('TEntry',
                font=('Arial', 15),
                foreground=fg_color,
                background=bg_color,
                fieldbackground=bg_color,
                insertcolor=fg_color,
                padding=5)

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

    if ent.get().strip() == '' or len(ent.get()) < 8:
        w.title("Failed")
        filed = ttk.Label(w, style='F.TLabel', text='Failed!')
        filed.place(x=0,y=0)

        jorge = ttk.Label(w,state='TLabel',image=p_jorge)
        jorge.place(x=50,y=30)
    else:
        w.title("success")
        sub = ttk.Label(w, style='S.TLabel', text='You have successfully logged in!')
        sub.place(x=0,y=0)

        jorge = ttk.Label(w,state='TLabel',image=p_happy)
        jorge.place(x=70,y=50)
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

# أمر انهاء البرنامج عند الضغط على زر الإلغاء
def end():
    w.destroy()

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
photo_cancel = ttk.Button(w,image=p,style='TButton',command=end)
photo_cancel.place(x=420,y=-7)

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
photo.place(x=150,y=28)

# تشغيل الكود
w.mainloop()