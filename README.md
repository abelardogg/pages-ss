# pages-ss
web pages screenshot app

## setup
- download [chrome dirver](https://chromedriver.chromium.org/downloads) and put it on the root of the project.
- Install the [Selenium library](https://pypi.org/project/selenium/) (you will need pip installed).
- create ss directory in root.
- create `config.ini` file in root.


## config.ini
These are the properties that are needed for run the app
- list: this property contains the list of urls, they should be in json format separated by two commas (see the example)

```
[URLS]
list= {"key": "KEY1", "url": "https://www.sample.com/"},,{"key": "KEY2", "url": "https://www.sample.com/search?q=test"}
```
