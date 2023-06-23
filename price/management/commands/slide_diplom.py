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
        tk.Label(self, text="Диплом Стартовая траница", width=self.screen_width, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                            fill="x",
                                                                                                            pady=10)
        tk.Button(self, text="DiplomLib",
                  command=lambda: master.switch_frame(Diplom_Libraries)).pack()
        tk.Button(self, text="DiplomSerializers",
                  command=lambda: master.switch_frame(Diplom_serializers)).pack()
        tk.Button(self, text="DiplomAuth",
                  command=lambda: master.switch_frame(Diplom_Authentication)).pack()


from PIL import ImageTk, Image


class Diplom_Libraries(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        img = Image.open('media/diplom_settings.png')
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='DiplomLibraries', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label = tk.Label(self,
                         image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = 'Необходимо реализовать эндпоинт, который будет формировать цену товара с учетом всех надбавок. Эндпоинт используется для\n' \
               'маркетплейса, поэтому необходимо цену, которая была передана в запросе, увеличить на определенную сумму. Маркетплейс\n' \
               'должен заплатить налоги в размере 6%, также комиссию банку за проведение транзакции покупки в размере 2%,\n' \
               'также комиссию за проведение транзакцию перевода оплаты автору продукта и оставить себе комиссию в размере 20%.\n' \
               'При этом пользоваться этим эндпоинтом могут только авторизованные пользователи со статусом "продавец".\n' \
               '   '"Задача разделена на два модуля: 1. Регистрация, Логирование, Разлогирование в данном случае в поле модели пользователя ...BooleanField(choices=... \n" \
               "регистрация на rest_auth.registration и в serializers.py прописываем дополнительное поле родительскому классу RegisterSerializer\n" \
               "                                 2. Исполнение логики, в данном случае это функции create, update в serializers.py\n" \
               '           "БИБЛИОТЕКИ: \n"' \
               'INSTALLED_APPS = [\n' \
               "'django.contrib.admin',\n" \
               "'django.contrib.auth',\n" \
               "'django.contrib.contenttypes',\n" \
               "'django.contrib.sessions',\n" \
               "'django.contrib.messages',\n" \
               "'django.contrib.staticfiles',\n" \
               "'price',\n" \
               "'rest_framework',\n" \
               "'rest_framework.authtoken',\n" \
               "'rest_auth,\n" \
               "'rest_auth.registration,\n" \
               "'allauth,\n" \
               "'allauth.account,\n" \
               "'allauth.socialaccount,\n" \
               "'drf_yasg',\n" \
               ']\n'
        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)  # .pack(side=BOTTOM)


class Diplom_serializers(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        label = tk.Label(self, text='DiplomSerializers', font=('times', 18, 'bold'))
        label.pack(side="top", fill="x", pady=10)
        text = 'Сериализаторы производят перевод в json формат и валидацию, то есть логика по какому-либо полю может быть реализована на функциях create, update \n' \
               'Дополнительное поле пользователя "Продавец", помимо models.py, также устанавливается в serializers.py \n' \
               'class CustomRegisterSerializer(RegisterSerializer):\n' \
               '    seller = CustomUserSerializer(required=True)\n '

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)
        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)

        img1 = Image.open('media/diplom_serializers1.png')
        # img1 = img1.resize((800, 410), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('media/diplom_serializers2.png')
        # img2 = img1.resize((800, 410), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)
        img3 = Image.open('media/diplom_serializers3.png')
        # img3 = img1.resize((800, 410), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)
        # Define function to update the image

        # Create a canvas and add the image into it
        global canvas, image_container
        canvas = tk.Canvas(self, width=650, height=350)
        canvas.pack()
        # Create a button to update the canvas image
        function1 = [x for x in (self.photo2, self.photo3)]
        function = iter(function1)
        button = tk.Button(self, text="Refresh image",
                           command=lambda: self.update_image(next(function)))
        button.pack()

        self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)

    def update_image(self, j):
        print('____________________j', j)
        canvas.itemconfig(self.image_container, image=j)


class Diplom_Authentication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        label = tk.Label(self, text='DiplomSerializers', font=('times', 18, 'bold'))
        label.pack(side="top", fill="x", pady=10)

        text = '                      Аутенфикация (Логирование, Разлогирование, Регистрация (без подтверждения емэйла), валидация: \n' \
               'Здесь рассмотрим валидацию. Пользователь может создавать, удалять свои продукты и менять цену только в своих продукдах, скрин из файла views.py \n' \
               'Кастомная функция получения токена CustomAuthToken из документации. Получаем токен каждый раз, когда Post\n' \
               'Регистрация встроенная на ендпоинте rest-auth/registration во views.py нет кода по этому поводу \n' \

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).place(x=50, y=-75)
        img1 = Image.open('media/diplom_view_validation1.png')
        self.photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('media/diplom_view_validation2.png')
        self.photo2 = ImageTk.PhotoImage(img2)
        img3 = Image.open('media/diplom_view_customtoken.png')
        self.photo3 = ImageTk.PhotoImage(img3)
        img4 = Image.open('media/diplom_url_auth.png')
        self.photo4 = ImageTk.PhotoImage(img4)
        # Define function to update the image

        # Create a canvas and add the image into it
        global canvas, image_container
        canvas = tk.Canvas(self, width=650, height=350)
        canvas.pack()
        # Create a button to update the canvas image
        function1 = [x for x in (self.photo2, self.photo3, self.photo4)]
        function = iter(function1)
        button = tk.Button(self, text="Refresh image",
                           command=lambda: self.update_image(next(function)))
        button.pack()

        self.image_container = canvas.create_image(0, 0, anchor="nw", image=self.photo1)

    def update_image(self, j):
        print('____________________j', j)
        canvas.itemconfig(self.image_container, image=j)


from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        app = SampleApp()
        app.geometry('1800x1000')
        app.mainloop()
