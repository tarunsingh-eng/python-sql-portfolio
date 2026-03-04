import pytube

link = input("https://www.youtube.com/watch?v=wm86VOSf3rc")
video_download = pytube.YouTube(link)
video_download.streams.first().download()
print('Video Downloaded', link)