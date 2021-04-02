#!/usr/bin/env python
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
import runpy
import webbrowser
import os

widget    = []
geometry  = []
root1     = []

l = 0
e = 0
b = 0
t = 0
s = 0

r_var = 0
ra= 0

comb = 0

language = None
lang     = None

ua = ('текст',"рядок","стовпчик","колір фону","колір тексту","шрифт","його розмір","ширина:","висота:","код функції","функція","ДОПОМОГА","ЗБЕРЕГТИ","КНОПКА","ТЕКСТ мітка","ТЕКСТ рядок","ТЕКСТ поле","ТП з прокруткою","ЗАФІКСУВАТИ","Заповнить собою","ВІКНО:", "ВІДЖЕТ:","ТЕСТ","заголовок","рельєф","Лише для кнопок:","залити:",'ТЕКСТ викидний',"ОЧИСТИТИ", "мова:","Витріть, 4 відступи ...","Радіо КНОПКА","тип даних:","РадіоКфункція","#активуємо в потрібному рядку","Пайтон файли","Всі типи файлів","#об'єкт головного вікна","#заголовок вікна","#розміри вікна","#фіксація розмірів вікна","#створюємо текстову мітку","#створюємо текстове поле вводу","#створюємо текстове поле вибору з прокруткою","#стандартний варіант вибору","#створюємо текстове поле вводу"," ","#функція для сокупності радіо-кнопок","#створюємо радіо-кнопоку","#створюємо текстове поле вводу","#створюємо текстове поле вводу з прокруткою","#імпортуємо модуль tkinter","САЙТ","ЛІЦЕНЗІЯ")
ru = ('текст',"строка","столбик", "цвет фона", "цвет текста","шрифт","его размер", "ширина:","высота:","код функции","функция", "ПОМОЩЬ",  "СОХРАНИТЬ","КНОПКА","ТЕКСТ метка","ТЕКСТ строка","ТЕКСТ поле","ТП с прокруткой","ЗАФИКСИРОВАТЬ","Заполнит собой", "ОКНО",   "ВИДЖЕТ:","ТЕСТ","заглавие","рельеф","Только для кнопок:","залить:",'ТЕКСТ выкидной',"ОЧИСТИТЬ", "язык:","Сотри, 4 отступа ...","Радио КНОПКА","тип данных:","РадиоКфункця","#активируем в нужной строке","Пайтон файлы","Все типы файлов","#объект главного окна","#заглавие окна","#размеры окна","#Фиксация размеров окна","#создаем текстовую метку", "#создаем текстовое поле ввода","#создаем текстовое поле выбора с прокруткой","#стандартный вариант выбора","#создаем текстовое поле ввода","#создаем функцию","#функция для сокупности радио-кнопок","#создаем радио-кнопоку",  "#создаем текстовое поле ввода","#создаем текстовое поле ввода с прокруткой","#импортируем модуль tkinter","САЙТ","ЛИЦЕНЗИЯ")
en = ('text',"row","column","background","foreground","font","font size","width:","height:","function code","function","HELP","SAVE","BUTTON","LABEL","ENTRY","TEXT","ScrolledText","TO FIX","to fill","WINDOW:","WIDDGET:","TEST","title","relief","For buttons only:","flood:",'COMBOBOX',"CLEAN","language:","Wipe it, 4 indents ...", "Radio Button", "data type:", "RadioBfunction","#activate in the desired line","Python files","All file types","#main window object","#title name","#window sizes","#fixing window sizes","#create a text label","#create a text input field","#create a text selection box with scrolling","#standard choice","#create a text input field","#create a feature","#function for a set of radio buttons","#create a radio button","#create a text input field","#create a text input field with scrolling" ,"#import TKINTER module","THE SITE","LICENSE")

try:
    file = open('WCTk_config.txt', 'r', encoding='UTF-8')
    language = file.read()
    file.close()
    lang = language
except:
    file = open('WCTk_config.txt', 'w', encoding='UTF-8')
    file.write("en")
    file.close()
    language = file.read()
    file.close()
    lang = language
if language == "en":
   language = en
elif language == "ru":
   language = ru
elif language == "ua":
   language = ua
comment = None

module    = [f"""from tkinter import * {language[51]}
"""]

