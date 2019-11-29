from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get('file:///C:/Users/dell/Desktop/Counter%20for%20Messenger%20-%20%E0%A6%B2%20%E0%A6%AC%E0%A6%A8%E0%A7%8D%E0%A6%A6%E0%A7%81%20%E0%A6%AA%E0%A6%BE%E0%A6%97%E0%A6%BF,%E0%A6%95%E0%A6%BF%E0%A6%B0%E0%A6%95%E0%A7%87%E0%A6%9F,%E0%A6%AB%E0%A7%81%E0%A6%A4%E0%A6%AD%E0%A6%B2,%E0%A6%AC%E0%A6%BE%E0%A6%9A%E0%A6%96%E0%A7%87%E0%A6%A4%E0%A6%AD%E0%A6%B2%20%E0%A6%96%E0%A7%87%E0%A6%B2%E0%A6%BF..%20-%2020191127%20-%202.html')
time.sleep(5)

name = []
date = []
message = []


datas =driver.find_elements_by_class_name('box_r')

for data in datas:
	names = data.get_attribute('title')
	dates = data.get_attribute('time')
	messages = data.find_element_by_class_name('message-text').text

	name.append(names)
	date.append(dates)
	message.append(messages)

	

df = pd.DataFrame(list(zip(name, date, message)), columns=['Sender', 'Time', 'Message'])

message_data = df.to_csv('message_data4.csv', index=False)
print('Donee Boss')
