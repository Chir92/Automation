from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\chira\\Documents\\Driver\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/?stype=lo&jlou=AffHB2iVYgvpVVdBy8uKsy-D-l0zuJLkTvAAbS8CcK4ANSJbvDsv1TNjqbn2Tm2-QKF-GQngbJMutDAfeZzbmHIKunquM-bwASuH3fzROxa_CA&smuh=24460&lh=Ac_oMAZhcK242n5nIJc")
driver.find_element(By.XPATH, ("//html[@id='facebook']//input[@id='email']")).send_keys("chiragpatel747@gmail.com")
driver.find_element(By.XPATH, ("//html[@id='facebook']//input[@id='pass']")).send_keys("venkatesh@006!")
driver.find_element(By.XPATH, ("//html[@id='facebook']//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")).click()
driver.find_element(By.XPATH, ("//html[@id='facebook']//div[@class='m9osqain a5q79mjw jm1wdb64 k4urcfbm']//span")).click()
driver.find_element(By.XPATH, ("//html[@id='facebook']//div[@class='_5rpb']//div[@class='_1mf _1mj']")).send_keys("HI")
driver.find_element(By.XPATH, ("//html[@id='facebook']/body/div[1]/div/div[1]//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/form[@method='POST']/div/div[1]/div/div/div[3]/div[2]/div[@role='button']/div[2]")).click()