def language_selection():
    global language
    global lang
    file = open('WCTk_config.txt', 'w', encoding='UTF-8')
    file.write(str(c6.get()))
    file.close()
    file = open('WCTk_config.txt', 'r', encoding='UTF-8')
    language = file.read()
    file.close()
    print(language)
    if lang == "en":
        messagebox.showinfo('Information', """To change the language Reboot program""")
    elif lang == "ru":
        messagebox.showinfo('Информация', """Для изменения языка перезагрузите программу""")
    elif lang == "ua":
        messagebox.showinfo('Інформація', """Для зміни мови перезавантажте програму""")
        
def write1():
    global root1
    global widget
    global geometry
    global module
    global language
    
    if not widget:
        error3()
        clear()
    else:
        file_name = fd.asksaveasfilename(filetypes=((language[35], "*.py"),(language[36], "*.*")))
        file_name = file_name + ".py"

        geometry.append("""

root.mainloop()""")

        f = open(file_name, 'w', encoding='UTF-8')
        f.writelines(module)
        f.writelines(root1)
        f.writelines(widget)
        f.writelines(geometry)
        f.close()

def test():
    global root1
    global widget
    global geometry
    
    geometry1 = ["""
root.mainloop()"""]
    
    p = ["""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""]
    if not widget:
        error3()
    else:
        f = open('testGUI.py', 'w', encoding='UTF-8')
        f.writelines(p)
        f.writelines(module)
        f.writelines(root1)
        f.writelines(widget)
        f.writelines(geometry)
        f.writelines(geometry1)
        f.close()

        runpy.run_path(path_name="testGUI.py")
    
def window1():
    clear()
    global widget
    global language
    
    title      = e1.get()
    background = c5.get()
    relief     = c1.get()
    w = f"""
root = Tk () {language[37]}
root.title('{title}') {language[38]}
#root.geometry("270x220") {language[39]}
#root.resizable(width=False, height=False) {language[40]}
root.config(background='{background}', relief={relief})

"""
    widget.append(w)
    e1.delete(0, END)

def label():
    global widget
    global geometry
    global l
    global language

    text       = e2.get()
    row        = e3.get()
    column     = e4.get()
    background = c3.get()
    foreground = c4.get()
    font       = c2.get()
    size       = e5.get()

    width      = e9.get()
    height     = e10.get()
    rowspan    = e7.get()
    rowspan    = str(rowspan)
    columnspan = e8.get()
    columnspan = str(columnspan)
       
    if row == "" or column == "":
        error1()
    else:
        l = int(l+1)
        r = ""
        c = ""
        if  rowspan == "":
            r = ""
        else:
            r = f",rowspan={rowspan}"
        if columnspan == "":
            c = ""
        else:
            c = f",columnspan={columnspan}"
        h = ""
        if  height == "":
            h = ""
        else:
            h = f",height={height}" 
        w = f"""
l{l} = Label(root,width={width}{h},background='{background}', foreground="{foreground}",text='{text}',font='{font} {size}',anchor="w") {language[41]}"""
        g = f"""
l{l}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""
        
        widget.append(w)
        geometry.append(g) 

        e8.delete(0, END)
        e7.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

def entry():
    global widget
    global geometry
    global e
    global language
    
    row        = e3.get()
    column     = e4.get()
    background = c3.get()
    foreground = c4.get()
    font       = c2.get()
    size       = e5.get()
    width      = e9.get()
    height     = e10.get()
    rowspan    = e7.get()
    rowspan    = str(rowspan)
    columnspan = e8.get()
    columnspan = str(columnspan)
       
    if row == "" or column == "":
        error1()
    else:
        e = int(e+1)
        r = ""
        c = ""
        if  rowspan == "":
            r = ""
        else:
            r = f",rowspan={rowspan}"
        if columnspan == "":
            c = ""
        else:
            c = f",columnspan={columnspan}"
        h = ""
        if  height == "":
            h = ""
        else:
            h = f",height={height}"     
        w = f"""
e{e} = Entry(root,width={width}{h},background='{background}',foreground="{foreground}",font='{font} {size}') {language[42]}"""
        g = f"""
e{e}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""

        widget.append(w)
        geometry.append(g) 

        e8.delete(0, END)
        e7.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        
def combobox():
    global widget
    global geometry
    global comb
    global module
    global language
    
    text       = e2.get()
    row        = e3.get()
    column     = e4.get()
    background = c3.get()
    foreground = c4.get()
    font       = c2.get()             
    size       = e5.get()             
    width      = e9.get()             
    height     = e10.get()            
    rowspan    = e7.get()             
    rowspan    = str(rowspan)         
    columnspan = e8.get()             
    columnspan = str(columnspan)      

    if row == "" or column == "":
        error1()
    else:
        if text == "":
            error4()
        else:
            c = int(e+1)
            r = ""
            c = ""
            if  rowspan == "":
                r = ""
            else:
                r = f",rowspan={rowspan}"
            if columnspan == "":
                c = ""
            else:
                c = f",columnspan={columnspan}"
            h = ""
            if  height == "":
                h = ""
            else:
                h = f",height={height}"     
            w = f"""
c{comb} = Combobox(root,width={width}{h},background='{background}', foreground="{foreground}",font='{font} {size}') {language[43]}
c{comb}['values'] = ({text})
c{comb}.current(0) {language[44]}"""
            g = f"""
c{comb}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""
            m = f"""
from tkinter.ttk import Combobox"""

            widget.append(w)
            geometry.append(g) 
            module.append(m)

            e8.delete(0, END)         
            e7.delete(0, END)         
            e2.delete(0, END)         
            e3.delete(0, END)         
            e4.delete(0, END)         

def button():                         
    global widget                     
    global geometry                   
    global root1                      
    global b                          
    global language
    
    text       = e2.get()             
    row        = e3.get()             
    column     = e4.get()             
    background = c3.get()             
    foreground = c4.get()             
    function   = txt.get(1.0, END)
    font       = c2.get()             
    size       = e5.get()             
    command    = e6.get()             
    width      = e9.get()
    height     = e10.get()
    rowspan    = e7.get()
    rowspan    = str(rowspan)
    columnspan = e8.get()
    columnspan = str(columnspan)

    if row == "" or column == "":
        error1()
    else:
        if command == "" or function == "":
            error2()
        else:
            b = int(b+1)               
            r = ""
            c = ""
            if  rowspan == "":         
                r = ""
            else:                      
                r = f",rowspan={rowspan}"
            if columnspan == "":       
                c = ""
            else:                      
                c = f",columnspan={columnspan}"
            h = ""                     
            if  height == "":
                h = ""
            else:                      
                h = f",height={height}"
            f = f"""
def {command}(): {language[46]}
{function}
"""    
            w = f"""
b{b} = Button(root,width={width}{h},background='{background}', foreground="{foreground}",text='{text}',font='{font} {size}') {language[45]}
b{b}.config(command={command})"""
            g = f"""
b{b}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""

            root1.append(f)
            widget.append(w)
            geometry.append(g) 

            e8.delete(0, END)          
            e7.delete(0, END)          
            e2.delete(0, END)          
            e3.delete(0, END)          
            e4.delete(0, END)          
            e7.delete(0, END)          
            e6.delete(0, END)          
            e8.delete(0, END)          
            txt.delete(1.0, END)                  
            txt.insert(INSERT, language[30])

def rBf():                           
    global widget                    
    global r_var                          
    global language

    r_var = int(r_var+1)                     
    data_type  = c7.get()
    rB_f = f"""
r_var{r_var} = {data_type} {language[47]}
r_var{r_var}.set(0)"""
    widget.append(rB_f)
        
def radioB():                        
    global widget                    
    global geometry                  
    global ra                        
    global language

    text       = e2.get()            
    row        = e3.get()            
    column     = e4.get()            
    background = c3.get()            
    foreground = c4.get()            
    font       = c2.get()            
    size       = e5.get()            
    width      = e9.get()
    height     = e10.get()
    rowspan    = e7.get()
    rowspan    = str(rowspan)
    columnspan = e8.get()
    columnspan = str(columnspan)

    if row == "" or column == "":
        error1()
    else:
        ra = int(ra+1)                     
        r = ""
        c = ""
        if  rowspan == "":            
            r = ""
        else:                         
            r = f",rowspan={rowspan}"
        if columnspan == "":          
            c = ""
        else:                         
            c = f",columnspan={columnspan}"
        h = ""                        
        if  height == "":
            h = ""
        else:                         
            h = f",height={height}" 
        w = f"""
ra{ra} = Radiobutton(root,width={width}{h},background='{background}', foreground="{foreground}",text='{text}',font='{font} {size}',anchor="w") {language[48]}"""
        g = f"""
ra{ra}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""
        
        widget.append(w)
        geometry.append(g) 

        e8.delete(0, END)             
        e7.delete(0, END)             
        e2.delete(0, END)             
        e3.delete(0, END)             
        e4.delete(0, END)             
        
def text():                            
    global widget                      
    global geometry                    
    global t                           
    global language

    row        = e3.get()              
    column     = e4.get()              
    background = c3.get()              
    foreground = c4.get()              
    font       = c2.get()              
    size       = e5.get()              
    width      = e9.get()              
    height     = e10.get()             
    rowspan    = e7.get()              
    rowspan    = str(rowspan)          
    columnspan = e8.get()              
    columnspan = str(columnspan)       

    if row == "" or column == "":
        error1()
    else:
        t = int(t+1)
        r = ""
        c = ""
        if  rowspan == "":             
            r = ""
        else:                          
            r = f",rowspan={rowspan}"
        if columnspan == "":           
            c = ""
        else:                          
            c = f",columnspan={columnspan}"
        h = ""                         
        if  height == "":
            h = ",height=5"
        else:                          
            h = f",height={height}" 
        w = f"""
t{t} = Text(root,width={width}{h},background='{background}', foreground="{foreground}",font='{font} {size}') {language[49]}
"""
        g = f"""
t{t}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""

        widget.append(w)
        geometry.append(g) 

        e8.delete(0, END)              
        e7.delete(0, END)              
        e2.delete(0, END)              
        e3.delete(0, END)              
        e4.delete(0, END)              

def scrolledT():                       
    global widget                      
    global geometry                    
    global s                           
    global module                      
    global language

    row        = e3.get()              
    column     = e4.get()              
    background = c3.get()              
    foreground = c4.get()              
    font       = c2.get()              
    size       = e5.get()              
    width      = e9.get()              
    height     = e10.get()             
    rowspan    = e7.get()              
    rowspan    = str(rowspan)          
    columnspan = e8.get()              
    columnspan = str(columnspan)       

    if row == "" or column == "":
        error1()
    else:
        r = ""
        c = ""
        s = int(s+1)
        if  rowspan == "":             
            r = ""
        else:                          
            r = f",rowspan={rowspan}"
        if columnspan == "":           
            c = ""
        else:                          
            c = f",columnspan={columnspan}"
        h = ""                         
        if  height == "":
            h = ",height=5"
        else:                          
            h = f",height={height}" 
        w = f"""
s{s} = scrolledtext.ScrolledText(root,width={width}{h},background='{background}', foreground="{foreground}",font='{font} {size}') {language[50]}
"""
        g = f"""
s{s}.grid(row={row}{r},column={column}{c},sticky=N+S+W+E) {language[34]}"""
        m = f"""
from tkinter import scrolledtext"""
        
        widget.append(w)
        geometry.append(g)
        module.append(m)

        e8.delete(0, END)               
        e7.delete(0, END)               
        e2.delete(0, END)               
        e3.delete(0, END)               
        e4.delete(0, END)               

def help():
    cycle()
    global lang
    if lang == "en":
        messagebox.showinfo('Information about the program', """Widget Creator TK - A simple program to create GUI for Python, based on Tkinter for educational purposes. Is credited under the GPL3 distribution license.
    To create a GUI, fill in the box fields, click "Fix". Then enter the coordinate facility and other parameters you want, then press to create the desired button, such as "Button". Similarly, create other widgets. To view GUI before saving, click "Test" to save "Save", to clear "Clear". There is a "secret", when you click on the "Help" button, while this window opens on the main window, the colors and the font are changed to those that you have chosen (pull back this window).
    For the work of this program, Python 3 must be installed.

    Copyright (c) 2021 Snitko Dmytro Mykolayovych
    Help this application: 5168 7573 5185 9691
    On altruism is far from going to ( 
                         
                GNU GENERAL PUBLIC LICENSE
                      Version 3, 29 June 2007""")
    elif lang == "ru":
        messagebox.showinfo('Информация о программе', """Widget Creator Tk - простая программа для создания GUI для Python, созданная на базе Tkinter для учебных целей. Распростроняется под лицензией распространения GPL3.
    Для создания GUI сначала заполните поля "ОКНО", нажмите "ЗАФИКСИРОВАТЬ". Затем вводите для каждого объекта координаты и другие нужные параметры, после чего нажмите для их создания нужную кнопку, например "КНОПКА". Аналогично создавайте другие виджеты. Для просмотра GUI перед сохранением нажмите "ТЕСТ", для сохранения "СОХРАНИТЬ", для полного очищещення "очистить". Есть «пасхалка», при нажатии на кнопку "ПОМОЩЬ" пока это окно открыто на главном окне меняются цвета и шрифт на выбранные Вами (оттяните это окно).
    Думаю понятно, что для работы этой программы на ПК должен стоять Python3. 

    Copyright (c) 2021 Снитко Дмитрий Николаевич
    помочь развитию программы: 5168 7573 5185 9691
    на голом энтузиазме далеко не заеду (
                         
                GNU GENERAL PUBLIC LICENSE
                      Version 3, 29 June 2007""")
    elif lang == "ua":
        messagebox.showinfo('Інформація про програму', """Widget Creator Tk - проста програма для створення GUI для Python, створена на базі Tkinter для навчальних цілей. Росповсюджується під ліцензією розповсюдження GPL3.
    Для створення GUI спершу заповніть поля "ВІКНО", натисніть "ЗАФІКСУВАТИ". Потім вводьте для кожного об'єкта координати і інші потрібні параметри, після чого натискайте для їх створення потрібну кнопку, наприклад "КНОПКА". Аналогічно створюйте інші віджети. Для перегляду GUI перед збереженням натисніть "ТЕСТ", Для збереження "ЗБЕРЕГТИ", для повного очищення "ОЧИСТИТИ". Є «пасхалка», при натисненні на кнопку "ДОПОМОГА" поки це вікно відкрите на головному вікні змінються кольори й шрифт на ті, що обрали ВИ (відтягніть це вікно).
    Гадаю зрозуміло що для роботи цієї програми на ПК має стояти Python3.

    Copyright (c) 2021 Снітко Дмитро Миколайович
    допомогти розвитку програми: 5168 7573 5185 9691
    на голому ентузіазмі далеко не заїду(
                         
                GNU GENERAL PUBLIC LICENSE
                    Version 3, 29 June 2007""")
        
    l8.config(background='snow')
    l9.config(foreground='black')
    l2.config(background='snow')
    l10.config(font='Arial 12')
    
def clear():
    global language
    global root1                         
    global widget                        
    global geometry                      
    global module                        
    global l                             
    global e                             
    global b                             
    global t                             
    global s                             
    global comb                          
    e1.delete(0, END)                    
    e2.delete(0, END)                        
    e3.delete(0, END)                    
    e4.delete(0, END)                    
    e5.delete(0, END)                    
    e5.insert(0, "10") 
    e6.delete(0, END)                    
    e7.delete(0, END)                    
    e8.delete(0, END)                    
    e9.delete(0, END)                    
    e9.insert(0, "10")
    e10.delete(0, END)                   
    txt.delete(1.0, END)                  
    txt.insert(INSERT, language[30])
    root1.clear()                               
    widget.clear()                        
    geometry.clear()                      
    module.clear()                       
    l = 0
    e = 0
    b = 0
    t = 0
    s = 0
    comb = 0
    module    = [f"""from tkinter import * {language[51]}
"""]
    l8.config(background='snow')
    l9.config(foreground='black')
    l2.config(background='snow')
    l10.config(font='Arial 12')
    c1.current(4)
    c2.current(0)
    c3.current(2)
    c4.current(0)
    c5.current(2)
    
def error1():                           
    global lang
    if lang == "en":
        messagebox.showerror('Error', """INDICATE THE COORDINATES OF THE FULL ITEM!
                    (row, column)""")
    elif lang == "ru":
        messagebox.showerror('Ошибка', """УКАЖИТЕ КООРДИНАТЫ спавна ЭЛЕМЕНТА!
                    (Строка, столбец)""")
    elif lang == "ua":
        messagebox.showerror('Помилка', """ВКАЖІТЬ КООРДИНАТИ СПАВНУ ЕЛЕМЕНТА!
                    (рядок, стовпчик)""")
    
def error2():                           
    global lang
    if lang == "en":
        messagebox.showerror('Error', """НАПИШІТЬ КНОПЦІ ФУНКЦІЮ ТА ЇЇ КОД!
                    (потім можна відредагувати вручну)""")
    elif lang == "ru":
        messagebox.showerror('Ошибка', """НАПИШИТЕ кнопке ФУНКЦЫЮ и ее КОД!
                    (Потом можно отредактировать вручную)""")
    elif lang == "ua":
        messagebox.showerror('Помилка', """WRITE THE FUNCTION BUTTON AND ITS CODE!
                    (can then be edited manually)""")

    
def error3():                           
    global lang
    if lang == "en":
        messagebox.showerror('Error', """MAIN WINDOW PARAMETERS ARE MISSING!
            Specify them and click 'FIX'.
And after that, create all the other elements!""")
    if lang == "ru":
        messagebox.showerror('Ошибка', """ОТСУТСТВУЕТ ОСНОВНЫЕ ПАРАМЕТРЫ ОКНА!
            Укажите их, и нажмите "ЗАФИКСИРОВАТЬ".
И уже после этого создавайте все остальные элементы!""")
    if lang == "ua":
        messagebox.showerror('Помилка', """ВІДСУТНІ ОСНОВНІ ПАРАМЕТРИ ВІКНА!
            Вкажіть їх, й натисніть 'ЗАФІКСУВАТИ'.
І вже після цього створюйте всі інші елементи!""")
   


def error4():                           
    global lang
    if lang == "en":
        messagebox.showerror('Error', """TO CREATE A FIELD WITH DISCHARGE TEXT FOR SELECTION, CREATE SELECTION OPTIONS!
    Write in the text box the choices in commas in quotation marks.
    Example: 'FLAT', 'GROOVE', 'RIDGE', 'SUNKEN', 'RAISED'""")
    if lang == "ru":
        messagebox.showerror('Ошибка', """ДЛЯ СОЗДАНИЯ ПОЛЯ С выкидыша текста ВЫБОРА СОЗДАЙТЕ ВАРИАНТЫ ВЫБОРА!
    Пишите в текстовое поле варианты выбора через запятую в кавычках.
    Пример: "FLAT", "GROOVE", "RIDGE", "SUNKEN", "RAISED'""")
    if lang == "ua":
        messagebox.showerror('Помилка', """ДЛЯ СТВОРЕННЯ ПОЛЯ З ВИКИДНИМ ТЕКСТОМ ДЛЯ ВИБОРУ СТВОРІТЬ ВАРІАНТИ ВИБОРУ!
    Пишіть в текстове поле варіанти вибору через кому в лапках. 
    Приклад:'FLAT', 'GROOVE', 'RIDGE', 'SUNKEN', 'RAISED'""")
    
def cycle():
    l8.config(background=str(c3.get()))
    l9.config(foreground=str(c4.get()))
    l2.config(background=str(c5.get()))
    l10.config(font=str(c2.get()))
    
def site1():
    webbrowser.open("https://sites.google.com/teacher.rv.ua/widget-creator-tk")

root = Tk ()
root.title('Widget Creator Tk')
#root.geometry("270x220")
#root.resizable(width=False, height=False)
root.config(background='snow', relief=RAISED)
root.option_add ('*Dialog.msg.font', 'Arial 8')
root.option_add ('*Dialog.msg.geometry', '60')      

def gpl():
    fileName = "GPL3-license.txt"
    os.system("start " + fileName)
    
l0 = Label(root,background='snow',text=language[20],font='Arial 12')
l1 = Label(root,width=10,background='snow',text=language[23],font='Arial 12',anchor="w")
e1 = Entry(root,width=10,background='white',font='Arial 15')
l2 = Label(root,width=10,background='snow',text=language[3],font='Arial 12',anchor="w")
c5 = Entry(root,width=10,background='white',font='Arial 15') 
l3 = Label(root,width=10,background='snow',text=language[24],font='Arial 12',anchor="w")
l4 = Label(root,width=10,background='snow',text=language[21],font='Arial 12')
l5 = Label(root,width=10,background='snow',text=language[0],font='Arial 12',anchor="w")
e2 = Entry(root,width=10,background='white',font='Arial 15')
l6 = Label(root,width=10,background='snow',text=language[1],font='Arial 12',anchor="w")
e3 = Entry(root,width=10,background='white',font='Arial 15')
l7 = Label(root,width=10,background='snow',text=language[2],font='Arial 12',anchor="w")
e4 = Entry(root,width=10,background='white',font='Arial 15')
l8 = Label(root,width=10,background='snow',text=language[3],font='Arial 12',anchor="w")
l9 = Label(root,width=10,background='snow',text=language[4],font='Arial 12',anchor="w")
l10 = Label(root,width=10,background='snow',text=language[5],font='Arial 12',anchor="w")
l11 = Label(root,width=10,background='snow',text=language[6],font='Arial 12',anchor="w")
e5 = Entry(root,width=3,background='white',font='Arial 15')
e5.insert(0, "10") 
e6 = Entry(root,width=10,background='white',font='Arial 15')
l14 = Label(root,width=10,background='snow',text=language[26],font='Arial 12',anchor="w")
e7 = Entry(root,width=3,background='white',font='Arial 15')
e8 = Entry(root,width=3,background='white',font='Arial 15')
l15 = Label(root,width=10,background='snow',text=language[7],font='Arial 12',anchor="w")
e9 = Entry(root,width=3,background='white',font='Arial 15')
e9.insert(0, "10")    
l16 = Label(root,width=10,background='snow',text=language[8],font='Arial 12',anchor="w")
e10 = Entry(root,width=3,background='white',font='Arial 15')
l12 = Label(root,width=10,background='snow',text=language[10],font='Arial 12',anchor="w")
l12_1 = Label(root,width=25,background='snow',text=language[25],font='Arial 12')
l13 = Label(root,width=10,background='snow',text=language[9],font='Arial 12',anchor="w")
txt = scrolledtext.ScrolledText(root,width=10,height=10,background="white")
l17 = Label(root,width=10,background='snow',text=language[29],font='Arial 12',anchor="w")
txt.delete(1.0, END)                                           
txt.insert(INSERT, language[30])
l18 = Label(root,width=10,background='snow',text=language[32],font='Arial 12',anchor="w")
b1 = Button(root,width=8,background='lavender',text=language[18])
b1.config(command=window1) 
b2 = Button(root,width=10,background='lavender',text=language[14])
b2.config(command=label) 
b3 = Button(root,width=10,background='lavender',text=language[15])
b3.config(command=entry)
b4 = Button(root,width=10,background='lavender',text=language[13])
b4.config(command=button)
b5 = Button(root,width=10,background='snow4',text=language[12],foreground='white')
b5.config(command=write1)
b6 = Button(root,width=10,background='lavender',text=language[16])
b6.config(command=text)
b7 = Button(root,width=10,background='lavender',text=language[27])
b7.config(command=combobox)
b8 = Button(root,width=10,background='lavender',text=language[17])
b8.config(command=scrolledT)
b9 = Button(root,width=10,background='snow4',text=language[22],foreground='white')
b9.config(command=test)
b10 = Button(root,width=10,background='snow4',text=language[28],foreground='white')
b10.config(command=clear)
b11 = Button(root,width=10,background='lavender',text=language[11])
b11.config(command=help)
b12 = Button(root,width=10,background='lavender',text="ОК")
b12.config(command=language_selection)
b13 = Button(root,width=10,background='lavender',text=language[31])
b13.config(command=radioB)
b14 = Button(root,width=10,background='lavender',text=language[33])
b14.config(command=rBf)
b15 = Button(root,width=10,background='lavender',text=language[52])
b15.config(command=site1)
b16 = Button(root,width=10,background='lavender',text=language[53])
b16.config(command=gpl)
c1 = Combobox(root,width=8,background='white',font='Arial 15')
c1['values'] = ("FLAT", "GROOVE", "RIDGE", "SUNKEN", "RAISED")  
c1.current(4)
c2 = Combobox(root,width=8,background='white',font='Arial 15')
c2['values'] = ("Arial", "Book antiqua", "Garamond", "Georgia", "Trebushet", "Century gothic", "Consolas", "Lucida sans unicode", "Verdana", "Tahoma", "Courier new", "Lucida console", "Comic sans ms", "впишіть інший")  
c2.current(0)
colors = ('black','white','snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhitc5','AntiqueWhite3', 'AntiqueWhite2', 'bisquc5', 'bisque3', 'bisque2', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhitc5', 'NavajoWhite3', 'NavajoWhite2','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRosc5', 'MistyRose3','MistyRose2', 'azurc5', 'azure3', 'azure2', 'SlateBlue1', 'SlateBluc5', 'SlateBlue3','SlateBlue2', 'RoyalBlue1', 'RoyalBluc5', 'RoyalBlue3', 'RoyalBlue2', 'bluc5', 'blue2','DodgerBluc5', 'DodgerBlue3', 'DodgerBlue2', 'SteelBlue1', 'SteelBluc5','SteelBlue3', 'SteelBlue2', 'DeepSkyBluc5', 'DeepSkyBlue3', 'DeepSkyBlue2','SkyBlue1', 'SkyBluc5', 'SkyBlue3', 'SkyBlue2', 'LightSkyBlue1', 'LightSkyBluc5','LightSkyBlue3', 'LightSkyBlue2', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBluc5', 'LightSteelBlue3','LightSteelBlue2', 'LightBlue1', 'LightBluc5', 'LightBlue3', 'LightBlue2','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoisc5','PaleTurquoise3', 'PaleTurquoise2', 'CadetBlue1', 'CadetBluc5', 'CadetBlue3','CadetBlue2', 'turquoise1', 'turquoisc5', 'turquoise3', 'turquoise2', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarinc5', 'aquamarine2', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreusc5', 'chartreuse3', 'chartreuse2','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolatc5', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orangc5','orange3', 'orange2', 'DarkOrange1', 'DarkOrangc5', 'DarkOrange3', 'DarkOrange2','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purplc5', 'purple3', 'purple2', 'MediumPurple1', 'MediumPurplc5','MediumPurple3', 'MediumPurple2', 'thistle1', 'thistlc5', 'thistle3', 'thistle2','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99')  
c3 = Combobox(root,width=8,background='white',font='Arial 15')
c3['values'] = colors
c3.current(2)
c4 = Combobox(root,width=8,background='white',font='Arial 15')
c4['values'] = colors
c4.current(0)
c5 = Combobox(root,width=8,background='white',font='Arial 15')
c5['values'] = colors
c5.current(2)
c6 = Combobox(root,width=8,background='white',font='Arial 15')
c6['values'] = ("ua", "ru", "en")
cur = None
if lang == "en":
   cur = 2
elif lang == "ru":
   cur = 1
elif lang == "ua":
   cur = 0
c6.current(cur)
c7 = Combobox(root,width=8,background='white',font='Arial 10')
c7['values'] = ("BooleanVar()", "IntVar()", "DoubleVar()", "StringVar()")
c7.current(0)
c6.grid(row=0,column=2,sticky=N+S+W+E)
l17.grid(row=0,column=1,sticky=N+S+W+E)
b12.grid(row=0,column=3,sticky=N+S+W+E)
l0.grid(row=1,column=2)
b1.grid(row=2,rowspan=3,column=3,sticky=N+S+W+E)
l1.grid(row=2,column=1)
e1.grid(row=2,column=2)
l2.grid(row=3,column=1)
c5.grid(row=3,column=2,sticky=N+S+W+E)
l3.grid(row=4,column=1)
c1.grid(row=4,column=2,sticky=N+S+W+E)
l4.grid(row=5,column=2)
l5.grid(row=6,column=1)
e2.grid(row=6,column=2,columnspan=2,sticky=N+S+W+E)
l6.grid(row=7,column=1)
e3.grid(row=7,column=2)
l14.grid(row=7,column=3)
e7.grid(row=7,column=3,sticky=N+E)
l7.grid(row=8,column=1)
e4.grid(row=8,column=2)
e8.grid(row=8,column=3,sticky=N+E)
l8.grid(row=9,column=1)
l15.grid(row=9,column=3)
c3.grid(row=9,column=2,sticky=N+S+W+E)
c4.grid(row=10,column=2,sticky=N+S+W+E)
l9.grid(row=10,column=1)
e9.grid(row=10,column=3,sticky=N+E)
l16.grid(row=11,column=3)
l10.grid(row=11,column=1)
c2.grid(row=11,column=2,sticky=N+S+W+E)
l11.grid(row=12,column=1)
e5.grid(row=12,column=2,sticky=N+W)
e10.grid(row=12,column=3,sticky=N+E)
l12_1.grid(row=13,column=1,columnspan=3)
l12.grid(row=14,column=1)
e6.grid(row=14,column=2,columnspan=2,sticky=N+S+W+E)
txt.grid(row=15,column=2,columnspan=2,sticky=N+S+W+E)
l13.grid(row=15,column=1)
b6.grid(row=16,column=3,sticky=N+S+W+E)
b2.grid(row=16,column=1,sticky=N+S+W+E)
b3.grid(row=16,column=2,sticky=N+S+W+E)
b4.grid(row=17,column=3,sticky=N+S+W+E)
b7.grid(row=17,column=2,sticky=N+S+W+E)
b8.grid(row=17,column=1,sticky=N+S+W+E)
b14.grid(row=18,column=3,sticky=N+S+W+E)
l18.grid(row=18,column=1,sticky=N+S+W+E)
c7.grid(row=18,column=2,sticky=N+S+W+E)
b13.grid(row=19,column=1,columnspan=3,sticky=N+S+W+E)
b5.grid(row=20,column=3,sticky=N+S+W+E)
b9.grid(row=20,column=1,sticky=N+S+W+E)
b10.grid(row=20,column=2,sticky=N+S+W+E)
b11.grid(row=21,column=2,sticky=N+S+W+E)
b15.grid(row=21,column=3,sticky=N+S+W+E)
b16.grid(row=21,column=1,sticky=N+S+W+E)

cycle()
root.mainloop()