import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

def control_type(f):
    data = f
    if data.isdigit() and data != " " and len(f) == 11:
        return True
    else:
        return False

window = Tk()
window.title('Авторизация')
window.geometry('450x300')
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def Reg_clicked():
    newWindow = tkinter.Toplevel(window)
    newWindow.title('Регистрация')
    newWindow.geometry('450x200')
    window.withdraw()

    username_label = Label(newWindow, text='Имя пользователя', font=label_font, **base_padding)
    username_label.pack()

    username_entry = Entry(newWindow, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(newWindow, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(newWindow, bg='#fff', fg='#444', font=font_entry)
    password_entry.pack()

    def Reg1_clicked():
        #prowerka na wwod nomera
        username = username_entry.get()
        password = password_entry.get()
        flag = True
        with open("Пользователи.txt","r",encoding = "utf8") as user, open("Мэнеджеры.txt","r",encoding = "utf8") as menager, open("Дальнобойщики.txt","r",encoding = "utf8") as worker:
            text_user =  user.read().splitlines()
            text_menager = menager.read().splitlines()
            text_worker = worker.read().splitlines()
        for line_user in text_user:
            line_user = line_user.split(",")
            for line_menager in text_menager:
                line_menager = line_menager.split(",")
                for line_worker in text_worker:
                    line_worker = line_worker.split(",")
                    if line_user[0] == username:
                        messagebox.showerror("error", "Данный пользователь существует")
                        break
                    elif (line_menager[0] == username  and line_menager[1] == password) or (line_worker[0] == username  and line_worker[1] == password):
                        messagebox.showerror("error","Данный полльзователь зарегистрирован в системе в другой роли ,измените номер телефона или пароль")
                    else:
                        flag = False
            if flag == False:
                m = control_type(username)
                if m == True:
                    #zapis new polsowatelya
                    p = open("Пользователи.txt", "a")
                    n = username_entry.get() + "," + password_entry.get() + "\n"
                    p.write(n)

                    window.deiconify()
                    newWindow.destroy()
                else:
                    messagebox.showerror("error", "Некорекный номер телефона")
                    break

    # кнопка отправки формы
    send_btn = Button(newWindow, text='Зарегистрироваться', command=Reg1_clicked)
    send_btn.pack(**base_padding)

    def back():
        newWindow.destroy()
        window.deiconify()
    back_button =Button(newWindow,text = "Назад",command=back)
    back_button.pack()
def Vhod_clicked():
    named = username_entry.get()
    with open("Дальнобойщики.txt","r",encoding="UTF-8") as D:
        textD = D.read().splitlines()
    with open("Мэнеджеры.txt","r",encoding="UTF-8") as M:
        textM = M.read().splitlines()
    with open("Пользователи.txt","r",encoding="UTF-8") as P:
        textP = P.read().splitlines()

    for lines in textD:
        lines = lines.split(",")
        if username_entry.get() == lines[0] and password_entry.get() == lines[1]:
            window.destroy()

            Dalnob = Tk()
            Dalnob.geometry("400x400")
            Dalnob.title("Окно дальнобойщика")

            def zakaz():
                i = -1
                Dalnob.withdraw()
                Zakaz_Dal = Tk()
                Zakaz_Dal.geometry("400x400")
                Zakaz_Dal.title("Выполнение заказа")

                with open("Одобренные заказы.txt", "r", encoding="UTF-8") as f:
                    old_data = f.read()
                    f.seek(0)
                    lines = f.read().splitlines()
                    for line in lines:
                        line = line.split(",")
                        str1 = ",".join(line)
                        i = i + 1
                        if named == line[2]:
                            line[4] = "Принят"
                            break
                    str2 = ",".join(line)
                    new_data = old_data.replace(str1, str2)
                with open(r"Одобренные заказы.txt", "w", encoding="UTF-8") as f:
                    f.write(new_data)

                with open("Одобренные заказы.txt", "r", encoding="UTF-8") as f:
                    lines = f.read().splitlines()
                    for line in lines:
                        line = line.split(",")
                        if named == line[2]:
                            label = Label(Zakaz_Dal, text="Заказ:" + line[0], font=font_header)
                            label.pack(pady=15)
                            status = Label(Zakaz_Dal, text="Теущий статус: " + line[4], font=font_header)
                            status.pack(pady=15)
                            break

                def render(old_str, new_str):
                    with open("Одобренные заказы.txt", "r", encoding="UTF-8") as f:
                        old_data = f.read()
                        newdata = old_data.replace(old_str, new_str)
                    with open("Одобренные заказы.txt", "w", encoding="utf=-8") as f:
                        f.write(newdata)

                def replace(i):
                    with open("Одобренные заказы.txt", "r", encoding="utf-8") as f:
                        text = f.read().splitlines()
                        str = text[i]
                    return str

                def back():
                    Zakaz_Dal.destroy()
                    with open("Дальнобойщики.txt", "r", encoding="UTF-8") as f:
                        old_data = f.read()
                        f.seek(0)
                        text = f.read().splitlines()
                        for lines in text:
                            lines = lines.split(",")
                            if named == lines[0]:
                                str1 = ",".join(lines)
                                lines[3] = "0"
                                str2 = ",".join(lines)
                                newdata = old_data.replace(str1, str2)

                    with open("Дальнобойщики.txt", "w", encoding="utf=-8") as f:
                        f.write(newdata)
                    Dalnob.deiconify()

                def end():
                    status.config(text="Теущий статус: Заказ успешно доставлен")
                    old_str = replace(i)
                    str3 = replace(i).split(",")
                    str3[4] = "Доставлен"
                    render(old_str, ",".join(str3))

                    button_step.config(text="На главную", command=back)

                def next():
                    status.config(text="Теущий статус: В пути")
                    old_str = replace(i)
                    str3 = replace(i).split(",")
                    str3[4] = "В пути"
                    render(old_str, ",".join(str3))

                    button_step.config(text="Доставлен", command=end)

                def step():
                    status.config(text="Теущий статус: Погрузка")
                    old_str = replace(i)
                    str3 = replace(i).split(",")
                    str3[4] = "Погрузка"
                    render(old_str, ",".join(str3))

                    button_step.config(text="В путь", command=next)

                button_step = Button(Zakaz_Dal, text="Погрузка", command=step, font=font_header)
                button_step.pack(pady=15)

            button_zakaz = Button(Dalnob, text="Начать выполнение", command=zakaz, font=font_header)

            label = Label(Dalnob, font=font_header)
            label.pack()
            with open("Одобренные заказы.txt", "r", encoding="UTF-8") as f:
                text = f.read().splitlines()
            for lines in text:
                lines = lines.split(",")
                if named == lines[2] and lines[4] != "Доставлен":
                    label.config(text="Вам поступил заказ:" + lines[0], bg="lightgreen")
                    label.pack()
                    button_zakaz["state"] = "normal"
                    break
                else:
                    label.config(text="Нет заказов")
                    button_zakaz["state"] = "disabled"

                status = lines[4]
            button_zakaz.pack(pady=15)

            def view():
                Dalnob.withdraw()
                view_Dal = Tk()
                view_Dal.geometry("400x400")
                view_Dal.title("Просмотр заказов")
                label = Label(view_Dal, text="Ваши заказы", font=font_header)
                label.pack()

                with open("Одобренные заказы.txt", "r", encoding="UTF-8") as f:
                    r = f.read().splitlines()
                list_zakaz = Listbox(view_Dal, width=34)
                list_zakaz.pack()
                for lines in r:
                    lines = lines.split(",")
                    if lines[4] == "Доставлен":
                        list_zakaz.insert(END,lines[0])

                def back():
                    view_Dal.destroy()
                    Dalnob.deiconify()

                button_back = Button(view_Dal, text="Назад", command=back)
                button_back.pack(pady=15)

            button_sm = Button(Dalnob, text="Просмотр звказов", command=view, font=font_header)
            button_sm.pack()

            Dalnob.mainloop()

    for lines in textM:
        lines = lines.split(",")
        if username_entry.get() == lines[0] and password_entry.get() == lines[1]:
            window.destroy()

            Menager = Tk()
            Menager.geometry("400x300")
            Menager.title("Окно менеджера")

            def okno_zak(x):
                check = ' '.join(lb.get(ANCHOR))
                if check == " ":
                    tkinter.messagebox.showinfo("Ошибка", "Выберите работника")
                else:
                    Menager.withdraw()
                    naznac = Tk()
                    naznac.geometry("500x50")
                    naznac.title("Выбор работника")

                    def reg_zak():
                        c = combobox.get()
                        z = ''.join(lb.get(ANCHOR))
                        with open("Одобренные заказы.txt", "a", encoding="UTF-8") as op_file:
                            op_file.write(z)
                            op_file.write(",")
                            op_file.write(c)
                            op_file.write(",")
                            op_file.write("Одобрен")
                            op_file.write("\n")


                        seach = combobox.get()
                        with open("Дальнобойщики.txt", "r", encoding="UTF-8") as f_o:
                            r = f_o.read()
                            f_o.seek(0)
                            lines = f_o.read().splitlines()
                            for line in lines:
                                line = line.split(",")
                                str = ",".join(line)
                                if line[3] != "1":
                                    n = line[0] + "," + line[2]
                                    if n == seach:
                                        line[3] = "1"
                                        break

                            str1 = ",".join(line)
                            daedalus = r.replace(str, str1)

                        with open(r"Дальнобойщики.txt", "w", encoding="UTF-8") as f_o:
                            f_o.write(daedalus)

                        naznac.destroy()
                        Menager.deiconify()

                soz_btn = Button(naznac, text="Создать заказ", command=reg_zak)
                soz_btn.pack(side=BOTTOM)

                m = ' '.join(lb.get(ANCHOR))

                label = Label(naznac, text=m)
                label.pack(side=LEFT, anchor=NW)

                def rabotniki():
                    m = []
                    with open("Дальнобойщики.txt", "r", encoding="UTF-8") as d:
                        r1 = d.read().splitlines()
                    for lines in r1:
                        lines = lines.split(",")
                        if lines[3] == "0":
                            n = [lines[0] + "," + lines[2]]
                            m.append(n[0])
                            n = []

                    return m

                var = StringVar()
                combobox = ttk.Combobox(naznac, width=150, height=60, textvariable=var)
                combobox['values'] = rabotniki()
                combobox['state'] = 'readonly'
                combobox.pack(side=LEFT, anchor=NE)

                naznac.mainloop()

            with open("Одобренные заказы.txt", "r", encoding="UTF-8") as m1:
                r = m1.read().splitlines()
            lb = Listbox(Menager, width=34)
            lb.pack()

            for lines in r:
                lines = lines.split(",")
                if lines[4] == "На рассмотрении":
                    n = [lines[0] + "," + lines[1]]
                    lb.insert(END, n)

            lb.bind('<Double-Button>', okno_zak)



            Menager.mainloop()

    for lines in textP:
        lines = lines.split(",")
        if username_entry.get() == lines[0] and password_entry.get() == lines[1]:
            window.destroy()
            Polzovatel = Tk()
            Polzovatel.geometry("400x400")
            Polzovatel.title("Окно пользователя")

            def Soz_Zak():
                Polzovatel.withdraw()
                Sozdanie_zakaza = Tk()
                Sozdanie_zakaza.geometry("400x400")
                Sozdanie_zakaza.title("Окно создания закказа")

                def Goroda():
                    with open("Города.txt", "r", encoding='utf-8') as g:
                        goroda = g.read().splitlines()
                    return goroda

                Lab_gor = Label(Sozdanie_zakaza,text =  "Выберите город отправки",**base_padding)
                Lab_gor.pack()

                var = StringVar()
                combobox = ttk.Combobox(Sozdanie_zakaza,width=150,height=60, textvariable=var)
                combobox['values'] = Goroda()
                combobox['state'] = 'readonly'
                combobox.pack(**base_padding)


                Lab_gor1 = Label(Sozdanie_zakaza,text= "Выберите город доставки",**base_padding)
                Lab_gor1.pack()

                var1 = StringVar()
                combobox1 = ttk.Combobox(Sozdanie_zakaza,width=150,height=60, textvariable=var1)
                m = Goroda()
                def remuve_s(event):
                    p = combobox.get()
                    for i in m:
                        if combobox.get() == i:
                            m.remove(i)
                            break
                    combobox1['values'] = m
                    combobox1['state'] = 'readonly'

                combobox1.bind("<Enter>", remuve_s)
                combobox1.pack(**base_padding)

                def Soz_Zak1():
                    z = open("Одобренные заказы.txt","a", encoding="UTF-8")
                    z.write(combobox.get() + "-" + combobox1.get() + "," + named + "," + " "+ "," + " " + ","+ "На рассмотрении" + "\n")
                    Polzovatel.deiconify()
                    Sozdanie_zakaza.destroy()

                Soz_zak1 = Button(Sozdanie_zakaza, text="Создать заказ", command=Soz_Zak1)
                Soz_zak1.pack(**base_padding)

                def back():
                    Sozdanie_zakaza.destroy()
                    Polzovatel.deiconify()

                back_botton = Button(Sozdanie_zakaza,text = "Назад", command=back)
                back_botton.pack()
                Sozdanie_zakaza.mainloop()

            Soz_zak = Button(Polzovatel, text="Создать заказ", command=Soz_Zak)
            Soz_zak.pack(**base_padding)

            def Prosmotr():
                Polzovatel.deiconify()

                Zakaz = Tk()
                Zakaz.geometry("400x400")
                Zakaz.title("Заказы")

                lbl = Label(Zakaz,text = "Ваши заказы",**base_padding)
                lbl.pack()
                list_zakaz = Listbox(Zakaz, width=34)
                list_zakaz.pack()
                status = Label(Zakaz)
                status.pack(side=LEFT, anchor=NE)
                with open("Одобренные заказы.txt","r", encoding="UTF-8") as order:
                    text = order.read().splitlines()


                for lines in text:
                    lines = lines.split(",")
                    if lines[1] == named:
                        list_zakaz.insert(END, lines[0] + " , " + lines[4])


                def back():
                    Zakaz.destroy()
                    Polzovatel.deiconify()

                back_botton = Button(Zakaz,text = "Назад", command=back)
                back_botton.pack()
            Prosmotr_zak = Button(Polzovatel, text = "Просмотреть заказы", command=Prosmotr)
            Prosmotr_zak.pack(**base_padding)

            Polzovatel.mainloop()


main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Войти', command=Vhod_clicked)
send_btn.pack(**base_padding)

#кнопка регистрации
reg_btn = Button(window,text = "Или зарегистрируйтесь",command = Reg_clicked)
reg_btn.pack(**base_padding)


# запускаем главный цикл окна
window.mainloop()

