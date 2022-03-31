a = [1,2,3]
# encoding=utf8
import pickle
import time
import urllib

import chromedriver_binary
import selenium
##
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                NoSuchElementException,
                                WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

print ('st.')

#site = "https://invest.yandex.ru/catalog/fund/fxwo/"

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
#driver.get(site)

#one_prise = driver.find_element_by_id("root")

import requests
from bs4 import BeautifulSoup

#def big_broker(price):
#price2 = price
prise_list = [0]
old_price = 0
prise1 = 0
buy = True
sell = False
site = "https://www.tinkoff.ru/terminal/"

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome()
#driver.get(site)
        #picklein.dump(driver.get_cookies(), open ("session","wb"))
chromedriver = 'C:/broker/chromedriver'
#options = webdriver.ChromeOptions() 

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get(site)
def sell():
    print ('/////////////////sell')
    time.sleep(4)
    element_one =driver.find_element_by_xpath("/html/body/div[3]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[5]/div/div[2]/div[2]/button")
    #                                           /html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div[5]/div[2]
    element_one.click()
    #time.sleep(3)
    #sell = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div/input").send_keys(0)
    #enter = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
    #time.sleep(4)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[3]/div").click()
def buy():
    time.sleep(4)
    element_one =driver.find_element_by_xpath("/html/body/div[3]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[5]/div/div[1]/div[2]/button")
    element_one.click()
    #time.sleep(4)
    #buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div/input").send_keys("\r3")
    #enter = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
    #button_1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[3]/div").click()
    #time.sleep(1)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/button").click()
    #time.sleep(7)
    #button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()
    
def register_on_site():
    #reg_path = "/html/body/div[1]/header/div[2]/div[1]/span[1]" #"/html/body/div[2]/div[1]/header/div/span[2]/a[1]"
    #element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/header/div/span[2]/a[1]")))
    #register = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/span[1]").click()
    yandex_id = "/html/body/div/div[2]/div/div/form/div/div/div/div[1]/label/span"
    password = "/html/body/div[2]/div/div/main/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/input"
    register_id = driver.find_element_by_xpath(yandex_id).send_keys("+79186222038")
    time.sleep(10)
    register_button_1 =driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button").click()
    #/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button
    time.sleep(4)
    #cookie = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button").click()
    register_password = driver.find_element_by_xpath(password).send_keys("135797531AaA")
    time.sleep(40)
    #/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button
    #register_button_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button").click()
    time.sleep(10)
    buy()
    print ("Вызываю buy")

ind = 0
h = 0
index = 0
#register_on_site()
time.sleep(150)
def check():
    driver.get("https://www.tinkoff.ru/terminal/")
    rehtml = driver.page_source
    #url = 'https://invest.yandex.ru/catalog/fund/fxwo/'
    #response = requests.get(site)
    soup = BeautifulSoup(rehtml, 'html5lib')
    quotes = soup.find('div', class_='src-containers-Animated-styles-default-1BbLJ')
    #print (quotes)
    time.sleep(10)
    prise_tin = driver.find_element_by_xpath("/html/body/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[3]/div")
    print (prise_tin.text)
    try:
        for i in quotes:
            quotes = i
            quotes = quotes.replace('₽','')
            quotes = quotes.replace(' ','') # чистим цифры

            newquotes = ""
            b = 0
            for i in quotes:
                b +=1
                if b < 7 and i != ',': # убираем запятую
                    newquotes += i
                    quotes = newquotes # 2 0000
            prise2 = int(newquotes) #2
        #print ("Цена"+ str(prise2))
        price2 = prise2
        #print (price2)
        return price2
        #prise_list.append(int(price2)) # [2]
        #print (prise2) #2
        #print (prise_list) #[2]
    except TypeError:
        print ("Ошибка TypeError")
        pass
