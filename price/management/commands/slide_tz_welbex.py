import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, YES, TOP, BOTTOM, ttk
from tkinter.scrolledtext import ScrolledText


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


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Set up the root window Note the -72 hack to get it to fit
        self.screen_height = self.winfo_screenheight()
        # self.screen_height = self.winfo_screenheight() - 72
        self.screen_width = self.winfo_screenwidth()
        tk.Frame.configure(self, width=self.screen_width, height=self.screen_height, bg='green', borderwidth=10,
                           highlightcolor='blue', relief="raised", pady=125)

        # self.win_frame.configure(height=self.screen_height)
        tk.Label(self, text="Сервис поиска ближайших машин для перевозки грузов.", width=self.screen_width, height=10,
                 font=('times', 22, 'bold')).pack(side="top",
                                                  fill="x",
                                                  pady=10)
        tk.Button(self, text="МВК в Велбексе Models, Uls, Controllers",
                  command=lambda: master.switch_frame(Tz_Welbex_MVC)).pack()
        # tk.Button(self, text="Сервис поиска ближайших машин для перевозки грузов.",
        #           command=lambda: master.switch_frame(Tz1_celery_adminka)).pack()
        # tk.Button(self, text="Аудио файл (меняем расширение)",
        #           command=lambda: master.switch_frame(Tz3_audio)).pack()


from PIL import ImageTk, Image


class Tz_Welbex_MVC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        label = tk.Label(self, text='Сервис поиска ближайших машин', font=('times', 18, 'bold'))
        label.pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)
        text = ' Сервис поиска ближайших машин для перевозки грузов. distance - функция GeoPy \n'

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=(
                                       'times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=
        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)  # .pack(side=BOTTOM)
        img1 = Image.open('media/tz_welbex_models.png')
        self.photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('media/tz_welbex_createnumber.png')
        self.photo2 = ImageTk.PhotoImage(img2)
        img3 = Image.open('media/tz_welbex_fill_cars.png')
        self.photo3 = ImageTk.PhotoImage(img3)
        img4 = Image.open('media/tz_welbex_distance.png')
        self.photo4 = ImageTk.PhotoImage(img4)
        img5 = Image.open('media/tz_welbex_filllocations.png')
        # img5 = img5.resize((700, 410), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(img5)
        img55 = Image.open('media/tz_welbex_filllocations2.png')
        self.photo55 = ImageTk.PhotoImage(img55)
        img6 = Image.open('media/tz_welbex_serializers.png')
        self.photo6 = ImageTk.PhotoImage(img6)
        img7 = Image.open('media/tz_welbex_view1.png')
        self.photo7 = ImageTk.PhotoImage(img7)
        img77 = Image.open('media/tz_welbex_view11.png')
        self.photo77 = ImageTk.PhotoImage(img77)
        img8 = Image.open('media/tz_welbex_view2.png')
        self.photo8 = ImageTk.PhotoImage(img8)

        # self.photo5 = self.photo5
        # (self.winfo_screenwidth())
        # Create a canvas and add the image into it
        global canvas, image_container
        canvas = tk.Canvas(self, width=1150, height=450)
        canvas.pack()
        # Create a button to update the canvas image
        function1 = [x for x in (self.photo1, self.photo2, self.photo3, self.photo4, self.photo5,  self.photo55, self.photo6, self.photo7, self.photo77, self.photo8)]  # self.photo3, self.photo4, self.photo5
        function = iter(function1)

        button = tk.Button(self, text="Refresh image",
                           command=lambda: self.update_image(next(function)))
        # if self.photo5:
        #     button.configure(width = self.winfo_screenwidth())
        #     button.pack()
        button.pack()

        self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)

    def update_image(self, j):
        canvas.itemconfig(self.image_container, image=j)

#
# class Tz1_celery_adminka(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
#         label = tk.Label(self, text='DiplomSerializers', font=('times', 18, 'bold'))
#         label.pack(side="top", fill="x", pady=10)
#         text = 'Работа из админки и в консоли 1. celery -A config worker -l INFO 2.celery -A config beat -l info -S django'
#
#         TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
#                                    font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=
#
#         TKScrollTXT.insert(1.0, text)
#         TKScrollTXT.configure()
#         TKScrollTXT.pack(side=tk.TOP)
#         tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
#                   command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)
#
#         img1 = Image.open('media/tz1_celery_admin.png')
#         self.photo1 = ImageTk.PhotoImage(img1)
#         img2 = Image.open('media/tz1_celery_asyncprint.png')
#         self.photo2 = ImageTk.PhotoImage(img2)
#         # img3 = Image.open('media/diplom_serializers3.png')
#         # # img3 = img1.resize((800, 410), Image.ANTIALIAS)
#         # self.photo3 = ImageTk.PhotoImage(img3)
#         # Define function to update the image
#
#         # Create a canvas and add the image into it
#         global canvas, image_container
#         canvas = tk.Canvas(self, width=1150, height=450)
#         canvas.pack()
#         # Create a button to update the canvas image
#         function1 = [x for x in (self.photo1, self.photo2)]  # self.photo2, self.photo3
#         function = iter(function1)
#         button = tk.Button(self, text="Refresh image",
#                            command=lambda: self.update_image(next(function)))
#         button.pack()
#
#         self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)
#
#     def update_image(self, j):
#         print('____________________j', j)
#         canvas.itemconfig(self.image_container, image=j)


from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        app = SampleApp()
        app.geometry('1800x1000')
        app.mainloop()
