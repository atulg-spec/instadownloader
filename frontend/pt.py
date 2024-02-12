from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

print(stream.url)
