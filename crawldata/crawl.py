from selenium import webdriver
from time import sleep
from random import randint
import csv
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="venv/chromedriver")

for k in range(2,330):
    print(k)
    t = "https://propzy.vn/mua/bat-dong-san/hcm/page-"+str(k)+"?type=mua"
    browser.get(t)
#print(data_list)

    with open('hcm.csv', 'a') as f:
        writer = csv.writer(f)

        sleep(5)
        data_list = browser.find_elements(By.XPATH, "//div[@class='styles__Wrapper-sc-15tjew1-4 fCxcOJ listing-detail']")
        for data in data_list:
            data1 = data.find_element(By.CLASS_NAME,'facilities')
            s=''
            a = []
            k= 0;
            for i in data1.text:
                if(i == '\n'):
                    a.append(s)
                    s=''
                    k+=1
                else:
                    s +=i
            buget = data.find_element(By.CLASS_NAME, 'format-price')
            buget = buget.text[:-3]
            buget = buget.replace(",",".")

            price = data.find_element(By.CLASS_NAME, 'format-unit-price')
            price = price.text[:-9]
            price = price.replace(",", ".")
            area = float(buget)*1000 / float(price)

            local_street = data.find_element(By.CLASS_NAME, 'street')
            local_street = local_street.text[:-1]

            local_ward = data.find_element(By.CLASS_NAME, 'ward')
            local_ward = local_ward.text[:-1]

            local_district = data.find_element(By.CLASS_NAME, 'district')
            local_district = local_district.text[:-1]

            local_city = data.find_element(By.CLASS_NAME, 'city')
            if (k >= 3):
                a[2] = a[2][:-2]
                writer.writerow([a[0],a[1],a[2],buget,price,local_street,local_ward,local_district,local_city.text])
sleep(5)
browser.close()