################# Enter menyaet image######################
# from tkinter import Tk
#
# from PIL import ImageTk, Image
# import tkinter as tk
# root = Tk()
# path1 = '/home/andrey_mazo/PycharmProjects/DjangoProjectDiplomSkyeng/media/diplom_serializers1.png'
# path2 = '/home/andrey_mazo/PycharmProjects/DjangoProjectDiplomSkyeng/media/странная ваза с суку.png'
#
# img1 = ImageTk.PhotoImage(Image.open(path1))
# panel1 = tk.Label(root, image=img1)
# panel1.pack(side="bottom", fill="both", expand="yes")
#
#
# def callback(e):
#     img2 = ImageTk.PhotoImage(Image.open(path2))
#     panel1.configure(image=img2, width=1000, height=500)
#     panel1.image = img2
#
#
# root.bind("<Return>", callback)
# root.mainloop()
##########################################

# lst = [1, 2, 3]
# l = iter(lst)
# for i in l:
#     print(i)
# def function():
#     for x in range(10):
#         yield x ** 2


function1 = (x ** 2 for x in range(10))

# g1 = function()
# for x in g1:
#     print("Received", x)
for x in function1:
    print("Received", x)