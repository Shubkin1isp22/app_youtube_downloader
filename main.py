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

def is_url(url):
    print("IS_URL running")
    if bool(re.match('https://', url)):
        box_close()
        return True
    f_error_box()
    return False
    

def box_close():
    error_box.configure(state='normal')
    error_box.destroy()
    print("box is closed")

def f_error_box():
    print("error_box is running")
    text_error_url = "Вы ввели некорректную ссылку.\nПример корректной ссылки:\nhttps://www.youtube.com/watch?v=YIEvDwq41OY\n"
    error_box.insert("1.0", text_error_url)
    error_box.get("1.0", "end")
    error_box.configure(state='disabled')
    error_box.pack(pady = (15,0))
    print("error_box is end")



tk.set_default_color_theme("dark-blue")

win = tk.CTk()
win.geometry("300x400")
win.title("Video Downloader")
win.configure(fg_color="#FCE6E6")

input = tk.CTkEntry(win, border_color="#FFD1D1", placeholder_text="Введите ссылку:")
input.pack(pady=(20,5), anchor = "center")

button = tk.CTkButton(win, text= "Скачать", command=lambda: download(input.get()))
button.pack(pady=5)

label = tk.CTkLabel(win, text = "by shekspii", text_color="grey")
label.pack(side = "bottom", pady = 5)

error_box = tk.CTkTextbox(win, width=260, height=80, text_color="red", activate_scrollbars=False)
print("Programm is run")
win.mainloop()