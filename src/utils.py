import time
import os

def gen_search_query(params):
    query = ""
    for k, v in params.items():
        query += f"{str(k)}={str(v)}*"
    return query[:-1]


def download_wait(path_to_downloads, download_wait):
    dl_wait = True
    second = 0
    while dl_wait and second < download_wait:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        second += 1