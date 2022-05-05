# pages-ss
web pages screenshot app

## setup
- download [chrome dirver](https://chromedriver.chromium.org/downloads) and put it on the root of the project.
- Install the [Selenium library](https://pypi.org/project/selenium/) (you will need pip installed)
- create ss directory in root

## URLS list
page_list is a objects list of urls that will be inspected. It should look like this.
```py
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
```