from pytube import YouTube
SAVE_PATH="E:/"
link="https://www.youtube.com?v=xWOoBJUqlbI"
try:
    yt=YouTube(link)
except:
    print("Connection Error")
files=yt.filter('mp4')
yt.set_filename("Videoplayback")
video=yt.get(files[-1].extension,files[-1].resolution)
try:
    video.download(SAVE_PATH)
except:
    print("Error")
print("Task Completed")
