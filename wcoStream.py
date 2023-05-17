from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


if __name__ == '__main__':

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	#driver = webdriver.Chrome(executable_path="/home/danny/.local/myResources/chromedriver", options=options)
	driver = webdriver.Chrome(service=Service("/home/danny/.local/myResources/chromedriver"))

	driver.set_window_size(1920,1080)
	driver.get("https://www.wcostream.net/playlist-cat/60334/one-piece-episode-309-english-subbed")

	input("Press enter to quit")
