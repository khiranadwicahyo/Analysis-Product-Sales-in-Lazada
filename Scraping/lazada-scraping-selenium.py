from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import pandas as pd 
import time


urlist = []
for page in range(1,9):
    page_link = 'https://www.lazada.com.my/tag/milo/?catalog_redirect_tag=true&page={}&q=milo&spm=a2o4k.searchlist.search.d_go.64e97cc3TN9s4L'.format(page)
    urlist.append(page_link)

# path chrome driver
path = 'D:\Develop\dev python\Chrome Driver\chromedriver.exe'
# url = 'https://www.lazada.co.id/tag/indomie/?_keyori=ss&catalog_redirect_tag=true&from=input&page=1&q=indomie&spm=a2o4j.searchlist.search.go.4619188fjdOHok'
driver = webdriver.Chrome(executable_path= path)
# # driver.maximize_window()
# driver.get(url)


# WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#root')))
# time.sleep(2)
productAll= []
products =[]


# looping untuk dapat halaman berikutnya 
for i in range(len(urlist)):
    # page_link = 'https://www.lazada.co.id/tag/wardah/?_keyori=ss&catalog_redirect_tag=true&from=input&page={}&q=wardah&spm=a2o4j.searchlist.search.go.3ebf40a0S96hsC'.format(i)
    driver.get(urlist[i])
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#root')))
    time.sleep(2)
    # html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # product_name, product_price, product_sold, product_location = [], [], [], []

    for items in soup.findAll('div', class_= 'Bm3ON'):
        product_name = items.find('div', class_= 'RfADt').text
        product_price = items.find('div', class_= 'aBrP0').text 
        product_location = items.find('span', class_= 'oa6ri').text 
        product_sold = items.find('div', class_= '_6uN7R').text
        # review_count = items.find('span', class_= 'qzqFw').text

        products.append(
            (product_name, product_price, product_location, product_sold)
            )
        # productAll.extend(products)
    time.sleep(4)
    # driver.find_element(By.CSS_SELECTOR, '.ant-pagination-next > button').click()
    # time.sleep(3)
df =  pd.DataFrame(data= products, columns= ['product_name', 'product_price','product_location', 'product_sold'])
print(df)
print('jumlah produk :', len(products))

# for items in soup.findAll('div', class_= 'Bm3ON'):
#     for items in soup.findAll('span', class_= '_1cEkb'):
#         product_sold = items.find('span').text 
#         products.append((product_sold))

    

# df =  pd.DataFrame(data= products, columns= ['Sold_product'])
# print(df)
df.to_csv('lazada-soup-malaysia-milo.csv', index= False)

driver.close()
