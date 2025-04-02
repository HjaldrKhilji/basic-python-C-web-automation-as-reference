from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
#websites change so does this script has to too so unless u mantain the script, the script might become outdated for
#any future versions of the site.
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://tiktok.com")

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/button").click() #clicking on the search button to drag open the search box

    #the three lines below simply give input to the search box and wait for 5 seconds
search_input_box=driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div[2]/form/input")
search_input_box.send_keys("a")
time.sleep(5)
results_path="/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div[2]/ul"
results=driver.find_element(By.XPATH, results_path)
inner_html_of_results=results.get_attribute('innerHTML')
soap = BeautifulSoup(inner_html_of_results, 'html.parser')
results_after_clicking_all_non_account_elements=[]
i=0
for sub_element in soap.find_all(True):
    i+=1
    if sub_element.get_text() == "Accounts":
        break
    driver.find_element(By.XPATH, results_path+f"/li[{i}]").click()
    while 1==1:
        try:
            captcha_close=driver.find_element(By.ID,"captcha_close_button").click()
            print("clicked captcha closed once")
            time.sleep(1)
        except:
            print("captcha not found, its a good thing")
            break
    # driver.back() i couldnt use this function cuz the tiktok page was like not actually changing pages but instead changing a certian part of it.
    #this is what i used instead:
    print("done till here")
            
    driver.get("https://tiktok.com")
    print("done till here   22222222222222222")

    # driver.get(driver.getCurrentUrl());
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/button").click() #clicking on the search button to drag open the search box
    search_input_box=driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div[2]/form/input")
    search_input_box.send_keys("a")
    time.sleep(5)