my_paper=[]
#price1 = 0#0
i2 = True
n = 0
prise_2 = 0
list_prise = []
flag_buy = 0
stop = 0
stop_list = []
nl = 0
while i2 == True:
    time.sleep(2)
    n +=1
    print (n)
    prise_tin3 = driver.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/div/div/div[1]/div/div[3]").text
    ost_buy = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[5]/div/div[1]/div[1]/div/div").text
    ost_sell = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[5]/div/div[2]/div[1]/div/div").text
    ost_buy = ost_buy.replace("Доступно","")
    ost_sell = ost_sell.replace("Доступно","")
    print (prise_tin3)
    print (ost_buy)
    print (ost_sell)
    quotes = prise_tin3
    quotes = quotes.replace('₽','')
    quotes = quotes.replace(' ','') # чистим цифры # 6400
    quotes = quotes.replace(',','')
    prise_1 = int(quotes)
    if nl < 1111:
        stop_list.append(int(prise_1))
        if nl == 1110:
            a = stop_list[0]
            b = stop_list[-1]
            if b - a < 0:
                c = b - a
                c = c * -1
                if c > 300:
                    print("РЕЗКОЕ ПАДЕНИЕ ФОНДА, ТОРГОВЛЯ ЗАМОРОЖЕНА") 
                    time.sleep(5000)
                    stop_list = []
            else:
                nl = 0
    nl += 1
    if int(ost_sell) > 22 :
        for i in list_prise:
            if prise_1 > (i+4):
                ps = prise_1
                ps2 = format(ps, ',d')
                close = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/span[3]").click()
                prise_sell = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/input").send_keys(ps2)
                sell = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[5]/div/div[2]/div[2]/button").click()
                print ("Старая цена: " + str(i) + "  Новая цена: " + str(prise_1) + "Выстовляю на продажу за: " + str(ps2))
                list_prise.remove(i)
    if int(ost_buy) > 22:
        flag_buy += 1
        if flag_buy % 5 == 0:
            if prise_2 > prise_1 and prise_2 != 0:
                #prise_button_1 = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[9]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/input").send_keys(buy_prise)
                ps_2 = prise_1 - 0 
                ps_3 = format(ps_2, ',d')
                time.sleep(3)
                close = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/span[3]").click()
                time.sleep(3)
                prise_sell = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/input").send_keys(ps_3)
                time.sleep(3)
                buy = driver.find_element_by_xpath("/html/body/div[1]/main/div/section/div[3]/div[2]/div/div[1]/div/div[10]/div/div[1]/div[2]/div[5]/div/div[1]/div[2]/button").click()
                print ("Старая цена: " + str(prise_2) + "  Новая цена: " + str(prise_1) + "Выстовляю на покупку за: " + ps_3)
                list_prise.append(int(prise_1))
    prise_2 = prise_1
    print (list_prise)
while i2 == True: 
    try:
        k = 0
        #check() 
        index +=1
        print (index)                                                                                             # Парсим цену
        price2 = check()
        #with open("C:/broker/log.txt", "a") as file:
        #    file.write(str(" " + str(price2))) 
        print ("Старая цена : " + str(prise1))  
        print ("Новая цена : " + str(price2))  
        print (my_paper)
        try:
            button_exit = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()
            print ("Убрал нежелательный урон")
        except:
            print ("Нет нежелательного элемента")   
        if price2 != prise1 and prise1 != 0 and len(str(price2)) == 5 :     
            try:                                                                                                # Если цена изменилась и старая цена не равна 0 то:
                if price2 < prise1 : # покупаю                                                                  # Если новая цена меньше старой то:
                    difference = prise1 - price2 
                    try:
                        if difference > 20:
                            print ("Разница : " +str(difference))
                            time.sleep(2)
                            bytton_fast_buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/button").click()                                                        # Покупаю
                            time.sleep(4)
                            button_3 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div/div/div").click()
                            time.sleep(4)
                            prise = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/ul[1]/li[1]/div[2]")
                            #global prise_2 
                            prise_2 = prise.text
                            prise_2 = prise_2.replace(" ","")
                            prise_2 = prise_2.replace("₽","")
                            prise_2 = prise_2.replace(",","")
                            prise_2 = prise_2.replace("\u202f\u202f", "")
                            print(prise_2)
                            time.sleep(10)
                            button_exit = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/button").click()
                            my_paper.insert(0,prise_2)
                            buy()
                            with open("C:/broker/log.txt", "a", encoding="utf-8") as file:
                                file.write(" " + str(prise_2)) 
                            print ("/////////////////////Покупаю")
                            #with open("C:/broker/log.txt", "w") as file:
                            #    file.write(str(my_paper))                                                          # В список добавляется купленная акция
                            #print ("Комиссия : " + str(price2*0.025))
                        else:
                            print ('Маленькая цена для покупки :'+ str(difference))
                    except NoSuchElementException:    
                        print ("Повторная покупка ошибка : NoSuchElementException")
                        print ("Не купил")
                        buy()
                        pass
                    except WebDriverException:
                        print ("Повторная покупка ошибка : WebDriverException")
                        print ("Не купил")
                        pass
                    except ElementClickInterceptedException:
                        print ("Повторная покупка ошибка : ElementClickInterceptedException")
                        print ("Не купил")
                        pass

            except TypeError:
                pass
            except NoSuchElementException:
                pass
    except:
        pass      
    #else:
        #if prise1  == 0:                                                                            # Если старая цена равна 0 то:
            #prise1 = price2
    #prise1 = price2      
