import time
from src.modules.driver_manager import DriverManager
from src.modules.logger import Logger
from src.utils import gen_search_query, download_wait
from config.config import config


def run_crawler():
    logger = Logger("crawler")
    try:
        # Load webpage    
        crawler = DriverManager(logger)
        crawler.get(config["home_url"])
        crawler.raise_error_if_wrong_page(config["home_title"])
        elements = config["elements"]

        # Login
        crawler.click_button(elements["login_popup_button"])
        crawler.switch_tab(1)
        credentials = config["credentials"]
        crawler.send_text_to_input(elements["email_input"], credentials["email"])
        crawler.send_text_to_input(elements["password_input"], credentials["password"])
        crawler.click_button(elements["login_button"])
        crawler.switch_tab(0)

        # Search - query / filter(checkbox) / sort 
        crawler.get(config["search_url"])
        crawler.send_text_to_input(
            elements["search_input"], 
            gen_search_query(config["search_data"]))
        crawler.click_checkbox_label(
            elements["search_claim_checkboxes"], 
            config["search_claim_check_list"])
        crawler.click_checkbox_label(
            elements["search_release_checkboxes"], 
            config["search_release_check_list"], 
            check_all_element_text=config["search_release_check_all"])
        crawler.select_sort(
            elements["search_sort_list"],
            config["search_sort"],
            elements["search_sort_desc"]
        )
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

        download_wait(config["download_dir"], config["download_wait"])
    except Exception as e:
        logger.error(e)
    finally:
        crawler.quit()