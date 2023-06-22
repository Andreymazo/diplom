# import tkinter as tk
#
# import blue as blue
# import green as green
# import img as img
# from ruamel.yaml import anchor
#
# root = tk.Tk()
# #
# # # root.mainloop()
# root.title("Create new price")
# # root.geometry("400x300+100+100")
# canvas = tk.Canvas(root, width=1500, height=900, bg='green')  # r
# # canvas['bg'] = "green"
#
#
# def content(tx):
#     canvas.create_text(10, 50, text=tx, anchor=tk.NW, justify=tk.LEFT)
# canvas.create_rectangle(0,45,800,10, fill="yellow")
# img = tk.PhotoImage(file="media/рюмкиРесурс 8.png")
# canvas.create_text(10, 10, text="First text", fill="blue", font="Times 20 italic bold", anchor=tk.NW)
# content("This is .....................")
# canvas.create_image(10, 10, image=img, anchor=tk.NW)
# canvas.pack()
# from django.core.management import BaseCommand
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         root.mainloop()
###################################################################
#
# from tkinter import *
# def raise_frame(frame):
#     frame.tkraise()
# root = Tk()
# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)
# for frame in (f1, f2, f3, f4):
#     frame.grid(row=0, column=0, sticky='news')
# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# Label(f1, text='FRAME 1').pack()
# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()
# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')
# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()
# raise_frame(f1)
#
# from django.core.management import BaseCommand
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         root.mainloop()


########################################################
# try:
#     import tkinter as tk  # python 3
#     from tkinter import font as tkfont  # python 3
# except ImportError:
#     import Tkinter as tk  # python 2
#     import tkFont as tkfont  # python 2
#
#
# class SampleApp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
#
#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#         for F in (StartPage, PageOne, PageTwo):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#
#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("StartPage")
#
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label1 = tk.Label(self, text="This is the start page", font=controller.title_font)
#         label1.pack(side="top", fill="x", pady=10)
#         label2 = tk.Label(
#             text="Hello, Tkinter",
#             foreground="white",  # Set the text color to white
#             background="black",  # Set the background color to black "purple"
#
#         )
#         # label = tk.Label(
#         #     text="Hello, Tkinter",
#         #     fg="white",
#         #     bg="black",
#         #     width=10,
#         #     height=10
#         # )
#         label2.pack(side='left')#(side="top", fill="x", pady=10)
#
#         button1 = tk.Button(self, text="Go to Page One",
#                             command=lambda: controller.show_frame("PageOne"))
#         button2 = tk.Button(self, text="Go to Page Two",
#                             command=lambda: controller.show_frame("PageTwo"))
#         button1.pack()
#         button2.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 1", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
#
#
# from django.core.management import BaseCommand
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
# #         root.mainloop()
# #         if __name__ == "__main__":
#             app = SampleApp()
#             app.mainloop()
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
################################################################################

import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, YES, TOP, BOTTOM
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Scrollbar


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# from tkinter import *
#
# ws = Tk()
# ws.title('Python Guides')
# ws.geometry('250x200')
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        tk.Label(self, text="This is the start page", width=20, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                            fill="x",
                                                                                                            pady=10)
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(GeoDjango_Libraries)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(GeoDjango_Video)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(GeoDjango_Settings)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(GeoDjango_Model)).pack()


from PIL import ImageTk, Image


