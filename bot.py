import xlrd
from ClointFusion import ClointFusion as Cf
import pytube
from pytube import YouTube
import os
from tqdm import tqdm
import time
import urllib.request
import xlrd
import xlsxwriter


#def progress_check(stream = None, chunk = None, file_handle = None, remaining = None, file_size = "MB"):
#   percent = (100*(file_size-remaining))/file_size
#   print(f"{percent:00.00}% downloaded")



def file_path():
    home = os.path.expanduser('~')
    downlod_path = os.path.join(home, 'C:\Python39')
    return downlod_path
copy =str(Cf.excel_copy_range_from_sheet(excel_path="", startCol=0, startRow=0, endRow=0, endCol=0))
print(copy)
# browser = Cf.browser_activate(url:= "https://www.youtube.com/",
#                      files_download_path:= 'C:\Python39
#                      dummy_browser:= True,
#                      open_in_background:= False,
#                      incognito:= False,
#                      clear_previous_instances:= False,
#                      profile:= "Default")
#link = Cf.gui_get_any_input_from_user("")
#write = Cf.browser_write_h(Value:= link, User_Visible_Text_Element:= "Search")
#enter = Cf.browser_hit_enter_h()
#webUrl = urllib.request.urlopen('link')

#drag = Cf.mouse_move(x=300,y=300)
#click = Cf.browser_mouse_click_h(User_Visible_Text_Element:=link,element:= "1",double_click:= False,right_click:= True)

def progress_func(self, chunk, bytes_remaining):
    for i in tqdm(range(100),desc="downloading...", ascii=False, ncols=75):
        time.sleep(0.01)
def complete_func(self, file_path):
    pass
def my_proxies():
    pass

def download():
    global copy

    x=0;
    while x < len(copy):
        print(copy[x])
        print("Your video will saved to: {}".format(file_path()))
        print("Accessing Youtube URL....")
        youtube = pytube.YouTube(copy, on_progress_callback=progress_func, on_complete_callback=complete_func, use_oauth=False, allow_oauth_cache=True)
        video = youtube.streams.first()
    #video.stream_to_buffer(buffer=1).filter(progressive=True, file_extension="mp4", file_size=MB)
    #video.order_by(resolution)
        title = video.title
        print("FEtching:{}...".format(title))
        video.download('C:\Python39')
        print("download is completed...")
        print("Ready to Download another video. \n\n")
        x =+1
download()
Cf.excel_set_single_cell(excel_path="", sheet_name="", header=0, columnName="", cellNumber=0, setText="")

#aa = Cf.excel_describe_data(excel_path="C:\Python39", sheet_name='Sheet1', header=0)
