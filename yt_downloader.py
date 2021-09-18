#!/usr/bin/env python
"""Download youtube's video

"""

from pytube import YouTube
import os

__author__ = "Bebeshen"
__version__ = "1.0.0"
__maintainer__ = "Bebeshen"
__email__ = "Bebeshen@gmail.com"
__status__ = "Production"

# vsize = 0
# def percent(tem, total):
#     perc = (float(tem) / float(total)) * float(100)
#     return perc
# def progress_function(chunk, file_handle, bytes_remaining):
#     global vsize
#     p = 0
#     progress = p
#     p = percent(vsize-bytes_remaining, vsize)
#     file_handle.write(chunk)
#     print('%.1f%s \r' % (p,"%")),

link = input("[+] Enter the link: ")
yt = YouTube(link)
downloadType = input("[+] What is type you want to download? Video or Audio (Type `mp4` or `mp3`): ")

filename = yt.title
#Title of video
print("[+] Title: ",yt.title)
#Number of views of video
print("[+] Number of views: ",yt.views)
#Length of the video
print("[+] Length of video: ",yt.length,"seconds")
#Description of video
print("[+] Description: ",yt.description)
#Rating
print("[+] Ratings: ",yt.rating)
print()

#printing all the available streams
#with filter that only video
print(yt.streams.filter(only_video=True))

#
print(yt.streams.filter(progressive=True))

# get highest 
ys = yt.streams.get_highest_resolution()
vsize = ys.filesize

#Starting download
print("[+] Downloading...")
outfile = ys.download(os.getcwd())

if downloadType == "mp3":
    base, ext = os.path.splitext(outfile)
    new_file = base + '.mp3'
    os.rename(outfile, new_file)
    
print("[+] Download completed!!")