class GeoDjango_Libraries(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        img = Image.open('media/GeoDjangoMap.png')
        img = img.resize((1250, 450), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        # img = ImageTk.PhotoImage(Image.open('media/лисица.png'))  # media/странная ваза с суку.png
        # self.images = []
        # self.photo = img
        tk.Label(self, text='GeoDjango', font=('times', 22, 'bold')).pack(side="top", fill="x", pady=10)
        label = tk.Label(self,
                         image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = '               БИБЛИОТЕКИ: \n' \
               '- Leaflet (html lib), ссылка на установку geodjango: ' \
               'https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/\n' \
               '- djangorestframework-gis (pip install djangorestframework-gis),\n' \
               '- GDAL (Geospatial Data Abstraction Library) sudo apt install gdal-bin, \n' \
               '- PostGIS Установка в несколько шагов, подразумевается, что Постгрес уже есть, по ссылке документация\n' \
               '                      ссылка на установку postgis' \
               'https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS3UbuntuPGSQLApt\n' \
               '                      ссылка на видео Джанго-Контрибьютора: \n' \
               'https://www.youtube.com/watch?v=k2Y_jBmyGVY\n' \
               '\n' \
               '                      Settings: \n' \
               '"DATABASES = {\n' \
               '"default": {\n' \
               '"ENGINE": "django.contrib.gis.db.backends.postgis",\n' \
               '"NAME": "geodjango",\n' \
               '"USER": "geo",\n' \
               '},\n' \
               '},\n' \
               '...\n' \
               'INSTALLED_APPS = [\n' \
               '"django.contrib.admin",\n' \
               '"django.contrib.auth",\n' \
               '"django.contrib.contenttypes",\n' \
               '"django.contrib.sessions",\n' \
               '"django.contrib.messages",\n' \
               '"django.contrib.staticfiles",\n' \
               '"django.contrib.gis",\n' \
               '"world",\n' \
               ' ]  \n'

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=
        # img = ImageTk.PhotoImage(Image.open('media/лисица.png'))  # media/странная ваза с суку.png
        # set default text if desired
        # img = ImageTk.PhotoImage(Image.open('media/лисица.png'))  # media/странная ваза с суку.png

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        # label1 = tk.Label(self, image=self.photo1, width=(self.winfo_screenwidth()) - 350, height=((self.winfo_screenheight()) - 150))  # ,  text=text, width=100, height=1000, font=('times', 14, 'bold')
        # label1.pack(fill=BOTH, pady=10, expand=YES)  # image=img,side=LEFT, #

        # my_canvas = tk.Canvas(label, width=400, height=400, bg='green')
        # img = tk.PhotoImage(file="media/рюмкиРесурс 8.png")
        # canvas.create_text(10, 10, text="First text", fill="blue", font="Times 20 italic bold", anchor=tk.NW)
        # content("This is .....................")
        # my_canvas.create_image(10, 10, image=img, anchor=tk.NW)
        # my_canvas.pack()

        # my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        # y_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        # y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # my_canvas.configure(yscrollcommand=y_scrollbar.set)
        # my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))
        ####################################################
        # self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        # self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        # self.canvas = tk.Canvas(self, width=300, height=100,
        #                         xscrollcommand=self.scroll_x.set,
        #                         yscrollcommand=self.scroll_y.set)
        # self.scroll_x.config(command=self.canvas.xview)
        # self.scroll_y.config(command=self.canvas.yview)
        #########################################

        # https: // pythonru.com / uroki / sozdanie - skrollbarov - tkinter - 6?ysclid = lj3ccv0y8v398364505
        # self.canvas.bind('', self.moose_motion)
        # languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
        #              "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
        #              "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
        # ttext=[text]
        # listbox = tk.Listbox(ttext)
        # languages_var = tk.StringVar(value=text)#languages
        # listbox = tk.Listbox(listvariable=languages_var)
        # listbox.pack(side=LEFT, fill=BOTH, expand=1)
        # frame1 = tk.Frame(win, width=80, height=80, bg='#ffffff',
        #                   borderwidth=1, relief="sunken")
        # scrollbar = tk.Scrollbar(self)
        # editArea = tk.Text(self, width=10, height=10, wrap="word",
        #                    yscrollcommand=scrollbar.set,
        #                    borderwidth=0, highlightthickness=0)
        # scrollbar.config(command=editArea.yview)
        # scrollbar.pack(side="right", fill="y")
        # editArea.pack(side="left", fill="both", expand=True)

        # sb_ver = Scrollbar(
        #     self,
        #     orient=VERTICAL,
        #     command=listbox.yview
        #     # command=lb.yview
        #
        # )
        # https://www.codeunderscored.com/tkinter-scrollbar-explained-with-examples/

        # scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
        # https: // metanit.com / python / tkinter / 2.13.php?ysclid = lj1ujabvoz278548423
        # sb_ver.pack(side=RIGHT,fill=Y, expand=True)##
        # listbox["yscrollcommand"] = sb_ver.set
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1
        # frame = ttk.Frame(root, relief=tk.RAISED)
        # Create an object of tkinter ImageTk

        # ws = Tk()
        # sb_ver = Scrollbar(
        #     ws,
        #     orient=VERTICAL
        # )
        # sb_ver.pack(side=RIGHT, fill=Y)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


# import Tkinter
# tk = Tkinter.Tk()
# frame1 = Tkinter.Frame(tk, height = 100, width = 100, bg = "WHITE", borderwidth=2)
# frame2 = Tkinter.Frame(frame1, height = 100, width = 100, bg = "RED", borderwidth=2)
# frame1.pack()
# frame2.pack()
# label = Tkinter.Label(frame2, text = "Label") #Receive a callback from button here
# label.pack()
# button = Tkinter.Button(frame1,text="Button") #Send some action to Label here
# button.pack()
# tk.mainloop()

class GeoDjango_Video(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        tk.Label(self, text="This is page 2", width=100, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                     fill="x", pady=10)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack()


class GeoDjango_Settings(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        tk.Label(self, text="This is page 3", width=100, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                     fill="x", pady=10)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack()


class GeoDjango_Model(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        tk.Label(self, text="This is page 3", width=100, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                     fill="x", pady=10)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack()


from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        app = SampleApp()
        app.geometry('1800x1000')
        app.mainloop()
#########################################################################
# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk


# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()
#
#
# class StartPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go to page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         tk.Button(self, text="Go to page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()
#
#
# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='blue')
#         tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
#
# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='red')
#         tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
# from django.core.management import BaseCommand
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
# # if __name__ == "__main__":
#         app = SampleApp()
#         app.mainloop()
########################################################3
