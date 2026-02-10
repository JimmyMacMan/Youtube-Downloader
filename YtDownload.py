import yt_dlp
  

url = input("Enter the video URL: ")

ydl_opts= {'outtmpl': '%(title)s.%(ext)s',  "format": 'preferredcodec[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            , 'cookiefile': 'cookies.txt','writethumbnail': True,'embedthumbnail': True, 'destination': '/files'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("Download completed.")
