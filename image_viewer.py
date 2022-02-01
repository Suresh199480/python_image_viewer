from tkinter import *
from PIL import Image, ImageTk
import os

mw = Tk()
mw.title('Image Viewer')
mw.config(bg='grey')

path = 'images'
files_list = os.listdir(path)
img_list = []
# print(files_list)
for f in files_list:
    if '.jpg' in f or '.png' in f:
        # print(f)
        img_with_path = path + '/' + f
        img_list.append(img_with_path)

# print(img_list)
img = ImageTk.PhotoImage(Image.open(img_list[0]))
img_lbl = Label(mw, image=img)
img_lbl.grid(row=0, column=1, padx=30, pady=10)

img_num = 0


def fwd_func(num):
    global img, img_num
    back_btn.config(state='normal')
    img_num = num + 1
    # print(img_num, len(img_list))
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_lbl.config(image=img)
    if len(img_list) == img_num + 1:
        fwd_btn.config(state='disabled')


def back_func(num):
    global img, img_num
    fwd_btn.config(state='normal')
    img_num = num - 1
    # print(img_num, len(img_list))
    img = ImageTk.PhotoImage(Image.open(img_list[img_num]))
    img_lbl.config(image=img)
    if img_num == 0:
        back_btn.config(state='disabled')


fwd_btn = Button(mw, text='>>Next', font=('', 20), command=lambda: fwd_func(img_num))
fwd_btn.grid(row=0, column=3, padx=10, pady=10, sticky=E)

back_btn = Button(mw, text='<<Back', font=('', 20), state='disabled', command=lambda: back_func(img_num))
back_btn.grid(row=0, column=0, padx=10, pady=10, sticky=W)

mw.mainloop()
