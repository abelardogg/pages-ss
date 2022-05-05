import time
import datetime
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



pages_list = [{"key": "HOME", "url": "https://www.1aauto.com/"}, 
{"key": "SEARCH", "url": "https://www.1aauto.com/search?q=mirror"}]


def take_screenshot(page_name, file_key, screen_size):
	current_date = datetime.datetime.now()
	screenshot_name = f"{file_key}--{current_date.year}-{current_date.month}-{current_date.day}--{current_date.microsecond}"
	
	print(f'\n\n *** Attempting to create screenshot for {file_key} with the name {screenshot_name} *** \n\n')

	options = Options()
	options.add_argument("--headless")
	options.add_argument(screen_size)

	# driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

	driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver', service_args=["--log-path=./Logs/DubiousDan.log"])


	driver.get(page_name);
	time.sleep(2) # Let the user actually see something!
	
	try:
		popup = driver.find_element(By.CSS_SELECTOR, '#ltkpopup-close-button .ltkpopup-close')
		if(popup.size['width']>0):
			popup.click()
	except:
		print("probably the popup doesnt exists")

	el = driver.find_element(By.TAG_NAME,'body')
	el.screenshot(f'./ss/{screenshot_name}.png')
	print(f'\n\n ***Screenshot: {screenshot_name} succsefully saved *** \n\n')
	driver.quit()

for page in pages_list:
	# desktop
	take_screenshot(page['url'], page['key'], "window-size=1400,10000")

	# mobile
	take_screenshot(page['url'], page['key'], "window-size=414,10000")

print("\n\n")
print("====================================")
print("\n All screenshot done \n")
print("====================================")