import re, os, threading
from yt_dlp import YoutubeDL
import customtkinter as tk
from threading import Thread

def download(url):
    print("Download is run")
    home_path = os.path.expanduser('~/Desktop')
    path = os.path.join(home_path, "video_downloads", '%(title)s.%(ext)s')
    options = {
        'cookiesfrombrowser': ('chrome',),
        'outtmpl': path,
        'format' : 'bestvideo[vcodec^=avc1] + bestaudio[acodec^=mp4a]/best',
        'noplaylist':True,
        'merge_output_format':'mp4',
        'postprocessors':[{
            'key': 'FFmpegVideoConvertor',
            'preferedformat':'mp4'
        }]
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

text_error = tk.StringVar()
text_error.set("")
error_label = tk.CTkLabel(win, width=200, height=25, text_color="red",textvariable=text_error)
error_label.pack(pady = (5,5))


print("Programm is run")
win.mainloop()