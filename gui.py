import yt_dlp
import tkinter as tk

def download_video(url_string):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'preferredcodec[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'cookiefile': 'cookies.txt',
        'writethumbnail': True,
        'embedthumbnail': True,
        'destination': '/files'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_string.get()])

    print("Download completed.")



window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry('400x250')
window.configure(bg='lightblue')

url_string = tk.StringVar(value="Enter video URL here")
url_label = tk.Label(window, text="Enter the video URL:").grid(row=0)
url_entry = tk.Entry(window, textvariable=url_string).grid(row=0, column=1)

button = tk.Button(window, text="Click Download to start downloading the video.", command=lambda: download_video(url_string)).grid(row=1)



# Quit
button = tk.Button(window, text="Quit", command=window.destroy).grid(row=2)
# Start the GUI event loop
window.mainloop()
