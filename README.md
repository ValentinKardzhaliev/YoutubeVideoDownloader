# YoutubeVideoDownloader
A simple python script used to download videos from Youtube using the library pytube

By default the resolution the video will be downloaded in is the highest available, but you can change that if you wish by replacing the following line of code:
yd = yt.streams.get_highest_resolution()

to:

- yd = yt.streams.get_by_resolution("720p")
You can put any resolution you wish instead in the brackets

- yd = yt.streams.get_audio_only()
- This will give you only the audio of the video

- yd = yt.streams.get_lowest_resolution()
- This will download the video in the lowest available resolution

