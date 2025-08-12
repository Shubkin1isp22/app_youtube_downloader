import re, os, threading
from yt_dlp import YoutubeDL
import customtkinter as tk
from threading import Thread
from tkinter import filedialog

postprocess = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat':'mp4'
        }]

def download(url):
    print("Download is run")
    path = os.path.join(path_text.get(), '%(title)s.%(ext)s')
    options = {
        'cookiesfrombrowser': ('chrome',),
        'outtmpl': path,
        'format' : f'{format.get()}',
        'noplaylist':True,
        'merge_output_format':'mp4',
        'postprocessors': postprocess
    }
    yt = YoutubeDL(options)
    if is_url(url):
        try:    
            with yt as video:
                video.download(url)
        except Exception as e:
            print(f"Ошибочка: ",{e})

def thread_download(url):
    new_potok = threading.Thread(target=download, args=(url,))
    new_potok.start()

def is_url(url):
    print("IS_URL running")
    if bool(re.match('https://', url)):
        clear_label()
        return True
    f_error_label()
    return False
    
def clear_label():
    text_error.set("")
    input.delete(0, "end")
    print("Is clear")

def f_error_label():
    text_error.set("Ссылка не корректна")

def choose_directory():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_input.delete(0, "end")
        path_text.set(folder_path)

def segment_but(variant):
    global postprocess
    buttons_values = {
        "Видео и аудио": 'bestvideo + bestaudio/best',
        "Аудио": 'bestaudio[acodec^=mp4a]/bestaudio/best',
        "Видео": 'bestvideo[vcodec^=avc1]/bestvideo/best'
    }

    keys = {
        "Видео и аудио": 'FFmpegVideoConvertor',
        "Аудио": 'FFmpegExtractAudio',
        "Видео": 'FFmpegVideoConvertor'
    }
    preferred = {
        "Видео и аудио": 'preferedformat',
        "Аудио": 'preferredcodec',
        "Видео": 'preferedformat'
    }
    mp = {
        "Видео и аудио": 'mp4',
        "Аудио": 'mp3',
        "Видео": 'mp4'
    }

    postprocessors_list = [{
        'key': f'{keys[variant]}',
        f'{preferred[variant]}': f'{mp[variant]}'
    }]

    reset =  buttons_values[variant]
    format.set(reset)
    postprocess = postprocessors_list

    

tk.set_appearance_mode("light")
tk.set_default_color_theme("dark-blue")

win = tk.CTk()
win.geometry("300x400")
win.title("Video Downloader")
win.configure(fg_color="#FCE6E6")

input = tk.CTkEntry(win, border_color="#FFD1D1", placeholder_text="Введите ссылку:")
input.pack(pady=(20,5), anchor = "center")

button = tk.CTkButton(win, text= "Скачать", command=lambda: thread_download(input.get()))
button.pack(pady=5)

label = tk.CTkLabel(win, text = "by shekspii", text_color="grey")
label.pack(side = "bottom", pady = 5)

# Label для вывода ошибки при неверном url
text_error = tk.StringVar()
text_error.set("")
error_label = tk.CTkLabel(win, width=200, height=25, text_color="red",textvariable=text_error)
error_label.pack(pady = (5,5))

# Сегментированная кнопка (Аудио и видео/только Аудио/только Видео)
segmented_button = tk.CTkSegmentedButton(win, values=["Видео и аудио", "Видео", "Аудио"],font=("Arial", 11), command=segment_but)
segmented_button.set("Видео и аудио")
segmented_button.pack(pady=5)

format = tk.StringVar()
format.set('bestvideo + bestaudio/best')
format_label = tk.CTkLabel(win, textvariable=format)

# Input для ввода пути сохранения видео
desktop_path = os.path.expanduser("~/Desktop")
user_path = os.path.join(desktop_path, "video_downloads")
path_text = tk.StringVar()
path_text.set(user_path)
path_input = tk.CTkEntry(win, textvariable=path_text, width=200, font=("Arial", 12), justify="left")
path_input.pack(side='bottom',pady=(5,45))

# Кнопка для срабатывания askdirectory
button_path = tk.CTkButton(win, width=200,text="Выбрать", command=choose_directory)
button_path.pack(side='bottom',pady=(0,5))

# Надпись над кнопкой выбора пути сохранения, что бы не громаздить в кнопке много текста
path_label = tk.CTkLabel(win, text = "Выберите путь сохранения",font=("Arial", 13),text_color="gray")
path_label.pack(side="bottom", pady = 2)

print("Programm is run")
win.mainloop()