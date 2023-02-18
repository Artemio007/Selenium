import time
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPaths import binance_url_xrp_usdt, hour_1, xpath_xrp_usdt_max_price, xpath_xrp_usdt_price_now, time_req


def pars_price(url: str, max_in_h: str, xpath_max_p: str, xpath_p: str):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--enable-javascript')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    browser.get(url)
    time.sleep(2)
    browser.find_element(by=By.XPATH, value=max_in_h).click()
    time.sleep(2)
    max_price_xrp = browser.find_element(by=By.XPATH, value=xpath_max_p).text
    price_xrp = browser.find_element(by=By.XPATH, value=xpath_p).text

    header_csv = ['Time', 'price']
    if float(price_xrp) <= float(max_price_xrp) * 0.99:
        print(f"The price fell by 1 percent or more and amounted to {price_xrp}")

        dict_time_fell = {price_xrp: datetime.datetime.now()}
        with open('price_history_fell.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header_csv)
            writer.writerow(dict_time_fell)


def work():
    try:
        print("Program working")
        while True:
            pars_price(binance_url_xrp_usdt, hour_1, xpath_xrp_usdt_max_price, xpath_xrp_usdt_price_now)
            time.sleep(time_req)
    except Exception as err:
        print(err)
    finally:
        work()


if __name__ == "__main__":
    work()






