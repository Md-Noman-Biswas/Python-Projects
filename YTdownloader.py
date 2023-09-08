from pytube import YouTube
from sys import argv

url = input("Enter the link: ")

link = url

try:
    yt = YouTube(link)
    print("Title:", yt.title)
    print("Views:", yt.views)
    
    yd = yt.streams.get_highest_resolution()
    yd.download('D:/YT downloads')
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
