


# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random

# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали из класса Tk() — он есть в графической библиотеке
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('Packman')
# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить. Попробуйте :)
tk.wm_attributes('-topmost', 1)
# создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=800, height=600, highlightthickness=0)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом

tk.update()








def packman():
    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 300
    x1_eye = x1 + 110
    y1_eye = y1 + 30
    x2_eye = x2 - 70
    y2_eye = y2 - 150
    s = -30
    e = 60
    close_mouth = True
    open_mouth = False
    while True:
        if x1 > 700:
            x1 = 100
            x2 = 300
        x1 += 5
        x2 += 5
        x1_eye = x1 + 110
        x2_eye = x2 - 70
        canvas.create_rectangle(0, 0, 1000, 1000, fill='gray94')  # очистка холста(костыль, так не надо делать)
        canvas.create_oval(x1, y1, x2, y2, fill='yellow', outline='black')
        canvas.create_oval(x1_eye, y1_eye, x2_eye, y2_eye, fill='black', outline='black')
        canvas.create_arc(x1, y1, x2, y2, start=s, extent=e, fill='gray94')
        canvas.create_arc(x1, y1, x2, y2, start=s, extent=e, style=ARC, outline='gray94', width=1.5)
        print(s, e)
        if close_mouth:
            s += 10  # увеличение s должно быть в два раза меньше уменьшения e
            e -= 20
        elif open_mouth:
            s -= 10
            e += 20
        if abs(s) < 1:
            close_mouth = False
            open_mouth = True
        if s < -29:
            close_mouth = True
            open_mouth = False
        time.sleep(0.1)
        tk.update()





def moving_ball():
    """
    Позволяет двигать любые объекты, нужен только id
    """
    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200
    velocity = 10
    id = canvas.create_oval(x1, y1, x2, y2, fill='yellow', outline='black')  # надо писать id вне цикла
    while True:
        print(id)  # двигаю объект с одним и тем же id
        canvas.move(id, velocity, 0)
        # print(x1, y1, x2, y2)  # изначальные координаты в процессе не изменяются
        print(canvas.coords(id))  # текущие координаты можно получить так
        time.sleep(0.07)
        tk.update()



if __name__ == '__main__':
    packman()
    # moving_ball()







































