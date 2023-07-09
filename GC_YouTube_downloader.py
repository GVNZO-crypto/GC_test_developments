# Импортируем tkinter
from tkinter import *

# Импортируем модуль YouTube
from pytube import YouTube

# Инициализация tkinter
root = Tk()

# Настройка геометрии графического интерфейса
root.geometry("400x350")

# Установка заголовка графического интерфейса
root.title("GVNZO Youtube Video Downloader")

# Определение функции загрузки
def download():

    # Использование try и except для выполнения программы без ошибок
    try:
        myVar.set("Загрузка...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Видео успешно загружено!")
    except Exception as e:
        myVar.set("Ошибка")
        root.update()
        link.set("Введите правильную ссылку")

# Создал виджет Label для приветствия пользователя
Label(root, text="Добро пожаловать на загрузчик\n YouTube Видео", font="Consolas 15 bold").pack()

# Объявление переменной типа StringVar
myVar = StringVar()

# Установка текста по умолчанию в myVar
myVar.set("Введите ссылку ниже")

# Создал виджет Entry, чтобы попросить пользователя ввести url
Entry(root, textvariable=myVar, width=40).pack(pady=10)

# Объявление переменной типа StringVar
link = StringVar()

# Создал виджет Entry для получения ссылки
Entry(root, textvariable=link, width=40).pack(pady=10)

# Создал и вызвал функцию download для загрузки видео
Button(root, text="Скачать видео", command=download).pack()

# Выполнение главного цикла
root.mainloop()

# coding_by_GVNZO

"""Код не работает т.к при запуске тестового режима выходит www.youtube.com не найден, жду обновление модуля pytube"""