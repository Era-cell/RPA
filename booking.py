import os
import testing.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"E:\RPA\Web_Automation",teardown=False):
        self.driver_path=driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        opts.add_experimental_option('excludeSwitches',['enable-logging'])
        super(Booking,self).__init__(options=opts)
        self.implicitly_wait(3)
        self.wait = WebDriverWait(self,10)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self .teardown:
            self.quit()

    def pop_clear(self):
        try:
            btn = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Dismiss sign in information."]'
            )
            btn.click()
        except:
            print('No pop up...')
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.pop_clear()

    def change_currency(self):
        currency = self.find_element(
            By.CSS_SELECTOR,
            'button[class="a83ed08757 c21c56c305 f38b6daa18 f671049264 deab83296e fd3248769f"]'
        )

        selected_currency = self.find_element(
            By.CSS_SELECTOR,
            'button[class="a83ed08757 aee4999c52 ffc914f84a c39dd9701b ac7953442b"]'
        )

        currency.click()
        selected_currency.click()

    def select_palce(self,place):
        text_fld = self.find_element(
            By.ID,':re:'
        )

        text_fld.clear()
        text_fld.send_keys(place)
        first_element = self.find_element(
            By.CLASS_NAME,
            "a72ed04875"
        )

        print(first_element)

    def dates(self):
        open_tab = self.find_element(
            By.CLASS_NAME,
            "d606c76c5a"
        )
        open_tab.click()

        select1 = self.find_element(
            By.CSS_SELECTOR,
            'span[data-date="2023-09-12"]'
        )
        select2 = self.find_element(
            By.CSS_SELECTOR,
            'span[data-date="2023-10-18"]'
        )
        select1.click()
        select2.click()
    def select_occupancy(self):
        o = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]'
        )

        o.click()
        adult_no= self.find_element(
            By.ID,
            "group_adults"
        )


        donebtn = self.wait.until(EC.presence_of_element_located((
            By.XPATH,
            '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div'
        )))

        donebtn.click()
        search_btn = self.find_element(
            By.XPATH,
            '/html/body/div[3]/div[2]/div/form/div[1]/div[4]/button/span'
        )

        search_btn.click()

    def report_results(self):
        results = self.find_elements(
            By.CLASS_NAME,
            "c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 da89aeb942"
        )
        print(results)
        # document.getElementsByClassName("c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 da89aeb942")

        return len(results)