import yt_dlp, re
from yt_dlp import YoutubeDL
import customtkinter as tk


def download(url):
    print("Download is run")
    options = {
        'cookiesfrombrowser': ('chrome',),
    }
    yt = YoutubeDL(options)
    if is_url(url):
        try:    
            with yt as video:
                video.download(url)
        except Exception as e:
            print(f"Ошибочка: ",{e})

def is_url(url):
    print("IS_URL running")
    if bool(re.match('https://', url)):
        return True

win = tk.CTk()
win.geometry("300x450")
input = tk.CTkEntry(win, placeholder_text="Введите ссылку:")
input.pack(pady=7)

button = tk.CTkButton(win, text= "Скачать",fg_color="darkgreen", command=lambda: download(input.get()))
button.pack(pady=5)
print("Programm is run")
win.mainloop()