from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com.br/SSD-SATA3-120GB-Kingston-SA400S37/dp/B01N6JQS8C/ref=asc_df_B01N6JQS8C/?tag=googleshopp00-20&linkCode=df0&hvadid=379713309483&hvpos=&hvnetw=g&hvrand=11063542056456285281&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1031586&hvtargid=pla-318932234081&psc=1")

# Exemplo por id
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# Exemplo por xpath
# xpath = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]')
# print(xpath.text)

# Exemplo por Class name
# classname = driver.find_element_by_class_name("priceBlockBuyingPriceString")
# print(classname.text)

#Exemplo por name (Barra Search)
name = driver.find_element_by_name("url")
# print(name.get_attribute("style")) #colocar nome do atributo ex: name, style, placeholder
print(name.tag_name)

###########################################################################################################

#fecha apenas a aba atual
# driver.close()

# fecha o navegador
driver.quit()