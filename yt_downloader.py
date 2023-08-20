from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

yd = yt.streams.get_highest_resolution() # You can set lower resolutions too. Go to README if you wish to know more

yd.download("Downloads" # Provide the path you wish to download the video to
