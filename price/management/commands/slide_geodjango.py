import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, YES, TOP, BOTTOM
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
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        tk.Label(self, text="This is the start page", width=20, height=10, font=('times', 22, 'bold')).pack(side="top",
                                                                                                            fill="x",
                                                                                                            pady=10)
        tk.Button(self, text="GeoDjangoLib",
                  command=lambda: master.switch_frame(GeoDjango_Libraries)).pack()
        tk.Button(self, text="GeoDjangoVideo",
                  command=lambda: master.switch_frame(GeoDjango_Video)).pack()
        tk.Button(self, text="GeoDjangoSettings",
                  command=lambda: master.switch_frame(GeoDjango_Settings)).pack()
        tk.Button(self, text="GeoDjangoModel",
                  command=lambda: master.switch_frame(GeoDjango_Model)).pack()
        tk.Button(self, text="GeoDjangoView",
                  command=lambda: master.switch_frame(GeoDjango_View)).pack()


from PIL import ImageTk, Image


class GeoDjango_Libraries(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        img = Image.open('media/GeoDjangoMap.png')
        img = img.resize((1250, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='GeoDjangoLibraries', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label = tk.Label(self,
                         image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = '               БИБЛИОТЕКИ: \n' \
               '- Leaflet (html lib), ссылка на установку geodjango: ' \
               'https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/\n' \
               '- djangorestframework-gis (pip install djangorestframework-gis),\n' \
               '- GDAL (Geospatial Data Abstraction Library) sudo apt install gdal-bin, \n' \
               '- PostGIS Установка в несколько шагов, подразумевается, что Постгрес уже есть\n' \
               '                      ссылка на установку postgis\n' \
               'https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS3UbuntuPGSQLApt\n'

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


class GeoDjango_Video(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        img = Image.open('media/geodjango_video.png')
        img = img.resize((1250, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='GeoDjangoVideo', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self,
                          image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label1.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = 'Установку можно проводить по видео контрибьютора\n' \
               '                ссылка на видео Джанго-Контрибьютора: \n' \
               'Working with Maps in Django and GeoDjango: From Python to PostGIS' \
               'https://www.youtube.com/watch?v=k2Y_jBmyGVY\n' \
               'Также удобно можно скопировать с интсрукции по ссылке:\n' \
               'https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS3UbuntuPGSQLApt\n'
        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


class GeoDjango_Settings(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        img = Image.open('media/geodjango_settings.png')
        img = img.resize((1250, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='GeoDjangoSettings', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label = tk.Label(self,
                         image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = '                      Settings: \n' \
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
               '"django.contrib.staticfiles' \
               '"rest_framework_gis",\n' \
               '"django.contrib.gis",\n' \
               '"markers",\n' \
               ' ]  \n'

        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


class GeoDjango_Model(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        img = Image.open('media/geodjango_model.png')
        img = img.resize((1250, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='GeoDjangoModel', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self,
                          image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label1.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = 'Новая модель с новым полем\n' \
               'Eсли у библиотеки GeoPy (общеPython(вская)) поля широта и долгота, то у\n' \
               ' GeoDjango/PostGis свое поле PointField: \n' \
               'class Marker(models.Model):\n' \
               '   name = models.CharField(max_length=255)\n' \
               '   location = models.PointField()\n'
        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


class GeoDjango_View(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised", pady=125)
        img = Image.open('media/geodjango_view.png')
        img = img.resize((1000, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, text='GeoDjangoView', font=('times', 20, 'bold')).pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self,
                          image=self.photo)  # ,  width=(self.winfo_screenwidth() / 2.) - (350 / 2.), height=((self.winfo_screenheight() / 2.) - (150 / 2.))
        label1.pack(fill=BOTH, pady=10, expand=YES, side=TOP)
        text = 'Во view.py создаем рендомно 4 точки\n'
        TKScrollTXT = ScrolledText(self, width=(self.winfo_screenwidth()), height=10, wrap='char',
                                   font=('times', 16, 'bold'))  # font=("Courier", 16, "italic") )  # yscrollcommand=

        TKScrollTXT.insert(1.0, text)
        TKScrollTXT.configure()
        TKScrollTXT.pack(side=tk.TOP)

        tk.Frame.configure(self, bg='red', borderwidth=10, highlightcolor='blue', relief="raised",
                           pady=125)  # , **size_1

        tk.Button(self, text="Return to start page", width=20, height=3, font=('times', 12, 'bold'),
                  command=lambda: master.switch_frame(StartPage)).pack(side=BOTTOM)


from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        app = SampleApp()
        app.geometry('1800x1000')
        app.mainloop()
