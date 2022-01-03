import time
from src.modules.Crawler import Crawler
from config.config import config


def run_crawler():
    # Load webpage
    crawler = Crawler(wait=config["wait"])
    crawler.get(config["home_url"])
    elements = config["elements"]

    # Login
    crawler.click_button(elements["login_popup_button"])
    crawler.switch_tab(1)
    credentials = config["credentials"]
    crawler.send_text_to_input(elements["email_input"], credentials["email"])
    crawler.send_text_to_input(elements["password_input"], credentials["password"])
    crawler.click_button(elements["login_button"])
    crawler.switch_tab(0)

    # Search
    crawler.get(config["search_url"])
    crawler.click_button(elements["search_tab_button"])
    crawler.send_text_to_input(elements["ad_from_input"], config["search_date_from"])
    crawler.send_text_to_input(elements["ad_to_input"], config["search_data_to"])
    crawler.click_button(elements["search_button"])

    # Total patent count
    patent_count_str = crawler.get_text(elements["total_count"])
    patent_count = int(patent_count_str.replace(",", ""))

    # Download setup
    crawler.click_button(elements["download_popup_button"])
    crawler.switch_tab(1)
    crawler.select_options(
        elements["select_options"],
        config["download_data_list"],
        elements["select_move_button"],
    )

    # Download loop
    download_index_from = 1
    download_count_at_once = config["download_count_at_once"]
    while download_index_from < int(patent_count):
        crawler.send_text_to_input(
            elements["download_index_from_input"], download_index_from
        )
        crawler.send_text_to_input(
            elements["download_index_to_input"],
            download_index_from + (download_count_at_once - 1),
        )

        crawler.click_button(elements["create_file_button"])
        crawler.wait_for_alert(config["create_file_wait"])
        crawler.click_button(elements["download_button"])
        download_index_from += download_count_at_once

    crawler.quit()
