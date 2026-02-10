import yt_dlp

option = input("Please chose one:\n" 
"1) Single Downlaod\n" 
"2) Multi Download\n") 
url=""
if option =="1":
    url = input("Enter the video URL: ")

    ydl_opts= {'outtmpl': 'files/%(title)s.%(ext)s',  "format": 'preferredcodec[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            , 'cookiefile': 'cookies.txt','writethumbnail': True,'embedthumbnail': True, 'destination': '/files'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download completed.")
if option =="2":

    option_loop=""
    download_queue=[]
    
    while option_loop != "Done":

        option_loop=input("Enter the video URL\n" \
        "Done to Download\n")
        if download_queue != "Done":
            download_queue.append(option_loop)
    
    for i in download_queue:
        ydl_opts= {'outtmpl': 'files/%(title)s.%(ext)s',  "format": 'preferredcodec[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            , 'cookiefile': 'cookies.txt','writethumbnail': True,'embedthumbnail': True, 'destination': '/files'}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])





else:
    print("Try Again!")
