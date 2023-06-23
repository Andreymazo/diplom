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
        tk.Frame.configure(self, width=self.screen_width, height=self.screen_height, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)

        # self.win_frame.configure(height=self.screen_height)
        tk.Label(self, text="Тестовое Селери Стартовая траница", width=self.screen_width, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                            fill="x",
                                                                                                            pady=10)
        tk.Button(self, text="Селери таски в таскс файле",
                  command=lambda: master.switch_frame(Tz1_celery_tasks)).pack()
        tk.Button(self, text="Селери админка и ассинхронный принт",
                  command=lambda: master.switch_frame(Tz1_celery_adminka)).pack()
        # tk.Button(self, text="Аудио файл (меняем расширение)",
        #           command=lambda: master.switch_frame(Tz3_audio)).pack()


from PIL import ImageTk, Image


class Tz1_celery_tasks(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        label = tk.Label(self, text='Селери таски в tasks.py', font=('times', 18, 'bold'))
        label.pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)
        text = ' Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration\n' \
               'во временную папку. После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла. Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration\n' \
               'Обязательно 100% покрытие тестами При выполнении в ChatGPT - обязательна переработка\n' \
            'а) клонируем и разорачиваем проект у себя, создаем суперюзера, вся работа из админки: добавляем 4 таски, поминутно, например, и получаем файл резулт1.ткст\n' \
            'б) создаем суперпольователя (python3 manage.py createsuperuser) работать через админку + 2 команды в консоли: 1. celery -A config worker -l INFO 2.celery -A config beat -l info -S django'

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
        img1 = Image.open('media/tz1_celery_tasks1.png')
        self.photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('media/tz1_celery_tasks2.png')
        self.photo2 = ImageTk.PhotoImage(img2)
        # img3 = Image.open('media/tz1_celery_tasks2.png')
        # self.photo3 = ImageTk.PhotoImage(img3)
        # img4 = Image.open('media/tz1_view_search.png')
        # self.photo4 = ImageTk.PhotoImage(img4)
        # img5 = Image.open('media/tz1_filters.png')
        # # img5 = img5.resize((700, 410), Image.ANTIALIAS)
        # self.photo5 = ImageTk.PhotoImage(img5)
        # self.photo5 = self.photo5
        #(self.winfo_screenwidth())

        # Create a canvas and add the image into it
        global canvas, image_container
        canvas = tk.Canvas(self, width=1150, height=450)
        canvas.pack()
        # Create a button to update the canvas image
        function1 = [x for x in (self.photo1, self.photo2)]# self.photo3, self.photo4, self.photo5
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



class Tz1_celery_adminka(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        label = tk.Label(self, text='DiplomSerializers', font=('times', 18, 'bold'))
        label.pack(side="top", fill="x", pady=10)
        text = 'Работа из админки и в консоли 1. celery -A config worker -l INFO 2.celery -A config beat -l info -S django'

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)

        img1 = Image.open('media/tz1_celery_admin.png')
        self.photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('media/tz1_celery_asyncprint.png')
        self.photo2 = ImageTk.PhotoImage(img2)
        # img3 = Image.open('media/diplom_serializers3.png')
        # # img3 = img1.resize((800, 410), Image.ANTIALIAS)
        # self.photo3 = ImageTk.PhotoImage(img3)
        # Define function to update the image

        # Create a canvas and add the image into it
        global canvas, image_container
        canvas = tk.Canvas(self, width=1150, height=450)
        canvas.pack()
        # Create a button to update the canvas image
        function1 = [x for x in (self.photo1, self.photo2)]#self.photo2, self.photo3
        function = iter(function1)
        button = tk.Button(self, text="Refresh image",
                           command=lambda: self.update_image(next(function)))
        button.pack()

        self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)

    def update_image(self, j):
        print('____________________j', j)
        canvas.itemconfig(self.image_container, image=j)


# class Tz3_audio(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
#         label = tk.Label(self, text='Тестовое СПА Таблица (2 варианта сортировки)', font=('times', 18, 'bold'))
#         label.pack(side="top", fill="x", pady=10)
#
#         tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
#                   command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)
#         text = 'надо создать спа приложение (один темплейт и реквест только для создания таблицы).Модель - таблица с 4 полями, создаем рэндомно при запуске 2 цифровых поля и одно с помощью библиотеки names.\n' \
#                'Tz1.   Сделал 2 мя способами: с приложением django-tables2, реквест только при заплолнении таблицы.Сортировка у django-tables2 своя, у django-filters свояю Файл views.py class TableListView(SingleTableView):\n' \
#                ' на ендпоинтах tz1_1/, функция search (джанго-фильтерс), и на '', TableListView.as_view() (джанго-тейблс2) \n' \
#                ' Создаем файл filters.py наследуемся от FilterSet и по документации фильтруем все, что хотим\n'
#         TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
#                                    font=(
#                                        'times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=
#
#         TKScrollTXT.insert(1.0, text)
#         TKScrollTXT.configure()
#         TKScrollTXT.pack(side=tk.TOP)
#
#         tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised",
#                            pady=125)
#
#         tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
#                   command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)  # .pack(side=BOTTOM)
#         img1 = Image.open('media/tz4_audio_url.png')
#         img1 = img1.resize((700, 400), Image.ANTIALIAS)
#         self.photo1 = ImageTk.PhotoImage(img1)
#         img2 = Image.open('media/tz4_audio_view.png')
#         img2 = img2.resize((700, 400), Image.ANTIALIAS)
#         self.photo2 = ImageTk.PhotoImage(img2)
#         img3 = Image.open('media/tz4_audio_models.png')
#         self.photo3 = ImageTk.PhotoImage(img3)
#         # img4 = Image.open('media/tz1_view_search.png')
#         # self.photo4 = ImageTk.PhotoImage(img4)
#         # img5 = Image.open('media/tz1_filters.png')
#         # # img5 = img5.resize((700, 410), Image.ANTIALIAS)
#         # self.photo5 = ImageTk.PhotoImage(img5)
#         # self.photo5 = self.photo5
#         # (self.winfo_screenwidth())
#
#         # Create a canvas and add the image into it
#         global canvas, image_container
#         canvas = tk.Canvas(self, width=650, height=450)
#         canvas.pack()
#         # Create a button to update the canvas image
#         function1 = [x for x in (self.photo1, self.photo2, self.photo3)]
#         function = iter(function1)
#
#         button = tk.Button(self, text="Refresh image",
#                            command=lambda: self.update_image(next(function)))
#         button.pack()
#
#         self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)
#
#     def update_image(self, j):
#         canvas.itemconfig(self.image_container, image=j)


from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        app = SampleApp()
        app.geometry('1800x1000')
        app.mainloop()