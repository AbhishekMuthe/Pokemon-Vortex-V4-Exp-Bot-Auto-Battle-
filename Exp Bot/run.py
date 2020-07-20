import re #created by Abhishek Muthe
import scrapy
import details
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from scrapy.selector import Selector
from time import sleep
from selenium.webdriver import ChromeOptions
#driver.get('chrome://settings/')
#driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')

class User():
	
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url


	def login(self):
		self.driver.maximize_window()
		self.driver.get(self.url)
		typeusername = self.driver.find_element_by_id('myusername')
		typepassword = self.driver.find_element_by_name('mypassword')
		typeusername.send_keys(details.username)
		typepassword.send_keys(details.password)
		login_acc = self.driver.find_element_by_id("submit")
		login_acc.click()
	
def battlesearch(driver):
	global i
	i = 0
	battle_url = 'https://www.pokemon-vortex.com/battle-search/'
	driver.get(battle_url)
	train = driver.find_element_by_xpath('//*[@name="buser"]')
	train.send_keys(details.training_acc)
	battle = driver.find_element_by_xpath('//*[@name="submitb"]')
	battle.click()
	while i < 6:
		try:
			sleep(0.2)
			backtoteam(driver)
			attack(driver)
			continuos(driver)
			i = i + 1
		except:
			return battlesearch(driver)
def backtoteam(driver):
	while True:
		try:
			sleep(0.2)
			sel = Selector(text=driver.page_source)
			a = sel.xpath('//*[@class="button-maroon button-small"]/@value').extract()
			r = re.compile(".*ntinu*.")
			b = list(filter(r.match, a))
			b = "".join(map(str, b))
			d = '//*[@value="foo"]'
			d = d.replace("foo", b)
			driver.execute_script("window.scrollTo(0, 1000)")
			num1 = sel.xpath('//*[@id="nojs-solve-a"]/@value').extract()
			num2 = sel.xpath('//*[@id="nojs-solve-b"]/@value').extract()
			num1 = int("".join(map(str, num1)))
			num2 = int("".join(map(str, num2)))
			num = num1 + num2
			v = driver.find_element_by_xpath('//*[@id="nojs-solve-v"]')
			v.send_keys(num)
			c = driver.find_element_by_xpath(d)
			sleep(0.2)
			c.click()
		except:
			break
	
def attack(driver):
	while True:
		try:
			sels = Selector(text=driver.page_source)
			at = sels.xpath('//*[@class="button-maroon button-small"]/@value').extract()
			r = re.compile(".*ttac*.")
			b = list(filter(r.match, at))
			b = "".join(map(str, b))
			d = '//*[@value="fooo"]'
			d = d.replace("fooo", b)
			#driver.execute_script('window.scrollTo(0, 200)')
			sleep(0.2)
			attack = driver.find_element_by_xpath(d)
			attack.click()
		except:
			break
	
def continuos(driver):
	while True:
		try:
			sleep(0.2)
			seli = Selector(text=driver.page_source)
			at = seli.xpath('//*[@class="button-maroon button-small"]/@value').extract()
			#r = re.compile(".*ntinu*.")
			#e = list(filter(r.match, at))
			f = at[1:2]
			f = "".join(map(str, f))
			g = '//*[@value="foooo"]'
			g = g.replace("foooo", f)
			t = driver.find_element_by_xpath(g)
			#driver.execute_script('window.scrollTo(0, 250)')
			sleep(0.2)
			t.click()
		except:
			break
def rebattle(driver, l):
	sleep(0.2)
	# l = driver.find_element_by_xpath('//*[@class="menu-tab"]/a')
	# l = l.get_attribute('href')
	driver.get(l)
	i = 0
	while i < 6:
		try:
			sleep(0.2)
			backtoteam(driver)
			attack(driver)
			continuos(driver)
			i = i + 1
		except:
			return rebattle(driver, l)
	return rebattle(driver, l)
	
def getlink(driver):
	global l
	l = driver.find_element_by_xpath('//*[@class="menu-tab"]/a')
	l = l.get_attribute('href')


def main():
	options = ChromeOptions()
	prefs = {'profile.managed_default_content_settings.javascript': 2}
	options.add_experimental_option('prefs', prefs)
	url = 'https://www.pokemon-vortex.com/login/'
	driver = webdriver.Chrome('Add your path here/chromedriver.exe', options=options) #Add path here with '/' slash
	user = User(driver, url)
	user.login()
	battlesearch(driver)
	getlink(driver)
	rebattle(driver ,l)

if __name__ == '__main__':
	main()
		
			
	
	
	