from Crawler import Crawler
from config.config import config


def run_crawler():
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

    # Download
    crawler.click_button(elements["download_popup_button"])
    crawler.switch_tab(1)
    crawler.select_options(
        elements["select_options"],
        config["download_data_list"],
        elements["select_move_button"],
    )

    crawler.quit()


if __name__ == "__main__":
    run_crawler()
