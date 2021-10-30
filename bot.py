import ClointFusion as Cf
import pytube
from pytube import YouTube
import os
from tqdm import tqdm
import time
import urllib.request
import xlrd
import xlsxwriter
import array


#def progress_check(stream = None, chunk = None, file_handle = None, remaining = None, file_size = "MB"):
#   percent = (100*(file_size-remaining))/file_size
#   print(f"{percent:00.00}% downloaded")

copy = Cf.excel_copy_range_from_sheet(excel_path="", startCol=0, startRow=0, endRow=0, endCol=0)
print(copy)

def file_path():
    home = os.path.expanduser('~')
    downlod_path = os.path.join(home, 'C:\Python39')
    return downlod_path


def progress_func(self, chunk, bytes_remaining):
    for i in tqdm(range(100),desc="downloading...", ascii=False, ncols=75):
        time.sleep(0.01)

def complete_func(self, file_path):
    excel = Cf.excel_set_single_cell(excel_path="", sheet_name="Sheet1", header=0, columnName="status", cellNumber=0, setText="")
    print(excel)


def my_proxies():
    pass
## here use downlaoding function also using for loop for multiple vidoes downloade in single click
for i in range(len(copy)):

    def download(copy):
        print('specific url:', copy[0])
        print("Your video will saved to: {}".format(file_path()))
        print("Accessing Youtube URL....")
        youtube = pytube.YouTube(copy[0], on_progress_callback=progress_func, on_complete_callback=complete_func, use_oauth=False, allow_oauth_cache=True)
        video = youtube.streams.first()
        title = video.title
        print("Fetching:{}...".format(title))
        video.download('C:\Python39')
        print("download is completed...")
        print("Ready to Download another video. \n\n")


    download(copy[i])
