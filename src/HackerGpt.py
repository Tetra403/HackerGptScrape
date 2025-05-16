from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
from colorama import Fore, Style
import pyfiglet
import time
import os
import sys
import logging

# Logger Setup
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Color Aliases
R, B, G, BL, C, Y, RESET = Fore.RED, Fore.BLUE, Fore.GREEN, Fore.BLACK, Fore.CYAN, Fore.YELLOW, Style.RESET_ALL

class HackerGPTBuilder:
    def __init__(self, base_url: str, headless: bool = True):
        self.base_url = base_url
        self.driver = self._init_driver(headless)

    def _init_driver(self, headless: bool) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless")
        try:
            driver = webdriver.Chrome(options=options)
            logging.info("Chrome WebDriver initialized.")
            return driver
        except Exception as e:
            logging.critical(f"{R}WebDriver başlatılamadı: {e}{RESET}")
            sys.exit(1)

    def display_logo(self):
        logo = pyfiglet.figlet_format("HACKERGPT")
        print(R + logo + RESET)

    def open_page(self):
        try:
            self.driver.get(self.base_url)
            logging.info("Siteye başarıyla bağlanıldı.")
            time.sleep(2)
        except Exception as e:
            logging.error(f"{R}Site bağlantı hatası: {e}{RESET}")
            self.cleanup()
            sys.exit(1)

    def login(self, username: str, password: str):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log In']"))).click()

            self.driver.find_element(By.ID, "email").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "loginBtnText").click()

            logging.info("Giriş başarılı.")
            time.sleep(2)
        except Exception as e:
            logging.error(f"Giriş sırasında hata oluştu: {e}")
            self.cleanup()
            sys.exit(1)

    def create_project(self, prompt: str):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.element_to_be_clickable((By.ID, "menuToggle"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='nav-link'])[2]"))).click()

            self.driver.find_element(By.ID, "prompt").send_keys(prompt)
            print(f"{C}Proje oluşturuluyor, lütfen bekleyin...{RESET}")
            time.sleep(2)

            wait.until(EC.element_to_be_clickable((By.ID, "buildBtn"))).click()
            time.sleep(10)  # Builder süresi

            self._download_result(wait)
        except TimeoutException:
            logging.error("İlgili butonlar zamanında yüklenmedi.")
        except Exception as e:
            logging.error(f"Proje oluşturma hatası: {e}")

    def _download_result(self, wait: WebDriverWait):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            page_html = self.driver.page_source
            soup = BeautifulSoup(page_html, "html.parser")
            status_message = soup.find("div", {"id": "statusMessage"})

            if status_message and "Tool created successfully! 100%" in status_message.text.strip():
                download_btn = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@class, 'btn-primary') and contains(text(), 'Download')]")
                ))
                download_btn.click()
                print(f"{G}Proje başarıyla indirildi!{RESET}")
            else:
                print(f"{Y}Uyarı: Başarı mesajı bulunamadı veya eşleşmiyor!{RESET}")
        except Exception as e:
            print(f"{R}Hata: İndirme işlemi başarısız. Detay: {e}{RESET}")

    def cleanup(self):
        if self.driver:
            self.driver.quit()
            logging.info("Tarayıcı kapatıldı.")

def main():
    os.system("cls" if os.name == "nt" else "clear")

    builder = HackerGPTBuilder(base_url="https://hackergpt.se7eneyes.org/builder7e", headless=True)
    builder.display_logo()

    try:
        prompt = input(f"{B}Lütfen Prompt girin: {RESET}").strip()
        if not prompt:
            raise ValueError("Prompt boş olamaz.")

        print(f"{Y}Proje oluşturuluyor ve indiriliyor...{RESET}")
        builder.open_page()
        builder.login(username="tetra", password="Hecibaba.1")
        builder.create_project(prompt=prompt)
    finally:
        builder.cleanup()

if __name__ == "__main__":
    main()
