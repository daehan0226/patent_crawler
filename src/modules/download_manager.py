import time
import os
import shutil
from os import path
from datetime import datetime

class downloadManager():

    def __init__(self, download_dir):
        self.download_dir = download_dir
    
    def wait_for_download_complete(self, wait_time):
        dl_wait = True
        second = 0
        while dl_wait and second < wait_time:
            time.sleep(1)
            dl_wait = False
            for fname in os.listdir(self.download_dir):
                if fname.endswith('.crdownload'):
                    dl_wait = True
            second += 1
    
    def move_downloaded_files(self, target_dir):
        today = datetime.now().strftime('%Y%m%d')
        file_extension = '.xls'
        
        for fname in os.listdir(self.download_dir):
            if fname.startswith(today) and fname.endswith(file_extension):
                shutil.move(path.join(self.download_dir, fname), path.join(target_dir, fname))