import os
import time
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN = float(os.environ.get("PROMISED_DOWN", 150))
PROMISED_UP = float(os.environ.get("PROMISED_UP", 10))
Email = os.environ.get("TWITTER_EMAIL", "")
Password = os.environ.get("TWITTER_PASSWORD", "")


# driver.get("https://app.100daysofpython.dev/services/y")
# #Logging in Google
# Allow_Biscuits= driver.find_element(By.XPATH, value='//*[@id="y-cookie-banner"]/button')
# Allow_Biscuits.click()
# time.sleep(2)
# Login= driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/a[4]')
# Login.click()
# time.sleep(2)
# #Giving Email and PASS
# Email= driver.find_element(By.XPATH, value='//*[@id="email"]')
# Pass=driver.find_element(By.XPATH, value='//*[@id="password"]')
# Email.send_keys("dibyasarothidibya@gmail.com")
# Pass.send_keys("3hspJg7wbqaoxLvB")
# Login= driver.find_element(By.XPATH, value='/html/body/div[1]/div/form/button')
# Login.click()

#Creating the definitions

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down= 0
        self.up= 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        # Handle cookie consent overlay if it appears
        try:
            consent_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            consent_button.click()
            time.sleep(2)
        except Exception:
            pass

        go_button = self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test")
        go_button.click()
        
        # Wait up to 120 seconds (polling every 3 seconds) for speed test completion
        for _ in range(40):
            time.sleep(3)
            try:
                download_element = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
                upload_element = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
                # Parse as floats to ensure speeds are fully calculated and not placeholders like '' or '-'
                float(download_element.text)
                float(upload_element.text)
                self.down = download_element.text
                self.up = upload_element.text
                break
            except (ValueError, Exception):
                continue





    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y")

    # Cookie banner
        self.driver.find_element(By.XPATH, value='//*[@id="y-cookie-banner"]/button').click()
        time.sleep(2)

    # Go to login
        self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/a[4]').click()
        time.sleep(2)

    # Enter credentials
        self.driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(Email)
        self.driver.find_element(By.XPATH, value='//*[@id="password"]').send_keys(Password)
        self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/form/button').click()
        time.sleep(2)

        # Compose the post
        Post = self.driver.find_element(By.XPATH, value='/html/body/div[1]/nav/button')
        Post.click()
        time.sleep(2)

        compose_box = self.driver.find_element(By.XPATH, value='//*[@id="modal-compose"]')
        compose_box.click()
        time.sleep(1)

        tweet_text = (
            f"Hey Internet Provider, why is my internet speed "
            f"{self.down}Mbps down / {self.up}Mbps up when I pay for "
            f"{PROMISED_DOWN}Mbps down / {PROMISED_UP}Mbps up?"
        )
        compose_box.send_keys(tweet_text)
        posting=self.driver.find_element(By.XPATH, value='//*[@id="modal-post-btn"]')
        posting.click()
        pass

















bot = InternetSpeedTwitterBot()
bot.get_internet_speed()      # opens speedtest.net, runs test, saves self.down/self.up
print(f"Download Speed: {bot.down}")
print(f"Upload Speed: {bot.up}")
bot.tweet_at_provider() 