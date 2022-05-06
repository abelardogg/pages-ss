import time
import datetime
import modules.utils as utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

pages_list = config['URLS']['list']
pages_list = pages_list.split(',,')

ss_dir_path = './ss'
utils.createDir(ss_dir_path) #create the directory if doesnt exists


def take_screenshot(page_name, file_key, device_type, screen_size):
	current_date = datetime.datetime.now()
	screenshot_name = f"{file_key}--{current_date.year}-{current_date.month}-{current_date.day}--{device_type}"
	
	outuptDir = f'{ss_dir_path}/{file_key}'
	utils.createDir(outuptDir)


	print(f'\n\n *** Attempting to create screenshot for {file_key} with the name {screenshot_name} *** \n\n')

	options = Options()
	options.add_argument("--headless")
	options.add_argument(screen_size)
	options.add_argument('log-level=2')

	driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver', service_args=["--log-path=./Logs/DubiousDan.log"])


	driver.get(page_name)
	# print('ncookie PRE')
	# print(driver.get_cookie("ApplicationGatewayAffinity"))
	# print(driver.get_cookie("ApplicationGatewayAffinityCORS"))
	
	
	driver.add_cookie({"name": "ApplicationGatewayAffinity", "value": "ed56ad980dd6de285a1aa9141afb565c"})
	driver.add_cookie({"name": "ApplicationGatewayAffinityCORS", "value": "ed56ad980dd6de285a1aa9141afb565c"})
	driver.refresh()
	# print('ncookie POST')
	# print(driver.get_cookie("ApplicationGatewayAffinity"))
	# print(driver.get_cookie("ApplicationGatewayAffinityCORS"))

	#time.sleep(2) # Let the user actually see something!
	
	try:
		popup = driver.find_element(By.CSS_SELECTOR, '#ltkpopup-close-button .ltkpopup-close')
		if(popup.size['width']>0):
			popup.click()
	except:
		print("\n\n INFO: probably the popup doesnt exists \n\n")


	try:
		el = driver.find_element(By.TAG_NAME,'html')
		el.screenshot(f'{outuptDir}/{screenshot_name}.png')
		print(f'\n\n ***Screenshot: {screenshot_name} successfully saved *** \n\n')
	except:
		print("\n\n There was a problem while trying to take the screenshot using <html> tag. \n\n")

	driver.quit()

for page in pages_list:
	page_json = json.loads(page)
	# desktop
	take_screenshot(page_json['url'], page_json['key'], 'D', "window-size=1400,10000")

	# mobile
	take_screenshot(page_json['url'], page_json['key'], 'M', "window-size=414,10000")

print("\n\n")
print("====================================")
print("\n All screenshot done \n")
print("====================================")