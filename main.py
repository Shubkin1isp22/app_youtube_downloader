import re, os
from yt_dlp import YoutubeDL
import customtkinter as tk


def download(url):
    print("Download is run")
    home_path = os.path.expanduser('~/Desktop')
    path = os.path.join(home_path, "video_downloads", '%(title)s.%(ext)s')
    options = {
        'cookiesfrombrowser': ('chrome',),
        'outtmpl': path,
        'format' : 'bestvideo[vcodec^=avc1] + bestaudio[acodec^=mp4a]',
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