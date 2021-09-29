from selenium import webdriver

class WebDriverChrome(object):

    def __init__(self):
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=chrome_options)
        with open('./stealth.min.js') as f:
            js = f.read()
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": js
            })
        return driver

    def RunStart(self):
        self.driver.get('https://bot.sannysoft.com')
        # time.sleep(10)
        # self.driver.quit()


if __name__ == '__main__':
    dri = WebDriverChrome()
    dri.RunStart()

