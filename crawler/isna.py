#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options=chrome_options)

def write_lists_to_csv_with_header(list_a, list_b, csv_file_name):
    # Combine the lists using zip
    combined_lists = list(zip(list_a, list_b))

    # Specify the header
    header = ['Class', 'Text']

    # Write the combined lists to a CSV file with two columns and a header
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        # Write the header
        csv_writer.writerow(header)

        # Write the data
        csv_writer.writerows(combined_lists)

    print(f'CSV file "{csv_file_name}" has been created.')


def get_isna():

    list_of_sub_link = []
    text_list = []

    # -----------------------Culture-----------------------
    for i in range(1,10):
        link = f'https://www.isna.ir/archive?pi={i}&tp=20&ms=0&dy=21&mn=10&yr=1402&ty=1'
        driver.get(link)
        urls_div = driver.find_element(By.CLASS_NAME, 'box.card.horizontal.full-card.bottom-fade._cyan')
        all_links = urls_div.find_elements(By.TAG_NAME, 'a')
        list_of_sub_link = set(list_of_sub_link)
        for i in all_links:
            if len(list_of_sub_link) < 50 :
                list_of_sub_link.add(i.get_attribute('href'))
            else:
                break
    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body.content-full-news').text
            text_list.append(str(a))
        except:
            text_list.append(f'{i} error')
    write_lists_to_csv_with_header(['culture']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/isna/culture.csv')

    list_of_sub_link = []
    text_list = []

    # -----------------------Politics-----------------------
    for i in range(1,5):
        link = f'https://www.isna.ir/archive?pi={i}&tp=14&ms=0&dy=21&mn=10&yr=1402&ty=1'
        driver.get(link)
        urls_div = driver.find_element(By.CLASS_NAME, 'box.card.horizontal.full-card.bottom-fade._cyan')
        all_links = urls_div.find_elements(By.TAG_NAME, 'a')
        list_of_sub_link = set(list_of_sub_link)
        for i in all_links:
            if len(list_of_sub_link) < 50 :
                list_of_sub_link.add(i.get_attribute('href'))
            else:
                break
    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body.content-full-news').text
            text_list.append(str(a))
        except:
            text_list.append(f'{i} error')
    write_lists_to_csv_with_header(['politics']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/isna/politics.csv')

    list_of_sub_link = []
    text_list = []

    #-----------------------Sport-----------------------
    for i in range(1,10):
        link = f'https://www.isna.ir/archive?pi={i}&tp=24&ms=0&dy=21&mn=10&yr=1402&ty=1'
        driver.get(link)
        urls_div = driver.find_element(By.CLASS_NAME, 'box.card.horizontal.full-card.bottom-fade._cyan')
        all_links = urls_div.find_elements(By.TAG_NAME, 'a')
        list_of_sub_link = set(list_of_sub_link)
        for i in all_links:
            if len(list_of_sub_link) < 50 :
                list_of_sub_link.add(i.get_attribute('href'))
            else:
                break
    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body.content-full-news').text
            text_list.append(str(a))
        except:
            text_list.append(f'{i} error')
    write_lists_to_csv_with_header(['sport']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/isna/sport.csv')

    list_of_sub_link = []
    text_list = []

    #-----------------------Economy-----------------------
    for i in range(1,10):
        link = f'https://www.isna.ir/archive?pi={i}&tp=34&ms=0&dy=21&mn=10&yr=1402&ty=1'
        driver.get(link)
        urls_div = driver.find_element(By.CLASS_NAME, 'box.card.horizontal.full-card.bottom-fade._cyan')
        all_links = urls_div.find_elements(By.TAG_NAME, 'a')
        list_of_sub_link = set(list_of_sub_link)
        for i in all_links:
            if len(list_of_sub_link) < 50 :
                list_of_sub_link.add(i.get_attribute('href'))
            else:
                break
    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body.content-full-news').text
            text_list.append(str(a))
        except:
            text_list.append(f'{i} error')
    write_lists_to_csv_with_header(['economy']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/isna/economy.csv')


def create_folder(folder_name, name):
    folder_name += f'/{name}' 
    try:
        # Create a folder in the current working directory
        os.mkdir(folder_name)
        print(f'Folder "{folder_name}" created successfully.')
    except FileExistsError:
        print(f'Folder "{folder_name}" already exists.')

create_folder(os.path.dirname(__file__), 'isna')

get_isna()
