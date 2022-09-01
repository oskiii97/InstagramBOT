from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from secrets import login, password

url='https://instagram.com/'


class Bot():
    def __init__(self):
        self.login(login,password)

    def login(self, login, password):
        self.driver = webdriver.Chrome()      #driver
        self.driver.get(url) #get url to driver
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
        username_input= self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(login)
        password_input= self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def whoNotfollowYou(self):
        print("")



def main():
    my_bot = Bot()

if __name__ == '__main__':
    main()
