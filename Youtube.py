from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\chira\\Documents\\Driver\\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH, ("//div[@id='search-input']/input[@id='search']")).send_keys("hope by chainsmokers")
driver.find_element(By.XPATH, ("//button[@id='search-icon-legacy']/yt-icon[@class='style-scope ytd-searchbox']")).click()
driver.find_element(By.XPATH, ("//a[@id='video-title']/yt-formatted-string[text()='The Chainsmokers - Hope ft. Winona Oak (Lyric Video)']")).click()

