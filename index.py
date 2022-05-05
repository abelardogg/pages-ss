import time
import datetime
import modules.utils as utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



pages_list = [{"key": "HOME", "url": "https://www.1aauto.com/"}, 
{"key": "SEARCH", "url": "https://www.1aauto.com/search?q=mirror"},
{"key": "PDP", "url": "https://www.1aauto.com/toyota-lexus-front-and-rear-ceramic-brake-pad-and-rotor-kit-trq-bka11763/i/1abfs02636"},
{"key": "PDP_TOOL", "url": "https://www.1aauto.com/disc-brake-service-kit-50-state-formula/i/1avck00001"},
{"key": "PARTS", "url": "https://www.1aauto.com/catalog/parts"},
{"key": "GRANDPA_CATEGORIES", "url": "https://www.1aauto.com/brakes-wheel-bearing/c/508"},
{"key": "CATEGORIES", "url": "https://www.1aauto.com/abs-wheel-speed-sensor/c/133"},
{"key": "MAKES", "url": "https://www.1aauto.com/catalog/makes"},
{"key": "MAKE_RP", "url": "https://www.1aauto.com/infiniti-parts/ma/19"},
{"key": "MODEL", "url": "https://www.1aauto.com/infiniti-q60-parts/mo/2199"},
{"key": "YEAR_MODEL", "url": "https://www.1aauto.com/2016-infiniti-qx70-parts/y-mo/2016-2127"},
{"key": "MODEL_CATEGORY", "url": "https://www.1aauto.com/infiniti-q60-headlights-lighting/mo-c/2199-275"},
{"key": "YEAR_MODEL_CATEGORY", "url": "https://www.1aauto.com/2017-infiniti-q60-steeringsuspension/y-mo-c/2017-2199-509"},
{"key": "BRANDS", "url": "https://www.1aauto.com/catalog/brands"},
{"key": "BRAND_RP", "url": "https://www.1aauto.com/acdelco-parts/b/3"},
{"key": "BRAND_CATEGORY", "url": "https://www.1aauto.com/acdelco-belts-serpentine-belts-and-v-belts/b-c/3-192"},
{"key": "TRACKING", "url": "https://www.1aauto.com/tracking"},
{"key": "CONTACT", "url": "https://www.1aauto.com/about/contact"},
{"key": "RETURNS", "url": "https://www.1aauto.com/customer-service/returns"},
{"key": "VIDEOS_HOME", "url": "https://www.1aauto.com/videos"},
{"key": "VIDEOS_SEARCH", "url": "https://www.1aauto.com/search/videos?year=2018&model=271&videoSearchType=ymm"},
{"key": "VIDEO_DETAIL", "url": "https://www.1aauto.com/how-to-reset-oil-life-maintenance-reminder-2015-20-cadillac-escalade/video/46823"},
{"key": "VIDEOS_MAKE", "url": "https://www.1aauto.com/jeep-videos/ma-videos/23"},
{"key": "VIDEOS_MODEL_RP", "url": "https://www.1aauto.com/jeep-gladiator-videos/mo-videos/441"},

]

ss_dir_path = './ss'
utils.createDir(ss_dir_path) #create the directory if doesnt exists


def take_screenshot(page_name, file_key, screen_size):
	current_date = datetime.datetime.now()
	screenshot_name = f"{file_key}--{current_date.year}-{current_date.month}-{current_date.day}--{current_date.microsecond}"
	
	outuptDir = f'{ss_dir_path}/{file_key}'
	utils.createDir(outuptDir)


	print(f'\n\n *** Attempting to create screenshot for {file_key} with the name {screenshot_name} *** \n\n')

	options = Options()
	options.add_argument("--headless")
	options.add_argument(screen_size)

	driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver', service_args=["--log-path=./Logs/DubiousDan.log"])


	driver.get(page_name)
	time.sleep(2) # Let the user actually see something!
	
	try:
		popup = driver.find_element(By.CSS_SELECTOR, '#ltkpopup-close-button .ltkpopup-close')
		if(popup.size['width']>0):
			popup.click()
	except:
		print("probably the popup doesnt exists")

	el = driver.find_element(By.TAG_NAME,'body')
	el.screenshot(f'{outuptDir}/{screenshot_name}.png')
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