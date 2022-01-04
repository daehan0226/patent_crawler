import json

config = {
    "home_url": "http://www.kipris.or.kr/khome/main.jsp",
    "search_url": "http://kpat.kipris.or.kr/kpat/searchLogina.do?next=MainSearch",
    "search_data" : {
        "GD": "[20100101~20211231]"
    },
    "search_claim_check_list": ["특허"],
    "search_release_check_list": ["등록"],
    "search_release_check_all": ["전체"],
    "search_sort" : "등록일자",
    "log_dir": "./logs/",
    "driver": "./chromedriver.exe",
    "wait": 1,
    "create_file_wait": 60,
    "download_count_at_once": 5000,
    "elements": {
        "login_popup_button" :  ["xpath", "//*[@id='btnLogin']"],
        "email_input" : ["xpath", "//*[@id='login_id']"],
        "password_input" : ["xpath", "//*[@id='login_pw']"],
        "login_button": ["xpath", "//*[@id='btn_login']"],
        "search_tab_button" : ["xpath", "//*[@id='btnToggleSmartFinder']"],
        "search_input": ["xpath", "//*[@id='queryText']"],
        "search_button": ["css", ".input_btn"],
        "search_claim_checkboxes": ["css", ".claim_area"],
        "search_release_checkboxes": ["css", ".release_area"],
        "search_sort_list": ["xpath", "//*[@id='liSort_1']"],
        "search_sort_desc": ["xpath", "//*[@id='btnSortOrderDesc_1']"],
        "search_sort_asc": ["xpath", "//*[@id='btnSortOrderAsc_1']"],
        "total_count": ["css", ".total"],
        "download_popup_button": ["xpath", "//*[@id='aside']/section[1]/ul[2]/li[5]/a"],
        "select_options": ["xpath", "//*[@id='source']"],
        "select_move_button": ["css", ".btn_add"],
        "download_index_from_input": ["xpath", "//*[@id='from_val']"],
        "download_index_to_input": ["xpath", "//*[@id='to_val']"],
        "create_file_button": ["xpath", "//*[@id='divCreateButton']/span/button"],
        "download_button": ["xpath", "//*[@id='divDownButton']/span/button"]
    },
    "download_data_list": [
        "요약",
        "법적상태",
        "청구항",
        "등록번호",
        "등록일자",
        "출원번호",
        "출원일자",
        "발명의명칭",
        "출원인",
        "IPC분류",
        "CPC분류"
    ]
}

with open("./config/credentials.json", encoding="utf-8") as json_file:
    config["credentials"] = json.load(json_file)
